#!/bin/bash

if [ "$(uname)" == "Darwin" ]; then
  echo "using a mac"
  source venv/bin/activate
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  echo "using linux"
  source venv/bin/activate
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  echo "using windows 32-bit"
  source ./venv/Scripts/activate
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
  echo "using windows 64-bit"
  source ./venv/Scripts/activate
else
  echo "OS Uknown, exiting ..."
  exit 1
fi

# your environment variables to edit
export AES_KEY="your aes key (has to be 16, 24, or 32 characters long)"

export SQL_USERNAME="your sql username"
export SQL_PASSWORD="your sql password"
export SQL_SERVER_NAME="your sql server name"
export SQL_DRIVER="your sql driver"

export FIREBASE_API_KEY="Your API Key"
export FIREBASE_AUTH_DOMAIN="YourprojectId.firebaseapp.com"
export FIREBASE_DATABASE_URL="https://YourdatabaseName.firebaseio.com"
export FIREBASE_PROJECT_ID="your firebase project ID"
export FIREBASE_STORAGE_BUCKET="YourprojectId.appspot.com"
export FIREBASE_MESSAGING_SENDER_ID="your firebase messaging sender Id"
export FIREBASE_APP_ID="your firebase app Id"
export FIREBASE_MEASUREMENT_ID="your firebase messaging senser id"

# to set up flask
export FLASK_ENV=development
export FLASK_APP=run.py

# run flask
flask "$@"