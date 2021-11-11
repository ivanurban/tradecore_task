from celery.decorators import task

import requests
import json
import datetime


#Automatically Retrying Failed Celery Tasks 
#If Celery task needs to send a request to a third-party service,
# using exponential backoff to avoid overwhelming the service.
@task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 5})
def get_location(self):

    """Get the location of the user by users ip"""

    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=ab24d7de15824ba1bccfb014c057e769")
   

    response_json=json.loads(response.content)
    city=response_json.get("city")
    country=response_json.get("country")
    country_code = response_json.get('country_code')
  
    return [city,country,country_code]

@task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 5})
def user_location(self):
    """City and country for the field location when user registers"""
    city, country, code, = get_location()
    return city, country


@task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 5})
def get_local_holiday(self):
    """Look if there is a holiday in the location on the day
    that user is registered"""

    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    city, country, code = get_location()
    
    response = requests.get(f"https://holidays.abstractapi.com/v1/?api_key=b758785aff304d969b59ead5b46b61d3&country={code}&year={year}&month={month}&day={day}")
    
    if not response:
        return "no holiday"
    else:
        response_json=json.loads(response.content)
        holiday = response_json[0]
        return holiday["name"]