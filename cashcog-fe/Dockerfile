FROM node:13-alpine as build-node

WORKDIR /opt/app/

RUN npm install -g @angular/cli@9.0.6

ADD package*.json /opt/app/
RUN npm install

ADD . /opt/app/
RUN npm run build

FROM nginx:1.16.0-alpine

RUN sed -i "s/index.*index.html index.htm;/index  index.html index.htm;\n        try_files \$uri \$uri\/ \/index.html \/index.htm;/g" /etc/nginx/conf.d/default.conf
COPY --from=build-node /opt/app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
