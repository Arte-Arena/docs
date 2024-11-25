FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app/
RUN sphinx-build /app /app/_build/html -b dirhtml

FROM nginx:latest

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/_build/html /usr/share/nginx/html
EXPOSE 80