FROM node:latest AS builder

RUN mkdir /app && mkdir /app/data

COPY . /app

RUN cd /app && yarn install && \
    yarn build 



FROM node:latest

RUN mkdir /app

COPY --from=builder /app/build /app/build
COPY --from=builder /app/package.json /app/yarn.lock /app/
COPY --from=builder /app/server.js /app/
COPY --from=builder /app/ssl /app/ssl
COPY --from=builder /app/node_modules /app/node_modules
RUN cd /app && \ 
    yarn install --production && \
    yarn cache clean

WORKDIR /app
EXPOSE 3000
# CMD ["node", "build/index.js"]
CMD ["node","server.js"]