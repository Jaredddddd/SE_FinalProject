FROM python:latest

WORKDIR /app

COPY ./server /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 666

CMD ["python", "app.py"]

# docker build -t sm-flask-img:1.0.0 .
# docker run -d -p 666:666 --name sm-flask sm-flask-img:1.0.0
