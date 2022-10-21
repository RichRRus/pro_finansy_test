# PRO FINANCY тестовое

## Структура проекта

Основа проекта лежит в директории [app](./app)

## Запуск с помощью docker-compose

```bash
$ docker-compose up -d --build
```

_N.B_: Все переменные окружение хранятся в файле [.env](.env).
После запуска докера будет создана директория [postgres_data](./postgres_data), которая прокидывается из докера
по средством volume.

## Админка и документация

После запуска проекта админка будет доступна по адресу [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
Документация доступна на [http://127.0.0.1:8000/api/swagger](http://127.0.0.1:8000/api/swagger)