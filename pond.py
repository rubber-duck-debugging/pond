import os
from flask_migrate import Migrate, upgrade
from app import createApp, db

app = createApp(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
