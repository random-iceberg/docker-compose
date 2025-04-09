import os
import json
import fnmatch
import mimetypes

# Define the extensions that require partial content
PARTIAL_READ_EXTENSIONS = {'.csv', '.jsonl', '.txt', '.log'}  # Add more extensions as needed

# Initialize explicit filenames to ignore
EXPLICIT_IGNORE_FILES = {'LICENSE', 'output.json', 'CHANGELOG.md', '.dockerignore', '.gitignore', 'package-lock.json', 'dir_to_json.py', 'services/fullstack-solutions/next-saas/README.md'}  # Default filenames

# Initialize explicit folders to ignore entirely (except we still show their names)
EXPLICIT_IGNORE_FOLDERS = {
    '*/node_modules',  # Example folder to ignore entirely
    'venv',
    '*/.next',
    '.next',
    'services/billing-service',
    'services/user-service'
    # '.github',
    # '.devcontainer'
    # Add more folder patterns as needed
}

def parse_ignore_file(ignore_file_path):
    """
    Parses an ignore file and returns a set of filenames to ignore.
    """
    ignored_files = set()
    try:
        with open(ignore_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignored_files.add(line)
    except FileNotFoundError:
        pass  # If .ignore file does not exist, proceed with default ignore list
    return ignored_files

# Optionally, extend the ignore list by parsing an external .ignore file
IGNORE_FILE_PATH = os.path.join('.', '.ignore')  # Adjust the path if necessary
EXPLICIT_IGNORE_FILES.update(parse_ignore_file(IGNORE_FILE_PATH))

def read_partial_file(file_path, first_n=10, last_m=5):
    """
    Reads the first `first_n` lines and the last `last_m` lines of a file.
    Inserts '...' if the file has more than `first_n` lines.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            first_lines = []
            last_lines = []
            total_lines = 0
            for line in file:
                total_lines += 1
                safe_line = line.rstrip('\n').replace('`', '~')
                if total_lines <= first_n:
                    first_lines.append(safe_line)
                last_lines.append(safe_line)
                if len(last_lines) > last_m:
                    last_lines.pop(0)

        if total_lines <= first_n:
            return '\n'.join(first_lines)
        else:
            return '\n'.join(first_lines) + '\n...\n' + '\n'.join(last_lines)
    except Exception:
        return "..."

def read_file(file_path):
    """
    Reads a file and returns its content appropriately, handling different file types.
    For specified extensions, it returns a partial content with '...'.
    For image files, it returns '...'.
    For other text files, it returns the full content with backticks replaced by tildes.
    """
    try:
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type and mime_type.startswith('image'):
            return "..."

        _, ext = os.path.splitext(file_path)
        if ext.lower() in PARTIAL_READ_EXTENSIONS:
            return read_partial_file(file_path)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content.replace('`', '~')
    except (UnicodeDecodeError, FileNotFoundError):
        return "..."

def parse_gitignore(gitignore_path):
    """
    Parses a .gitignore file and returns a list of ignore patterns.
    """
    ignore_patterns = []
    try:
        with open(gitignore_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    except FileNotFoundError:
        pass
    return ignore_patterns

def is_ignored(file_path, ignore_patterns):
    """
    Checks if a file path matches any of the ignore patterns (like from .gitignore).
    """
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(file_path, pattern):
            return True
    return False

def is_folder_ignored(folder_path, ignore_folder_patterns):
    """
    Checks if a folder path matches any of the explicit folder ignore patterns.
    We test both `folder_path` and './folder_path' to be more robust with patterns.
    """
    for pattern in ignore_folder_patterns:
        # Try matching the exact relative path
        if fnmatch.fnmatch(folder_path, pattern):
            return True
        # Also try prefixing with "./" for patterns that start that way
        alt_path = './' + folder_path.lstrip('./')
        if fnmatch.fnmatch(alt_path, pattern):
            return True
    return False

def is_in_submodule(file_path, submodule_paths):
    """
    Checks if a file path is within any of the submodule paths.
    """
    for submodule_path in submodule_paths:
        # Normalize to handle potential trailing slashes
        if file_path.startswith(submodule_path.rstrip(os.sep)):
            return True
    return False

def dir_to_json(directory, submodules, ignore_submodules=False):
    """
    Converts a directory structure into a JSON object, optionally ignoring submodules.
    Allows ignoring certain folders (EXPLICIT_IGNORE_FOLDERS) so that:
      - The folder name appears
      - Its contents do not appear
    """
    result = {}
    ignore_patterns = ['.git', '.git/*']
    submodule_paths = [os.path.join(directory, submodule['path']) for submodule in submodules]

    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            dirs.remove('.git')

        relative_root = os.path.relpath(root, directory)
        if relative_root == ".":
            relative_root = ""

        # If ignoring submodules, skip entire submodule if no README in it
        if ignore_submodules and is_in_submodule(root, submodule_paths) and not any('README' in file for file in files):
            continue

        # Parse .gitignore in the current root
        gitignore_path = os.path.join(root, '.gitignore')
        ignore_patterns += parse_gitignore(gitignore_path)

        # Navigate into the JSON structure for the current folder
        sub_result = result
        if relative_root:
            for part in relative_root.split(os.sep):
                sub_result = sub_result.setdefault(part, {})

        # Check subfolders against EXPLICIT_IGNORE_FOLDERS before descending
        # We'll build a list of folders we intend to skip
        folders_to_skip = []
        for d in dirs:
            folder_relative_path = os.path.join(relative_root, d) if relative_root else d
            if is_folder_ignored(folder_relative_path, EXPLICIT_IGNORE_FOLDERS):
                # Record this folder in the JSON as empty dict
                sub_result.setdefault(d, {})
                # Mark it to be removed from recursion
                folders_to_skip.append(d)

        # Remove the ignored folders so we don't walk into them
        for d in folders_to_skip:
            dirs.remove(d)

        # Now proceed with files in this directory
        for file in files:
            if file in EXPLICIT_IGNORE_FILES:
                continue

            file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(file_path, directory)

            # Check if file is ignored by .gitignore or submodules
            if is_ignored(relative_file_path, ignore_patterns):
                continue
            if ignore_submodules and is_in_submodule(file_path, submodule_paths) and 'README' not in file:
                continue

            file_content = read_file(file_path)
            sub_result[file] = file_content

    return result

def load_submodules(gitmodules_path):
    """
    Loads submodules from the .gitmodules file.
    Returns a list of dicts, where each dict has {'path': <submodule_path>}.
    """
    submodules = []
    try:
        with open(gitmodules_path, 'r', encoding='utf-8') as gitmodules_file:
            current_submodule = None
            for line in gitmodules_file:
                line = line.strip()
                if line.startswith('[submodule'):
                    if current_submodule:
                        submodules.append(current_submodule)
                    current_submodule = {}
                elif line.startswith('path') and current_submodule is not None:
                    _, path = line.split('=', 1)
                    current_submodule['path'] = path.strip()
            if current_submodule:
                submodules.append(current_submodule)
    except FileNotFoundError:
        pass
    return submodules

def main(directory='.', ignore_submodules=False):
    """
    Main function to generate the directory structure in JSON format.
    """
    gitmodules_path = os.path.join(directory, '.gitmodules')
    submodules = load_submodules(gitmodules_path)

    json_data = dir_to_json(directory, submodules, ignore_submodules)
    json_output = os.path.join(directory, 'output.json')

    with open(json_output, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    print(f"JSON data has been written to {json_output}")

if __name__ == "__main__":
    # Call the main function with directory and submodule ignore flag
    main(directory='.', ignore_submodules=False)
