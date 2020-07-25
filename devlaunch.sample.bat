CALL venv/Scripts/activate.bat

REM your env variables
set SECRET_KEY=your secret key
set SQL_USERNAME=your sql username
set SQL_PASSWORD=your password
set SQL_SERVER_NAME=your server name
set SQL_DRIVER=your sql driver

REM to set up flask
set FLASK_APP=run.py
set FLASK_ENV=development

flask  %*