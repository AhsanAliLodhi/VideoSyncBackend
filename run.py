import os
import config
from app.app import vs_app

if __name__ == '__main__':
    vs_app.run(
        host='0.0.0.0',
        port=int(os.getenv('FLASK_PORT')),
        debug=os.getenv('FLASK_DEBUG')
    )
