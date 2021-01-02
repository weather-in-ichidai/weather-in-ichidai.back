from django.core.management.base import BaseCommand
import requests
import base64
from .POTEKA_token import poteka_auth
from ...models import Past_weather_data
import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--date', nargs='?', default='', type=str)

    def handle(self, *args, **options):
        request_date = datetime.datetime.strptime(options["date"],"%Y-%m-%d")
        request_start_datetime = request_date.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
        request_end_datetime = request_start_datetime + datetime.timedelta(days=1)

        #POTEKA指定
        #予測
        url = "http://api.potekanet.com/v1/point/real/ja/poteka"
        payload = {"potekaId":"1335","element":"temp,humi,weather","startDate":request_start_datetime.isoformat(),"endDate":request_end_datetime.isoformat()}
        print(payload)
        headers = {'X-POTEKA-Authorization':poteka_auth}
        request = requests.get(url, params=payload,headers=headers)

        try:
            request.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("error :",e)
        else:
            res = request.json()
            temp_array = []
            humi_array = []

            for x in res["poteka"][0]["element"][0]["dataList"]:
                temp_array.append(str(x["value"]))

            for x in res["poteka"][0]["element"][1]["dataList"]:
                humi_array.append(int(x["value"]))

            data = Past_weather_data()
            data.date = request_start_datetime.date()
            data.temp = ",".join(temp_array)
            data.humi = sum(humi_array)/len(humi_array)
            data.weather = res["poteka"][0]["element"][2]["dataList"][0]["value"]
            data.save()

            print("cleate data")
