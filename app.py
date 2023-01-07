from flask import Flask

import config.base as conf
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = conf.db_dsn
db.init_app(app)

# точка сбора и запуска приложения
if __name__ == '__main__':
    app.run()
