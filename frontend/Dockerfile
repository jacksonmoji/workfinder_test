###########
# BUILDER #
###########

# pull official base image
FROM node:14.16.1-alpine3.10 as builder

# set work directory
WORKDIR /usr/src/app

# install dependencies and avoid `node-gyp rebuild` errors
COPY ./app/package.json .
RUN apk add --no-cache --virtual .gyp \
    python \
    make \
    g++ \
    && npm install \
    && apk del .gyp

# copy our react project
COPY ./app .

# perform npm build

RUN npm run build

#########
# FINAL #
#########

# pull official base image
FROM node:14.16.1-alpine3.10

# set work directory
WORKDIR /usr/src/app

# install serve - deployment static server suggested by official create-react-app
RUN npm install -g serve

# copy build files from builder stage
COPY --from=builder /usr/src/app/build ./build