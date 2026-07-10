#  Yatube API

REST API для социальной сети Yatube с поддержкой публикаций, комментариев, сообществ и подписок.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2+-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.12+-red.svg)](https://www.django-rest-framework.org/)

## 📖 Оглавление

- [О проекте](#-о-проекте)
- [Стек технологий](#-стек-технологий)
- [Быстрый старт](#-быстрый-старт)
- [Модели данных](#-модели-данных)
- [Структура проекта](#-структура-проекта)

---

## 📝 О проекте

Yatube API — это RESTful веб-сервис для социальной сети, который предоставляет полный функционал для:
- 📝 Публикации постов с изображениями
- 💬 Комментирования постов
- 👥 Создания сообществ (групп)
- 🔔 Подписки на других пользователей
- 🔐 JWT-аутентификации

API следует принципам REST и использует пагинацию, фильтрацию и поиск.

---

## 🛠 Стек технологий

**Backend:**
- Python 3.9+
- Django 3.2+
- Django REST Framework 3.12+
- djangorestframework-simplejwt (JWT-аутентификация)
- Djoser (регистрация и аутентификация)
- Django-filter (фильтрация)

**Database:**
- SQLite

**Testing:**
- pytest
- pytest-django
- pytest-cov

**Documentation:**
- OpenAPI 3.0.2 (Swagger/Redoc)

---

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/xlllaMaH/api-final-yatube-ad.git
cd yatube_api
```

### 2. Создайте и активируйте виртуальное окружение

Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows:
```bash
py -m venv venv
venv\Scripts\activate
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```
### 4. Примените миграции
```bash
cd yatube_api/
python manage.py migrate
```
### 5. Запустите сервер разработки
```bash
pythom manage.py runserver
```
- API доступно по адресу: http://127.0.0.1:8000/api/v1/
- Документация: http://127.0.0.1:8000/redoc/

---

## 📊 Модели данных

### Post(Публикация)
```json
{
  "id": "integer (read-only)",
  "author": "string (username, read-only)",
  "text": "string (required)",
  "pub_date": "string (datetime, read-only)",
  "image": "string (file, nullable)",
  "group": "integer (nullable)"
}
```

### Comment(Комментарий)
```json
{
  "id": "integer (read-only)",
  "author": "string (username, read-only)",
  "text": "string (required)",
  "created": "string (datetime, read-only)",
  "post": "integer (read-only)"
}
```

### Group(Сообщество)
```json
{
  "id": "integer (read-only)",
  "title": "string (max 200, required)",
  "slug": "string (max 50, pattern: ^[-a-zA-Z0-9_]+$)",
  "description": "string (required)"
}
```

### Follow(Подписка)
```json
{
  "user": "string (username, read-only)",
  "following": "string (username, required)"
}
```

### Token(JWT)
```json
{
  "refresh": "string",
  "access": "string"
}
```
---
## 📁 Структура проекта
```
yatube_api/
├──postman_collection/            # Тесты Postman
├──tests/                         # Тесты Pytest
├── api/                          # Основное приложение API
│   ├── serializers.py            # Сериализаторы DRF
│   ├── views.py                  # ViewSet'ы и endpoints
│   ├── urls.py                   # Роутинг API
│   ├── permissions.py            # Кастомные права доступа
│   └── tests/                    # Тесты API
├── posts/                        # Приложение постов
│   ├── models.py                 # Модели (Post, Comment, Group, Follow)
│   ├── migrations/               # Миграции БД
│   ── admin.py                   # Админка Django
── yatube_api/                    # Настройки проекта
│   ├── settings.py               # Конфигурация Django
│   ├── urls.py                   # Корневой URLconf
│   └── wsgi.py                   # WSGI config
├── manage.py                     # Django management script
├── requirements.txt              # Зависимости проекта
├── README.md                     # Документация
└── .gitignore                    # Git ignore
```
---
