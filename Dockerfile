# Установка базового образа Python
FROM python:3.11

# Установка переменных окружения
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Установка рабочей директории в контейнере
WORKDIR /app

# Копирование зависимостей проекта
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода проекта в контейнер
COPY . .

# Запуск команды миграции базы данных и сбор статических файлов
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

# Открытие порта, на котором будет работать Django сервер
EXPOSE 8000

# Запуск команды для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

