# Electronics Network - Торговая сеть электроники

## Описание проекта

Этот проект представляет собой онлайн-платформу торговой сети электроники, разработанную с использованием Django и Django REST Framework (DRF). Платформа предоставляет API для управления данными сети, а также административную панель для удобного администрирования.

## Функциональность

*   **Модели данных:**
    *   `Factory`: Производитель электроники.
    *   `RetailNetwork`: Розничная сеть.
    *   `IndividualEntrepreneur`: Индивидуальный предприниматель, занимающийся продажей электроники.
    *   `Product`: Электронный продукт.
*   **API (Django REST Framework):**
    *   CRUD-операции для моделей `Factory`, `RetailNetwork` и `IndividualEntrepreneur`.
    *   Фильтрация объектов сети по стране и городу.
    *   Аутентификация и права доступа: Доступ к API разрешен только для активных сотрудников.
    *   Запрет на обновление поля "Задолженность" через API.
*   **Административная панель (Django Admin):**
    *   Управление моделями данных.
    *   Фильтр по названию города для объектов сети.
    *   Admin action для очистки задолженности перед поставщиком у выбранных объектов.
    *   Отображение кликабельной ссылки на поставщика (предыдущий уровень иерархии) для объектов сети.

## Технологии

*   Python
*   Django
*   Django REST Framework (DRF)
*   PostgreSQL (или другая поддерживаемая Django база данных)
*   pip

## Установка

1.  Клонируйте репозиторий:
    ```bash
    git clone <your_repository_url>
    ```
2.  Перейдите в директорию проекта:
    ```bash
    cd electronics_network
    ```
3.  Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate.bat  # Windows
    ```
4.  Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
5.  Настройте базу данных PostgreSQL:
    *   Создайте базу данных.
    *   Укажите параметры подключения в файле `electronics_network/settings.py`.
6.  Примените миграции:
    ```bash
    python manage.py makemigrations network
    python manage.py migrate
    ```
7.  Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```
8.  Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## Использование

*   **Административная панель:** Откройте в браузере `http://127.0.0.1:8000/admin/` и войдите, используя учетные данные суперпользователя.
*   **API:** Используйте API, отправляя запросы на соответствующие URL-адреса (например, `/api/factories/`, `/api/retailnetworks/`, `/api/entrepreneurs/`).  Подробную информацию об API можно получить, используя инструмент, такой как Swagger или OpenAPI (если документация была сгенерирована).

