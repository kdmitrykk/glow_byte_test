## О сервисе
Hotelservice - микросервис для бронирования отелей. Реализованы операции добавления бронирования, а также их отмена.
Цена проживания за всё время бронирования и система лояльностей высчитываются автоматически.
Отели можно создавать только через админ-зону.

## Эндпоинты

- `POST /hotelservice/api/v1/reservations` - Создать бронирование
- `DELETE /hotelservice/api/v1/reservations/{{reservationUid}}` - Удалить бронирование

## Примеры запросов

> Бронирование.

**Request:**
```POST /hotelservice/api/v1/reservations/
Content-Type: application/json
X-User-Name: {{username}}


json
{
    "hotelUid": "7951c718-18be-4039-8635-d3252b8ef5b6",
    "startDate": "2025-10-08",
    "endDate": "2027-10-22"
}
```
Бронирование не будет создано, если:

1. Дата начала бронирования указана позже, чем дата конца.
2. Дата начала бронирования в прошлом.
3. Отеля с указанным HotelUid не существует.
4. Поле X-User-Name пустое.

> Отмена бронирования.

**Request:**
```DELETE /hotelservice/api/v1/reservations/{{reservationUid}}/
Content-Type: application/json
X-User-Name: {{username}}
```

Бронирование удалится, если:

1. Оно уже не имеет статус CANCELED.
2. Оно было сделано тем же пользователем, что и X-User-Name.
3. Если бронирование вообще было изначально и удовлетворяет всем остальным условиям.
4. Поле X-User-Name не пустое.


## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/kdmitrykk/glow_byte_test
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd api_yamdb
    ```

3. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv env
    ```

    ```bash
    .\env\Scripts\activate  # Windows
    source env/bin/activate  # macOS и Linux
    ```

4. Обновите pip:
    ```bash
    python -m pip install --upgrade pip
    ```

5. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

6. Выполните миграции базы данных:
    ```sh
    python manage.py migrate
    ```

7. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

## Стек используемых технологий

* Python 3.9
* Django
* Django Rest Framework
* SQLite

## Автор
Крикунов Дмитрий
