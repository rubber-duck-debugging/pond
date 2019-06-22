# The Pond
Website for Rubber Duck Debugging Show on Twitch

## Development Install Steps

We are developing the Pond for the RubberDuckDebugging show on TwitchTV with Python 3.7.3, so get that installed! If you are unsure how to do that and just getting started head over to the [pyenv](https://github.com/pyenv/pyenv) project and follow the instructions to install it. It's a super simple way to install and manage your python versions. 

If you know how to create a virtual environment do that! Then install the packages we use via `pip install -r requirements.txt`

## Migrations

**BEFORE DOING ANYTHING** make sure to set `FLASK_APP` to `pond.py` by executing `export FLASK_APP=pond.py`

### In Development
1. Delete everything in migrations/versions
2. Delete app.db
3. `flask db migrate -m "init"`
4. `flask db upgrade`

### In Production
1. Make update to model
2. `flask db migrate -m "init"`
3. Push Code to Github
4. Pull updated code to production from GitHub
4. Run `flask db upgrade` on production
