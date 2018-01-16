package main

import (
	"testing"
	"net/http"
	"net/http/httptest"
	"io/ioutil"
)

func TestHandler(t *testing.T) {

	req, err := http.NewRequest("GET", "", nil)

	if err != nil {
		t.Fatal(err)
	}

	recorder := httptest.NewRecorder()

	hf := http.HandlerFunc(handler)

	hf.ServeHTTP(recorder, req)

	if status := recorder.Code; status != http.StatusOK {
		t.Errorf("Handler returnmed wrong status code: got %v wanted %v", status, http.StatusOK)
	}

	expected := `Hello`
	actual := recorder.Body.String()
	if actual != expected {
		t.Errorf("Handler returned unexpected body: got %v want %v", actual, expected)
	}
}

func TestRouter(t *testing.T) {

	r := newRouter()

	mockServer := httptest.NewServer(r)

	resp, err := http.Get(mockServer.URL + "/hello")

	if err != nil {
		t.Fatal(err)
	}

	if resp.StatusCode != http.StatusOK {
		t.Errorf("Status should be ok, got %d", resp.StatusCode)
	}

	defer resp.Body.Close()

	b, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		t.Fatal(err)
	}

	respString := string(b)
	expected := "Hello"

	if respString != expected {
		t.Errorf("Response should be %s, got %s", expected, respString)
	}
}

func TestRouterForNonExistentRoute(t *testing.T) {
	r := newRouter()
	mockServer := httptest.NewServer(r)

	// Create an undefined route
	resp, err := http.Post(mockServer.URL+"/hello", "", nil)

	if err != nil {
		t.Fatal(err)
	}

	defer resp.Body.Close()
	b, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		t.Fatal(err)
	}

	respString := string(b)
	expected := ""

	if respString != expected {
         t.Errorf("Response should be %s, got %s", expected, respString)
	}
}