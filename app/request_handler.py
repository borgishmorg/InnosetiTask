import decimal
import datetime
from request_error import RequestError


class RequestHandler:
    def __init__(self, request):
        try:
            params = request.json if request.json is not None else dict()
        except SystemError:
            raise RequestError('Please specify a valid body')
            
        try:
            self.date = datetime.date.fromisoformat(params['date'])
            self.cargo_type = params['cargo_type']
            self.declared_price = decimal.Decimal(params['declared_price'])
        except KeyError as e:
            raise RequestError(f'Please specify a {e}')
        except ValueError:
            raise RequestError('Please specify a valid date')