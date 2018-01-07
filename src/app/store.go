package main

import (
	"database/sql"
)

type Store interface {
	CreatePost(post *Post) error
	GetPosts() ([]*Post, error)
}

type dbStore struct {
	db *sql.DB
}

func (store *dbStore) CreatePost(post *Post) error {
	_, err := store.db.Query("INSERT INTO posts(title, date, description) VALUES ($1,$2)", post.Title, post.Date, post.Description)
	return err
}

func (store *dbStore) GetPosts() ([]*Post, error) {
	rows, err := store.db.Query("SELECT title, date, description from posts")

	if err != nil {
		return nil, err
	}
	defer rows.Close()

	posts := []*Post{}
	for rows.Next() {
		post := &Post{}

		if err := rows.Scan(&post.Title, &post.Date, &post.Description); err != nil {
			return nil, err
		}
		posts = append(posts, post)
	}
	return posts, nil
}

var store Store

func InitStore(s Store) {
    store = s

    }