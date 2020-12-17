from django.core.management.base import BaseCommand
import requests
import base64

class Command(BaseCommand):
    def handle(self, *args, **options):
        #POTEKA指定
        #予測
        forecast_url = "http://api.potekanet.com/v1/point/forecast/ja/poteka"
        forecast_payload = {"potekaId":"1335","element":"temp,pop,weather","dataPeriod":"36","interval":"1"}
        #雨検知
        real_url = "http://api.potekanet.com/v1/point/real/ja/poteka"
        real_payload = {"potekaId":"1335","element":"rain"}

        #矩形指定
        """
        url = "http://api.potekanet.com/v1/area/forecast/ja/rectangle"
        payload = {"swPoint":"34.437090,132.411448","nePoint":"34.441312,132.421832","element":"temp"}
        """

        auth_data_b = base64.standard_b64encode('hirosima-cu:Ij2RhBVc'.encode('UTF-8'))
        auth_data = auth_data_b.decode("UTF-8").replace("=","")
        headers = {'X-POTEKA-Authorization':auth_data}

        real_request = requests.get(real_url, params=real_payload,headers=headers)
        forecast_request = requests.get(forecast_url, params=forecast_payload,headers=headers)

        print(real_request.text)
        print(forecast_request.text)
