FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN make html
COPY build/ /usr/share/nginx/html
FROM nginx:alpine
EXPOSE 80