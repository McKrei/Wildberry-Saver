# Используем базовый образ Python
FROM python:3.8

# Установка переменной окружения для установки вывода Python в буферизованный режим (для лучшей производительности в Docker)
ENV PYTHONUNBUFFERED 1

# Создание и переключение в рабочую директорию /app
WORKDIR /projectWB

# Копирование зависимостей в контейнер
COPY requirements.txt .

# Установка зависимостей с помощью pip
RUN pip install -r requirements.txt

# Копирование остальных файлов в контейнер
COPY . .

# Установка команды запуска приложения через Gunicorn
CMD ["gunicorn", "--workers", "1", "--bind", "0.0.0.0:5000", "app:app"]
