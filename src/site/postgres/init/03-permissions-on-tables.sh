#!/bin/sh

set -o errexit

main () {
  grant_blog_permissions
}

grant_blog_permissions() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    \c ataraxiadb;
    GRANT ALL PRIVILEGES ON TABLE posts TO $ATARAXIA_DB_USER;
    GRANT USAGE, SELECT ON SEQUENCE posts_id_seq TO $ATARAXIA_DB_USER;
EOSQL
}

main "$@"
