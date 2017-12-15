FROM golang:alpine
MAINTAINER 'Leland Later <llater@ataraxia.io>'
ADD . /src
RUN apk add --no-cache git ca-certificates tzdata && \
    go get github.com/sirupsen/logrus github.com/gorilla/mux
RUN cd /src && go build -v -o ataraxia
