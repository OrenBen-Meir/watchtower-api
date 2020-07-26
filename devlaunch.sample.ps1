# for windows powershell users

& .\venv\Scripts\activate.ps1

# your env variables
$Env:AES_KEY="your aes key (has to be 16, 24, or 32 characters long)"

$Env:SQL_USERNAME="your sql username"
$Env:SQL_PASSWORD="your password"
$Env:SQL_SERVER_NAME="your server name"
$Env:SQL_DRIVER="your sql driver"

$Env:FIREBASE_API_KEY="Your API Key"
$Env:FIREBASE_AUTH_DOMAIN="YourprojectId.firebaseapp.com"
$Env:FIREBASE_DATABASE_URL="https://YourdatabaseName.firebaseio.com"
$Env:FIREBASE_PROJECT_ID="your firebase project ID"
$Env:FIREBASE_STORAGE_BUCKET="YourprojectId.appspot.com"
$Env:FIREBASE_MESSAGING_SENDER_ID="your firebase messaging sender Id"
$Env:FIREBASE_APP_ID="your firebase app Id"
$Env:FIREBASE_MEASUREMENT_ID="your firebase messaging senser id"

# to set up flask
$Env:FLASK_APP="run.py"
$Env:FLASK_ENV="development"

# run flask
flask $args