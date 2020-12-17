import subprocess
def get_weather_from_POTEKA:
    try:
        res = subprocess.call('python ..\manage.py get_weather_from_POTEKA')
    except:
        print "Error."
    print res