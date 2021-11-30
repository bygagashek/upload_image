# upload_image


Установка необходимых зависимостей:
pip install -r requirement.txt

Конечные точки API:

POST /auth/register/
POST /auth/login/
GET /auth/current-user/
POST /auth/logout/
POST /auth/refresh-token/
POST /upload/

Использование.
Скачать репозиторий. Установить необходимые зависимости(рекомендую устанавливать из requirement.txt, т.к. существуют проблемы совместимости
версий некоторых библиотек)Провести миграции бд. Запустить сервер разработки.
Пройти регистрацию /auth/register/, пример:
Тело запроса:
{
  "username": "user1",
  "password": "testproject123",
  "confirm_password": "testproject123",
  "email": "user1@user.user",
  "first_name": "qwe",
  "last_name": "zxc"
}
Войти в созданную учетную запись /auth/login/ для получений access и refresh токенов JWT.
Пример:
{
  "username":"user1",
  "email":"user1@user.user",
  "password": "testproject123"
}
Для отправки изображения на сервер /upload/.В вкладке авторизации выбрать Bearer token, и ввести полученный вами токен.
В теле запроса,для содержимого формы выбрать form-data, изменить text на file, как ключь использовать picture,и выбрать необходимое изображение.

Загружает изображения не более 200 кБ и присваивает каждому уникальное имя.
