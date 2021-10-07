

import requests
from odoo import models, fields


class HotelApi(models.Model):
    _name = 'hotels.api'
    _description = 'Hotel api'

    url = "https://hotels4.p.rapidapi.com/locations/search"

    querystring = {"query":"new york","locale":"en_US"}

    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "6731843bfdmsh57505fdfed7cb23p172d89jsn7b9ade02f26b"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    hotel_name = fields.Char(string="Hotels name", default=response.json()['term'])