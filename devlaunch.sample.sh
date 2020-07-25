source venv/bin/activate

# set environment variables
export SECRET_KEY="your secret key"
export SQL_USERNAME="your sql username"
export SQL_PASSWORD="your sql password"
export SQL_SERVER_NAME="your sql server na,e"
export SQL_DRIVER="your sql driver"

# run app
export FLASK_ENV=development
export FLASK_APP=run.py
flask $1 $2 $3 $4 $5 $6 $7 $8 $9  