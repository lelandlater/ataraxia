#!/bin/sh

# exit immediately when encountering an error
set -o errexit

readonly REQUIRED_ENV_VARS=(
  "ATARAXIA_DB_USER"
  "ATARAXIA_DB_PASSWORD"
  "ATARAXIA_DB_DATABASE"
  "POSTGRES_USER")

main() {
  check_env_vars_set
  init_user_and_db
}

# checks all env variables set
check_env_vars_set() {
  for required_env_var in ${REQUIRED_ENV_VARS[@]}; do
    if [[ -x "${!required_env_var}" ]]; then
      echo "Error:
    Environment variable '$required_env_var' not set.
    Make sure you have th following enviornment variables set:

      ${REQUIRED_ENV_VARS[@]}

Aborting."
      exit 1
    fi
  done
}

# initialization with preconfigured postgres user
init_user_and_db() {
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER $ATARAXIA_DB_USER WITH PASSWORD '$ATARAXIA_DB_PASSWORD';
    CREATE DATABASE $ATARAXIA_DB_DATABASE;
    GRANT ALL PRIVILEGES ON DATABASE $ATARAXIA_DB_DATABASE TO $ATARAXIA_DB_USER;
EOSQL
}
 
main "$@"

