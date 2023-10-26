import requests
import os


def imei_checker(imei):
    """Checks the IMEI using an API database and returns model number and phone brand
       imei: 15-digit number belonging to any device that uses a cellular data """
    db_url = "https://imeidb.xyz/api/imei/"
    str_imei = str(imei)
    api_token = os.environ.get("api_key")
    header = {"X-Api-Key": api_token,
              "Content-Type": "application/json"}
    try:
        # Try for a successful response
        response = requests.get(db_url+str_imei, headers=header)
        response.raise_for_status()
    except requests.exceptions.HTTPError or requests.exceptions.Timeout:
        # If response comes as an error mark as not available, usually what this means is that the IMEI was wrong
        phone_model = "N/A"
        phone_brand = "N/A"
    else:
        # If try block is successful parse the response into json format and take out required data
        data = response.json()
        phone_model = data["data"]["model"]
        phone_brand = data["data"]["brand"]
    return [phone_model, phone_brand]


