import decimal
import datetime


class RequestError(Exception):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request


class RequestHandler:
    def __init__(self, request):
        try:
            self.params = request.json
        except SystemError:
            raise RequestError(request.body, 'Please specify a valid body')
            
        try:
            try:
                self.date = datetime.date.fromisoformat(self.params['date'])
            except (TypeError, ValueError):
                raise RequestError(self.params, 'Please specify a valid date')
            self.cargo_type = self.params['cargo_type'].__str__()
            try:
                self.declared_price = decimal.Decimal(self.params['declared_price'])
            except (decimal.InvalidOperation, TypeError):
                raise RequestError(self.params, 'Please specify a valid declared_price')
        except KeyError as e:
            raise RequestError(self.params, f'Please specify a {e}')
        
        