FROM node:10.21.0

WORKDIR /opt/gitbook

RUN npm install gitbook-cli  -g && gitbook -v && gitbook install

EXPOSE 4000

CMD ["gitbook", "serve"]