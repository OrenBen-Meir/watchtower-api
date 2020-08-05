CALL venv/Scripts/activate.bat

REM your env variables
set AES_KEY=a 64 digit hex number

set SQL_USERNAME=your sql username
set SQL_PASSWORD=your password
set SQL_SERVER_NAME=your server name
set SQL_DRIVER=your sql driver

set FIREBASE_API_KEY=Your API Key
set FIREBASE_AUTH_DOMAIN=YourprojectId.firebaseapp.com
set FIREBASE_DATABASE_URL=https://YourdatabaseName.firebaseio.com
set FIREBASE_PROJECT_ID=your firebase project ID
set FIREBASE_STORAGE_BUCKET=YourprojectId.appspot.com
set FIREBASE_MESSAGING_SENDER_ID=your firebase messaging sender Id
set FIREBASE_APP_ID=your firebase app Id
set FIREBASE_MEASUREMENT_ID=your firebase messaging senser id

REM to set up flask
set FLASK_APP=run.py
set FLASK_ENV=development

flask  %*