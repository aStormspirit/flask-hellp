# flask-hellp
Простое приложение на Flask, упакованное в Docker

![Image alt](https://github.com/aStormspirit/flask-hellp/raw/main/image/picture.png)

Сборка приложение командой:
docker build -t myapp .

Запуск приложения:

docker run -d -p 777:5000 myapp

приложение запускается на порту 777, можно увидеть в браузере по адресу 
http://localhost:777
