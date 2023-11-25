import requests
from document_creator import config
from flask import jsonify, Response
import json
from datetime import datetime
import base64


def get_info(params):

    url = "{}/info".format(config.property_information_api_url)

    headers = {
        'Content-Type': "application/json",
        }

    resp = requests.request("GET", url, data=json.dumps(params), headers=headers)
    data = json.loads(resp.text)

    return data
    