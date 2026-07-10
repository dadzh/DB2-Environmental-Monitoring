FROM php:8.2-apache

RUN apt-get update && apt-get install -y autoconf g++ make pkg-config libssl-dev libcurl4-openssl-dev \
    && docker-php-ext-install mysqli \
    && pecl install mongodb-1.20.1 \
    && docker-php-ext-enable mongodb

COPY . /var/www/html/
