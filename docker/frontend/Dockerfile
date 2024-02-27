ARG NODE_VERSION=20.10.0


FROM node:${NODE_VERSION}-alpine as base
ENV NODE_ENV=production

WORKDIR /src

#build
FROM base as build
COPY ../../frontend/package*.json ../../frontend/yarn.lock ./
RUN yarn install
COPY ../../frontend .
RUN yarn build 

#run 
FROM base
COPY --from=build /src/.output /src/.output
ENV HOST 0.0.0.0
EXPOSE 3000

