Шаги чтобы запустить:

1. Создать файл .env на основе .env.example
   1. PORT - порт, на котором будет запущен сервер
   2. DEBUG - лучше оставить True
   3. DB_USER - пользователь в базе данных
   4. DB_PASSWORD - пароль этого пользователя
   5. DB_HOST - хост, где расположена БД (локально - localhost)
   6. DB_PORT - порт, на котором расположена БД (обычно 5432)
   7. DB_NAME - название базы данных
2. Выполнить команду pip install -r requirements.txt
3. Выполнить команду python main.py