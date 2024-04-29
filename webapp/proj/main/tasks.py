import requests as r
import uuid
from celery import shared_task
from django.conf import settings


CAT_URL = 'https://cataas.com/cat'

@shared_task
def download_a_cat():
    resp = r.get(CAT_URL)
    file_ext = resp.headers.get('Content-Type').split('/')[1]
    file_name = settings.BASE_DIR / 'cats' / (str(uuid.uuid4()) + '.' + file_ext)
    with open(file_name, 'wb') as file:
        for chunk in resp.iter_content(chunk_size=128):
            file.write(chunk)

    return
