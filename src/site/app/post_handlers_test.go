package main

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"net/url"
	"strconv"
	"testing"
)

func TestGetPostHandler(t *testing.T) {

	posts = []Post{
		{"Reading List 2017", "December 31", "This is my reading list for 2017."},
	}

	req, err := http.NewRequest("GET", "", nil)

	if err != nil {
		t.Fatal(err)
	}

	recorder := httptest.NewRecorder()

	hf := http.HandlerFunc(getPostHandler)

	hf.ServeHTTP(recorder, req) // sends a one-odd request to the handler, with a "recorder" server

	if status := recorder.Code; status != http.StatusOK {
		t.Errorf("Handler returned wrong status code: got %v want %v",
			status, http.StatusOK)
	}

	expected := Post{"Reading List 2017", "December 31", "This is my reading list for 2017."}
	p := []Post{}
	err = json.NewDecoder(recorder.Body).Decode(&p)

	if err != nil {
		t.Fatal(err)
	}

	actual := p[0]

	if actual != expected {
		t.Errorf("Handler returned unexpected body: got %v want %v", actual, expected)

	}
}

func TestCreatePostsHandler(t *testing.T) {

	posts = []Post{
		{"Reading List 2017", "December 31", "This is my reading list for 2017."},
	}

	form := newCreatePostForm()
	req, err := http.NewRequest("POST", "", bytes.NewBufferString(form.Encode()))

	req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	req.Header.Add("Content-Length", strconv.Itoa(len(form.Encode())))
	if err != nil {
		t.Fatal(err)
	}

	recorder := httptest.NewRecorder()

	hf := http.HandlerFunc(createPostHandler)

	hf.ServeHTTP(recorder, req)

	if status := recorder.Code; status != http.StatusFound {
		t.Errorf("handler returned wrong status code: got %v want %v",
			status, http.StatusOK)

	}

	expected := Post{"Justice Kennedy and Data", "January 1", "Using subset cluster for gerrymandering solution."}

	if err != nil {
		t.Fatal(err)
	}

	actual := posts[1]

	if actual != expected {
		t.Errorf("handler returned unexpected body: got %v want %v", actual, expected)
	}
	}

func newCreatePostForm() *url.Values {
	form := url.Values{}
	form.Set("title", "Justice Kennedy and Data")
	form.Set("date", "January 1")
	form.Set("description", "Using subset cluster for gerrymandering solution.")
	return &form
}
