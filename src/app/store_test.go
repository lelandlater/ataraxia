package main

import (
	"database/sql"
	"github.com/stretchr/testify/suite"
	"testing"
	_ "github.com/lib/pq"
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
	connString := "user=ataraxia password=this-is-a-password port=5432 host=postgres dbname=ataraxiadb connect_timeout=30 sslmode=disable"
	db, err := sql.Open("postgres", connString)
	if err != nil {
		s.T().Fatal(err)
	}
	s.db = db
	s.store = &dbStore{db: db}
}

func (s *StoreSuite) SetupTest() {
	_, err := s.db.Query("DELETE FROM posts")
	if err != nil {
		s.T().Fatal(err)
	}
}

func (s *StoreSuite) TearDownSuite() {
	s.db.Close()
}

func TestStoreSuite(t *testing.T) {
	s := new(StoreSuite)
	suite.Run(t, s)
}

func (s *StoreSuite) TestCreatePost() {
	s.store.CreatePost(&Post{
		Title:       "Test Post",
		Date:        "December 31",
		Description: "Test description",
	})

	res, err := s.db.Query(`SELECT COUNT(*) FROM posts WHERE description='Test description' AND TITLE='Test Post'`)

	if err != nil {
		s.T().Fatal(err)
	}

	var count int
	for res.Next() {
		err := res.Scan(&count)
		if err != nil {
			s.T().Error(err)
		}
	}

	if count != 1 {
		s.T().Errorf("incorrect count, wanted 1, got %d", count)
	}
}

func (s *StoreSuite) TestGetPost() {

	_, err := s.db.Query(`INSERT INTO posts (title, date, description) VALUES('title', 'date','description')`)
	if err != nil {
		s.T().Fatal(err)
	}

	posts, err := s.store.GetPosts()
	if err != nil {
		s.T().Fatal(err)
	}

	nPosts := len(posts)
	if nPosts != 1 {
		s.T().Errorf("incorrect count")
	}

	expectedPost := Post{"title", "date", "description"}

	if *posts[0] != expectedPost {
		s.T().Errorf("incorrect details, expected %v, got %v", expectedPost, *posts[0])
	}
}
