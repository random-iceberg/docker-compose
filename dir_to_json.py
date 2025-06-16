#!/usr/bin/env python3
"""
Converts a directory structure into a JSON object while ignoring specified folders and files.
Specifically, any folder or file named ".git" or ".gitlab" is completely ignored.
"""

import os
import json
import fnmatch
import mimetypes

# Define extensions that require partial file reading
PARTIAL_READ_EXTENSIONS = {'.csv', '.jsonl', '.txt', '.log'}

# Default filenames to ignore
EXPLICIT_IGNORE_FILES = {
    'LICENSE',
    'output.json',
    'CHANGELOG.md',
    '.dockerignore',
    '.gitignore',
    # 'Sprint-1.md',
    # 'Sprint-2.md',
    # 'Sprint-3.md',
    # 'Sprint-4.md',
    'package-lock.json',
    'Project-Charter.md',
    'uv.lock'    
}

# Folders (and file names) to ignore entirely
EXPLICIT_IGNORE_FOLDERS = {
    '.git',
    '.gitlab',
    'node_modules',
    '.venv',
    '__pycache__',
    # '__tests__',
    '__snapshots__',
    'build',
    '.pytest_cache',
    '.ruff_cache'
}

def parse_ignore_file(ignore_file_path):
    """Parse an additional ignore file and return a set of filenames to ignore."""
    ignored_files = set()
    try:
        with open(ignore_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignored_files.add(line)
    except FileNotFoundError:
        pass
    return ignored_files

# Extend ignore files by parsing an external .ignore file if present
IGNORE_FILE_PATH = os.path.join('.', '.ignore')
EXPLICIT_IGNORE_FILES.update(parse_ignore_file(IGNORE_FILE_PATH))

def read_partial_file(file_path, first_n=10, last_m=5):
    """
    Reads the first 'first_n' lines and the last 'last_m' lines of a file.
    Inserts '...' in between if the file has more than 'first_n' lines.
    Replaces all occurrences of '`' with '~' in each line.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            first_lines = []
            last_lines = []
            total_lines = 0
            for line in file:
                total_lines += 1
                # Replace backticks with tildes
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
    Reads a file and returns its content.
    Uses partial content for specific extensions and returns '...' for image files.
    Replaces all occurrences of '`' with '~' in the file content.
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
    Checks if the given file path matches any of the ignore patterns.
    """
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(file_path, pattern):
            return True
    return False

def is_folder_ignored(folder_relative_path):
    """
    Returns True if the folder's name matches any of the explicit ignore folders.
    """
    folder_name = os.path.basename(folder_relative_path)
    return folder_name in EXPLICIT_IGNORE_FOLDERS

def is_in_submodule(file_path, submodule_paths):
    """
    Checks if a file is within any defined submodule paths.
    """
    for submodule_path in submodule_paths:
        if file_path.startswith(submodule_path.rstrip(os.sep)):
            return True
    return False

def dir_to_json(directory, submodules, ignore_submodules=False):
    """
    Walks through the directory structure and returns a nested dict representing the structure.
    Ignores any folders or files named .git or .gitlab.
    """
    result = {}
    ignore_patterns = ['.git', '.git/*']  # Basic patterns for git metadata
    submodule_paths = [os.path.join(directory, submodule['path']) for submodule in submodules]

    for root, dirs, files in os.walk(directory):
        # Remove ignored folders immediately from the directory walk
        dirs[:] = [d for d in dirs if d not in EXPLICIT_IGNORE_FOLDERS]

        relative_root = os.path.relpath(root, directory)
        if relative_root == ".":
            relative_root = ""

        # Optionally ignore submodule directories without a README file
        if ignore_submodules and is_in_submodule(root, submodule_paths) and not any('README' in f for f in files):
            continue

        # Collect .gitignore patterns from the current directory
        gitignore_path = os.path.join(root, '.gitignore')
        ignore_patterns.extend(parse_gitignore(gitignore_path))

        # Navigate into the nested dictionary corresponding to the current directory
        sub_result = result
        if relative_root:
            for part in relative_root.split(os.sep):
                sub_result = sub_result.setdefault(part, {})

        # Process folders: record names and skip traversal into ignored folders (already removed)
        for d in dirs:
            folder_relative_path = os.path.join(relative_root, d) if relative_root else d
            if is_folder_ignored(folder_relative_path):
                sub_result.setdefault(d, {})  # Record the folder name with an empty dict
                # Note: Already filtered out from dirs list
                continue

        # Process files: Skip if the file is explicitly ignored or is named like an ignored folder (.git/.gitlab)
        for file in files:
            if file in EXPLICIT_IGNORE_FILES or file in EXPLICIT_IGNORE_FOLDERS:
                continue
            file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(file_path, directory)
            if is_ignored(relative_file_path, ignore_patterns):
                continue
            if ignore_submodules and is_in_submodule(file_path, submodule_paths) and 'README' not in file:
                continue
            sub_result[file] = read_file(file_path)

    return result

def load_submodules(gitmodules_path):
    """
    Loads submodules defined in the .gitmodules file.
    Returns a list of dictionaries, each containing the 'path' key.
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
    Main function to generate the directory structure JSON output.
    The output is written to 'output.json' in the specified directory.
    """
    gitmodules_path = os.path.join(directory, '.gitmodules')
    submodules = load_submodules(gitmodules_path)
    json_data = dir_to_json(directory, submodules, ignore_submodules)

    json_output = os.path.join(directory, 'output.json')
    with open(json_output, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
    print(f"JSON data has been written to {json_output}")

if __name__ == "__main__":
    main(directory='.', ignore_submodules=False)
