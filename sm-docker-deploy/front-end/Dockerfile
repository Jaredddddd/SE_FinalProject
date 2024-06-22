FROM nginx:latest

COPY ./dist /usr/share/nginx/html/dist

COPY ./default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# docker build -t sm-vue-img:1.0.0 .
# docker run -d -p 80:80 --name sm-vue -d sm-vue-img:1.0.0