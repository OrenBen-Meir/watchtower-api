CALL venv/Scripts/activate.bat

set SECRET_KEY=your secret key
set SQL_USERNAME=your sql username
set SQL_PASSWORD=your password
set SQL_SERVER_NAME=your server name
set SQL_DRIVER=your sql driver

set FLASK_APP=run.py
set FLASK_ENV=development
flask %1 %2 %3 %4 %5 %6 %7 %8 %9