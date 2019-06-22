import os
from flask_migrate import Migrate
from app import createApp, db
from app.models import User, UserClass, Question

app = createApp(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, UserClass=UserClass, Question=Question)
