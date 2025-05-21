import sys
import logging
import os
from aiohttp.web import run_app

from sqli.app import init as init_app

log = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(sys.argv[1:])

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    log.info(f'App is listening at http://{host}:{port}')
    run_app(app, host=host, port=port)
