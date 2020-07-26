from main.application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config['FLASK_ENV'] == 'development')
else:
    application = app
