#!/bin/sh
# Install or update libraries before launching the bot
pip install --no-cache-dir -r /app/requirements.txt
exec python /app/main.py