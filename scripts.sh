#!/bin/bash

# Останавливаем контейнер docker
sudo docker stop wb

# Удаляем контейнер docker
sudo docker rm wb

# Собираем новый образ docker
sudo docker build -t myflaskapp .

# Запускаем контейнер docker
sudo docker run -d --name wb -p 5000:5000 myflaskapp
