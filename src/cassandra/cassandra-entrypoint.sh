#!/bin/sh
echo "Initializing the database..."
cqlsh -f init-db.cql
echo "Initialized."