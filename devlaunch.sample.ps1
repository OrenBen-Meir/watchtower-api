# for windows powershell users

& .\venv\Scripts\activate.ps1

# your env variables
$Env:SECRET_KEY="your secret key"
$Env:SQL_USERNAME="your sql username"
$Env:SQL_PASSWORD="your password"
$Env:SQL_SERVER_NAME="your server name"
$Env:SQL_DRIVER="your sql driver"

# to set up flask
$Env:FLASK_APP="run.py"
$Env:FLASK_ENV="development"

flask $argumentList