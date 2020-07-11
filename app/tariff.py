import json
import decimal

TARIFF_PATH = 'tariff.json'


class TariffException(Exception):
    pass


class Tariff:
    def __init__(self, path=TARIFF_PATH):
        with open(path) as file:
            self.tariff = json.load(file)
    
    def get_rate(self, date, cargo_type):
        # TODO make better code
        dates = self.tariff.keys()
        last_date = None
        for tariff_date in dates:
            if tariff_date > date:
                break
            last_date = tariff_date
        
        if last_date is None:
            raise TariffException('Please specify a valid date')
        
        for tariff_type in self.tariff[last_date]:
            if tariff_type["cargo_type"] == cargo_type:
                return decimal.Decimal(tariff_type['rate'])
        raise TariffException('Please specify a valid cargo type')
        
