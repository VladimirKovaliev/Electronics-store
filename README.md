# Electronics Store
Онлайн платформа торговой сети и электроники

## Стэки:
1. python
2. postgresql
3. django
4. DRF

# Проект в себя включает:
- Создание и настройка пользователей
- Распределение ролей между пользователями
- CRUD для продуктов и поставщиков
- swagger

## Для запуска проекта необходимо:

1. Клонируйте репозиторий
```bash
  git glone git@github.com:VladimirKovaliev/Electronics-store.git
```
2. Активируйте в нём виртуальное оружение, установите зависимости
```bash
  python source/bin/activate
```
```bash
  python -m pip install -r requirements.txt 
```
3. Создайте .env файл в корневой директории проекта и заполните следующие переменные:
```bash
SECRET_KEY=
TIME_ZONE=
DEBUG=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```

5. Выполните миграции
```bash
  python manage.py migrate
```
(если происходит ошибка, то пропишите 
'chmod u+rwx manage.py' и попробуйте выполнить миграции снова)
5. Запустите проект
```bash
    python manage.py runserver
```

## Для создания суперпользователя:
```bash
  python3 manage.py csu
```
- email: admintest@mail.ru
- password: qwerty7586
