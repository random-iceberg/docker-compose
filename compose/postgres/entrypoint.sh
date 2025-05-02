#!/usr/bin/env bash
set -eu

update_script=$(
    cat <<-EOF
    ALTER USER postgres WITH PASSWORD '$POSTGRES_PASSWORD';
    ALTER USER backend WITH PASSWORD '$POSTGRES_PASSWORD_BACKEND';
EOF
)

function update() {
    # Wait for the database
    while ! pg_isready --username "$POSTGRES_USER" --dbname "$POSTGRES_DB"; do
        echo Waiting for the database to be ready
        sleep 1
    done

    # Set the passwords
    echo Update the passwords
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<<$update_script
}

# Update the passwords asynchronously
update &

# Execute the original entry points
exec docker-entrypoint.sh "$@"
