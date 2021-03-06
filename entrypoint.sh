#!/bin/bash

# Set port (for Heroku compatibility)
if ! [ -z "$PORT" ]; then
    export STREAMLIT_SERVER_PORT=${PORT}
fi

# Enable virtualenv
source venv/bin/activate

# Start server
cd src/
streamlit run app.py
