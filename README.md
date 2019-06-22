# pond
Website for Rubber Duck Debugging Show on Twitch

# Migrations
**bold**
*italic*
-strikthrough-

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

```
flask run
```