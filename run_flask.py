import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
