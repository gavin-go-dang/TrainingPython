import requests
import json
import os
 

 

class RateOfCurrency(object):
    
    def __init__(sefl, url):
        sefl.url = url
        sefl.json_by_date = None

    
    def get_data(sefl):
        headers = {'Accept': 'application/json'}

        response = requests.get(sefl.url, headers=headers)
        return response.json()
    
    def create_json_by_date(sefl, path, filename):
        try:
            data = sefl.get_data()['result']['records']
            result_by_day = {}

            for date_info in data:
                date = date_info['end_of_day']
                rate= []
                atribute = list(date_info.keys())    
                atribute.remove('preliminary')
                atribute.remove('timestamp')
                atribute.remove('end_of_day')
                record = {}
                for rate_name in atribute: 
                        record[rate_name] = date_info[rate_name]
                result_by_day[date] = record

                with open('{}/{}'.format(path, filename), "w") as outfile:
                    json.dump(result_by_day, outfile)
            print('Creating Success !!!')
            sefl.json_by_date = '{}/{}'.format(path, filename)
            return 1        
        except:
            print('Creating Fail') 
            return 0

    def get_rate(self, currency_name):
        if not self.json_by_date:
            path = "json"
            dir_list = os.listdir(path)
            print= dir_list
            file_id= 0
            while True:
                filename = 'resultByDayOOP{}'.format(str(file_id))
                if filename not in dir_list:
                    self.create_json_by_date(path, filename)
                    break
                
                else:
                    file_id += 1

        f = open(self.json_by_date)  
        data = json.load(f)
        f.close()
        rate_by_date_dict = {}
        record ={}
        name_mapping_currency = ''
        for date, value in data.items():
            try:
                record[date] = float(value['{}_sgd'.format(currency_name)])
                name_mapping_currency = '{}_sgd'.format(currency_name)
            except:
                record[date] = float(value['{}_sgd_100'.format(currency_name)])
                name_mapping_currency = '{}_sgd_100'.format(currency_name)
        rate_by_date_dict['currency'] = currency_name
        rate_by_date_dict['record'] = record
        
        return rate_by_date_dict

 

url = 'https://eservices.mas.gov.sg/api/action/datastore/search.json?resource_id=95932927-c8bc-4e7a-b484-68a66a24edfe&limit=100&sort=end_of_day%20desc'


sgd = RateOfCurrency(url)
print(sgd.get_rate('vnd'))

