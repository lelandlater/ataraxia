#!/bin/sh

set -o errexit

main() {
  create_blog_tables
}

create_blog_tables() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    \c ataraxiadb;
    CREATE TABLE posts (
      id SERIAL PRIMARY KEY,
      title VARCHAR(256),
      date TIMESTAMP,
      description VARCHAR(4096)
    );
EOSQL
}

main "$@"
