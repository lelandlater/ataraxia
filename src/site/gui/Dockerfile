FROM mhart/alpine-node
MAINTAINER 'Leland Later <lelandlater@gmail>'
RUN npm install create-react-app --global
WORKDIR /app
RUN create-react-app ataraxia
RUN rm -rf ataraxia/src/* 
COPY src/ ataraxia/src/
WORKDIR /app/ataraxia
RUN yarn build
RUN yarn global add serve
CMD [ "serve", "-s", "build" ]
