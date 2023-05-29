import json
import pandas

"""Read saved Json file"""

import json
  
f = open('json/resultByDay.json')
  
data = json.load(f)
  

f.close()

def get_rate(data, currency_name):
    rate_by_date_dict = {}
    record ={}
    for date in list(data.keys()):
        try:
            record[date] = float(data[date][currency_name+'_sgd'])
        except:
            record[date] = float(data[date]['{}_sgd_100'.format(currency_name)])
    rate_by_date_dict['currency'] = currency_name
    rate_by_date_dict['record'] = record
    return rate_by_date_dict

usd_rate = get_rate(data, 'usd')

print(usd_rate)