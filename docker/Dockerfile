FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN make html
FROM nginx:alpine
COPY ./build/html/ /usr/share/nginx/html/
COPY docker/nginx.conf /etc/nginx/
EXPOSE 80
