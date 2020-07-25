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
export SECRET_KEY="your secret key"
export SQL_USERNAME="your sql username"
export SQL_PASSWORD="your sql password"
export SQL_SERVER_NAME="your sql server name"
export SQL_DRIVER="your sql driver"

# to set up flask
export FLASK_ENV=development
export FLASK_APP=run.py

flask "$@"