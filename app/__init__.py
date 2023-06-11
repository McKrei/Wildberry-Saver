# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__, static_folder='static')
# app.config.from_object('config.Config')

# db = SQLAlchemy(app)

# from . import models, views  # noqa

# db.create_all()



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import threading
import schedule
import time

app = Flask(__name__, static_folder='static')
app.config.from_object('config.Config')

db = SQLAlchemy(app)

from . import models, views, parsing  # noqa

db.create_all()

# Запускаем отдельный поток для планировщика
# scheduler_thread = threading.Thread(target=parsing.start_parsing)
# scheduler_thread.start()
