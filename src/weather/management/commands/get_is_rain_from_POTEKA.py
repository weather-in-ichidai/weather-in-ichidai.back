from django.core.management.base import BaseCommand
import requests
import base64

class Command(BaseCommand):
    def handle(self, *args, **options):
        #POTEKA指定
        #雨検知
        real_url = "http://api.potekanet.com/v1/point/real/ja/poteka"
        real_payload = {"potekaId":"1335","element":"rain"}


        auth_data_b = base64.standard_b64encode('hirosima-cu:Ij2RhBVc'.encode('UTF-8'))
        auth_data = auth_data_b.decode("UTF-8").replace("=","")
        headers = {'X-POTEKA-Authorization':auth_data}

        real_request = requests.get(real_url, params=real_payload,headers=headers)
        print(real_request.text)
