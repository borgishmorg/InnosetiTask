import japronto
import tariff
import decimal

t = tariff.Tariff()

def calc_handler(request):
    try:
        params = request.json if request.json is not None else dict()
    except SystemError:
        return request.Response(json={'error': 'Please specify a valid body'})
        
    try:
        date = params['date']
        cargo_type = params['cargo_type']
        declared_price = decimal.Decimal(params['declared_price'])
    except KeyError as e:
        return request.Response(json={'error': f'Please specify a {e}'})
    
    cost = declared_price * t.get_rate(date, cargo_type)
    cost = cost.quantize(decimal.Decimal('1'), rounding=decimal.ROUND_UP)
    return request.Response(json={'price': cost.__str__()})
    

def error_handler(request, exception):
    return request.Response(json={'error': exception.__str__()})


if __name__ == '__main__':
    app = japronto.Application()
    app.router.add_route('/calc', calc_handler, "GET")
    app.add_error_handler(tariff.TariffException, error_handler)
    app.run()
