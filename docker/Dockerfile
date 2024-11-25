FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN sphinx-build -b html source build
RUN make html
FROM nginx:alpine
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY build/html/ /usr/share/nginx/html/
EXPOSE 80