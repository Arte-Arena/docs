FROM python:3.11-slim AS builder

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
RUN make html

FROM nginx:latest

COPY ./docker/nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/_build/html /usr/share/nginx/html
EXPOSE 80