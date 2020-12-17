from django.core.management.base import BaseCommand
import requests
import base64
from  .POTEKA_token import poteka_auth

class Command(BaseCommand):
    def handle(self, *args, **options):
        #POTEKA指定
        #雨検知
        real_url = "http://api.potekanet.com/v1/point/real/ja/poteka"
        real_payload = {"potekaId":"1335","element":"rain"}

        headers = {'X-POTEKA-Authorization':poteka_auth}

        real_request = requests.get(real_url, params=real_payload,headers=headers)
        print(real_request.text)
