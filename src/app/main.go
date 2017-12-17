package main

import (
	"fmt"
	"github.com/gorilla/mux"
	log "github.com/sirupsen/logrus"
	"net/http"
	"os"
)

func init() {
	log.SetOutput(os.Stdout)
	log.SetLevel(log.DebugLevel)
	log.Debug("Initialized the logger")
}

func newRouter() *mux.Router {
	r := mux.NewRouter()
	r.HandleFunc("/hello", handler).Methods("GET")

	staticFileDirectory := http.Dir("./assets/")

	staticFileHandler := http.StripPrefix("/assets/", http.FileServer(staticFileDirectory))
	r.PathPrefix("/assets/").Handler(staticFileHandler).Methods("GET")
    r.HandleFunc("/add-post", getPostHandler).Methods("GET")
    r.HandleFunc("/add-post", createPostHandler).Methods("POST")
	return r
}

func main() {

	r := newRouter()
	http.ListenAndServe(":8000", r)
}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello")
}
