FROM mysql:latest

# 初始化超市项目数据库
COPY supermarket.sql /docker-entrypoint-initdb.d/
# 设置密码
ENV MYSQL_ROOT_PASSWORD=sysu

# docker build -t sm-db-img:1.0.0 .
# docker run -d -p 3306:3306 --name sm-db sm-db-img:1.0.0
# docker logs sm-db
