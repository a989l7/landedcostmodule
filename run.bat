@echo off
echo Starting Flask app...
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
pause

