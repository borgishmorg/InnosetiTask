import json
import decimal
import datetime

TARIFF_PATH = 'tariff.json'


class TariffException(Exception):
    pass


class Tariff:
    def __init__(self, path=TARIFF_PATH):
        with open(path) as file:
            tariff_data = json.load(file)
        self.tariff = dict()
        
        for date_string, subtariffs in tariff_data.items():
            date = datetime.date.fromisoformat(date_string)
            self.tariff[date] = dict()
            
            for subtariff in subtariffs:
                cargo_type = subtariff['cargo_type']
                rate = subtariff['rate']
                self.tariff[date][cargo_type] = decimal.Decimal(rate)
        
    
    def get_rate(self, date: datetime.date, cargo_type: str) -> decimal.Decimal:
        dates = self.tariff.keys()
        tariff_date = None
        for d in dates:
            if d > date:
                break
            tariff_date = d
        
        if tariff_date is None:
            raise TariffException('Please specify a valid date')
        
        try:
            return self.tariff[tariff_date][cargo_type]
        except KeyError:
            raise TariffException('Please specify a valid cargo type')
        
