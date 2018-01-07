package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Post struct {
	Title       string `json:"title"`
	Date        string `json:"date"`
	Description string `json:"description"`
}

var posts []Post

func getPostHandler(w http.ResponseWriter, r *http.Request) {
	// convert variable to json
	postListBytes, err := json.Marshal(posts)
	if err != nil {
		fmt.Println(fmt.Errorf("Error: %v", err))
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
    w.Write(postListBytes)
}

func createPostHandler(w http.ResponseWriter, r *http.Request) {
	post := Post{}
	// send all data as HTML form data
	err := r.ParseForm()

	if err != nil {
		fmt.Println(fmt.Errorf("Error: %v", err))
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	post.Title = r.Form.Get("title")
	post.Date = r.Form.Get("date")
	post.Description = r.Form.Get("description")

	posts = append(posts, post)

	http.Redirect(w, r, "/assets/", http.StatusFound)
}