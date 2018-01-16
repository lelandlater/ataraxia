FROM golang:alpine AS build-env
MAINTAINER 'Leland Later <llater@ataraxia.io>'
ADD . /src
RUN apk add --no-cache git ca-certificates tzdata && \
    go get github.com/sirupsen/logrus \
    github.com/gorilla/mux github.com/lib/pq
RUN cd /src && go build -v -o ataraxia

FROM alpine:3.6
RUN apk add --no-cache ca-certificates
WORKDIR /app
COPY --from=build-env /src/ /app/
ENTRYPOINT ./ataraxia