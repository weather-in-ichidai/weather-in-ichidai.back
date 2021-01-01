from django.core.management.base import BaseCommand
import requests
import base64
from .POTEKA_token import poteka_auth
from ...models import Weather_data

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

        
        headers = {'X-POTEKA-Authorization':poteka_auth}

        real_request = requests.get(real_url, params=real_payload,headers=headers)
        forecast_request = requests.get(forecast_url, params=forecast_payload,headers=headers)

        #通信が成功したかの判定
        try:
            real_request.raise_for_status()
            forecast_request.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("error :",e)
        else:
            real_res = real_request.json()
            forecast_res = forecast_request.json()
            temp_array = []
        
            #温度の予測値を24時間後まで配列に格納
            for x in forecast_res["poteka"][0]["element"][0]["dataList"][0:24]:
                temp_array.append(str(x["value"]))

            #雨が降って無ければ0
            now_rain = 1
            if real_res["poteka"][0]["element"][0]["dataList"][0]["value"] == "false":
                now_rain = 0 

            #データの保存
            data = Weather_data()
            data.date_time = real_res["poteka"][0]["element"][0]["dataList"][0]["datatime"]
            data.temp = ",".join(temp_array)
            data.pop = forecast_res["poteka"][0]["element"][1]["dataList"][0]["value"]
            data.weather = forecast_res["poteka"][0]["element"][2]["dataList"][0]["value"]
            data.now_rain = now_rain
            data.save()

            print("cleate data")
