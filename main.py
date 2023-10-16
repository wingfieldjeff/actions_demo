import logging
import logging.handlers
import os
import dominate
from dominate.tags import *
import requests
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)




if __name__ == "__main__":
    

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Tampa&country=US')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f'Weather in Tampa: {temperature}C')
        current_datetime = datetime.datetime.now()

        d =dominate.document(title='Github Actions Demo')
        d += h1('Weather in Tampa:')
        d += h2(f'{temperature}C')
        d += p(f'Last Updated: {current_datetime}')

        html_content = d.render()
        with open("index.html", "w") as file:
            file.write(html_content)