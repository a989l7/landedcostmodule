#!/bin/bash
echo "Starting Flask app..."
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

