from flask import Flask, render_template

import config.base as conf
from db import db
from web.view import get_form_data

app = Flask(
    __name__,
    template_folder='web/templates',
    static_folder='web/static',
)
app.config['SQLALCHEMY_DATABASE_URI'] = conf.db_dsn
db.init_app(app)


@app.route("/")
def home():
    form_data = get_form_data()
    return render_template(
        'report.html',
        committee_names=form_data[0],
        candidate_names=form_data[1],
    )


# точка сбора и запуска приложения
if __name__ == '__main__':
    app.run()
