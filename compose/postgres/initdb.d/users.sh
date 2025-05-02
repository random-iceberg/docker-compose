#!/bin/bash
set -eu

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOF
	CREATE ROLE backend LOGIN PASSWORD '$POSTGRES_PASSWORD_BACKEND';
	CREATE DATABASE backend;
	GRANT ALL PRIVILEGES ON DATABASE backend TO backend;

	\c backend postgres
	GRANT ALL ON SCHEMA public TO backend;
EOF
