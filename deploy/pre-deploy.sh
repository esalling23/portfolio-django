#!/bin/bash +e

echo "Installing packages..."
cd frontend && rm -rf node_modules package-lock.json && npm install

echo "Building app..." 
npm run build

echo "Collecting static files..."
cd ../
pipenv shell "pipenv install && python manage.py collectstatic && exit"