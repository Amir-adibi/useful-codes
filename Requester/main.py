import random
import threading
from urllib.parse import quote

import requests

import logging


def get_shot(url: str):
    url_parse = url.split("/")
    res = requests.post((f"http://127.0.0.1:8000/screenshot?link={quote(url)}"))
    if res.status_code != 200:
        logging.debug("response is: %s", res.content)
        return None
    with open(str(url_parse[-1]) + ".jpeg", "wb") as fp:
        fp.write(res.content)

threads = []
links = [
    "https://t.me/cvision/3013",
    "https://t.me/whitesquare18/383",
    "https://t.me/c/1466419661/3695",
    "https://t.me/saipa_goodarzi/2022",
    "https://t.me/SAJAD_JOEY/2240",
    "https://t.me/azarijahromi/783"
]


for link in links:
    p = threading.Thread(target=get_shot, args=[link])
    threads.append(p)
    p.start()

for thread in threads:
    thread.join()