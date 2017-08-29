# Cue API

* launch events and share music with your friends in a simple Python web UI 
* provides backend for iOS UI and Android, web
* collects logs and data re: user activity
* beta testing July 2017 - October 2017

### Get

Ask Leland for a tarball

### Requirements 

* AWS CLI, with credentials
* Python3

### Run

From `cue-api/` call `. bin/build`

### Destroy

From `cue-api/` call `. bin/destroy`

## Overview

The Cue API is an authentication-protected interface between the underlying mechanisms supporting multi-user live play queues. The Cue API serves HTTP responses to client end users.

## Goals

* API demo with GUI Fall 17
* MVP early 18
* steady progress each and every week

## Non-goals

* "sell out" 

## Documentation

### code structure

The `api/` directory contains the salient Python codesbase for the underlying REST API. A RAML spec defines usage and endpoints. 

`logic.py` provides the only algorithmically interesting component of Cue: the code that decides which song to play next. This is a work in progress and will certainly require tuning later in development.

`schemas.py` contains marshalling code to ensure well-strucutured responses.

`models.py` represents Python objects for use in the application logic.

`resources.py` contains the Flask-RESTful `Resource` definitions.

### design choices

The Cue API is written with a Cassandra backend to support high write capacity and fast reads for particular queries. The application logic does not allow users to execute a wide range of queries. Rather, the searching will be done within the Spotify API (QUESTION how do I make this as fast as possible... can I add Elasticsearch or Cassandra or Redis backend through which to display spotify search results? Does this require JavaScript?).

I chose Python because it is excellent for making a prototype.

### TODO (for house)

* shirts x2
* CURTAINS
* whiteboard on wall
* soundproofing
* bed
* bedding

### TODO (for code)

* configure database in a function, call that function in run.py, run a test on it to confirm configured correctly on each launch
* other containers operating smoothly from scratch: nginx, cassandra "black box" cluster, gui (very basic but needs to have some interactivity with the app)
* JWT with python or nginx LUA script? are either possible?
* no caching, no bells and whistles, just a demo with a live API (that can be scratched and rebuilt)

### TODO (for code, other)

* bash script that times AWS Cloudformation builds and logs them
