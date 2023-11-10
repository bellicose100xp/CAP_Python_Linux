#!/usr/bin/python3
"""API requests without threads | rzfeeser@alta3.com"""

# standard library
from time import time

# python3 -m pip install requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

# a list of apis from https://api.le-systeme-solaire.net/rest/bodies/
url_list = [
    "https://api.le-systeme-solaire.net/rest/bodies/lune",
    "https://api.le-systeme-solaire.net/rest/bodies/phobos",
    "https://api.le-systeme-solaire.net/rest/bodies/deimos",
    "https://api.le-systeme-solaire.net/rest/bodies/europe",
    "https://api.le-systeme-solaire.net/rest/bodies/callisto",
    "https://api.le-systeme-solaire.net/rest/bodies/himalia",
    "https://api.le-systeme-solaire.net/rest/bodies/elara",
    "https://api.le-systeme-solaire.net/rest/bodies/sinope",
    "https://api.le-systeme-solaire.net/rest/bodies/leda",
    "https://api.le-systeme-solaire.net/rest/bodies/thebe",
]


def download_file(url):
    html = requests.get(url, stream=True)
    return html.status_code


# for url in url_list:
#     print(download_file(url))
#
# # display the total run time
# print(f"Time taken: {time() - start}")

start = time()
processes = []

# Opening up a pool of five threads
with ThreadPoolExecutor(max_workers=5) as executor:
    for url in url_list:
        x = executor.submit(download_file, url)
        processes.append(x)

# processes == a list of threads

# Loop over each thread and wait until every thread is done
for task in as_completed(processes):
    print(task.result())

print("You shouldn't see this until all the threads are done")
print(f"time taken: {time() - start}")
