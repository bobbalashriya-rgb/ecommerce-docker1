"""
Application entry point
"""
from . import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='54.90.101.233', port=5000, debug=True)
