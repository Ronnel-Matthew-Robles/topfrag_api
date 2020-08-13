# Use an official node runtime as a parent image
FROM node:14.8.0-alpine3.10

WORKDIR /topfrag_frontend

# Install dependencies
COPY package.json /topfrag_frontend

RUN npm install

# Add rest of the client code
COPY . /topfrag_frontend

EXPOSE 3000

CMD npm start
