package main

import (
	"database/sql"
	"testing"
	"github.com/stretchr/testify/suite"
)

type StoreSuite struct {
	suite.Suite
	/*
	Any variables that are to be shared between tests in a
	suite should be stored as attributes of the suite instance
	*/
	store *dbStore
	db    *sql.DB
}

func (s *StoreSuite) SetupSuite() {
	connString := "dbname=ataraxiadb-test"
}