import os
import config
from app.app import audi_app

if __name__ == '__main__':
    audi_app.run(
        host='0.0.0.0',
        port=int(os.getenv('FLASK_PORT')),
        debug=os.getenv('FLASK_DEBUG')
    )
