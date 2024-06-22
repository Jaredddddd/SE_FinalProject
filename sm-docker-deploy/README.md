### 基于docker的自动化部署

通过`Docker`部署主要是用方便跨平台和简化环境配置，由于该项目是比较简单的单体应用，所以没有用到容器编排工具。**部署到不同服务器的时候需要注意异步请求的`IP`地址同步更改(给出的代码均适用于单机部署)**



- `Docker`版本：`Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1`

- 测试的服务器信息：

  ```
  Distributor ID: Ubuntu
  Description:    Ubuntu 22.04.4 LTS
  Release:        22.04
  Codename:       jammy



#### 数据库部署

1. 将数据库初始化文件放到和`Dockerfile`同级的目录下

   ```dockerfile
   FROM mysql:latest
   
   COPY supermarket.sql /docker-entrypoint-initdb.d/
   
   ENV MYSQL_ROOT_PASSWORD=sysu
   ```

2. 创建镜像并实例化容器，注意暴露端口

   ```shell
   docker build -t sm-db-img:1.0.0 .
   
   docker run -d -p 3306:3306 --name sm-db sm-db-img:1.0.0
   
   docker logs sm-db
   ```

> 两个可自行选择的点：
>
> 1. 可以通过数据卷的方式将MySQL配置文件挂载出来
> 2. 可以通过环境变量的方式指定数据库密码，避免在Dockerfile中明文给出



#### 后端服务器部署

1. 后端是简易的Flask服务器，基于`python`镜像创建服务器镜像并安装对应包即可

   ```dockerfile
   FROM python:latest
   
   WORKDIR /app
   
   COPY ./server /app
   
   RUN pip install --no-cache-dir -r requirements.txt
   
   EXPOSE 666
   
   CMD ["python", "app.py"]
   ```

2. 创建镜像并实例化容器，注意对外端口

   ```shell
   docker build -t sm-flask-img:1.0.0 .
   
   docker run -d -p 666:666 --name sm-flask sm-flask-img:1.0.0
   ```

   

#### 前端服务器部署

1. 前端将打包后的网站页面放到`Nginx`服务器上，所以只需基于`nginx`镜像创建新镜像并将页面整合到镜像中即可

   ```dockerfile
   FROM nginx:latest
   
   COPY ./dist /usr/share/nginx/html/dist
   
   COPY ./default.conf /etc/nginx/conf.d/default.conf
   
   EXPOSE 80
   ```

   `Nginx`需要进行一些网页重定向的配置，可以自定根据自己网页的位置和组织方式配置各种规则，这里给出一般的规则：

   ```nginx
   ####################default.conf####################
   # 负载均衡
   upstream backend-servers {
       server 127.0.0.1:5000;
       
   }
   
   server {
       listen       80;
       server_name  127.0.0.1;  # 服务器ip
   
       # 用location定义路径，访问 127.0.0.1:80/ 目录则返回root
       location / {
           root   /usr/share/nginx/html/dist;  # 指定根目录
           try_files $uri $uri/ @router;  # 路由重写规则
           index  index.html index.htm;    # 响应的页面文件
       }
   
       # 路由重写规则，表明任意不存在的页面则重写到index.html
       location @router {
           rewrite ^.*$ /index.html last;  
       }
   
       # 反向代理，这里暂时没有用到
       location /api/ {
           proxy_pass http://192.168.0.24:7830/api/;
       }
   
       #error_page  404              /404.html;
   
       # 服务端错误也重定位到/usr/share/nginx/html/dist下的网页(5xx)
       location = /50x.html {
           root   /usr/share/nginx/html/dist;
       }
   } 
   ```

2. 创建镜像并实例化容器，注意对外端口

   ```shell
   docker build -t sm-vue-img:1.0.0 .
   
   docker run -d -p 80:80 --name sm-vue -d sm-vue-img:1.0.0
   ```