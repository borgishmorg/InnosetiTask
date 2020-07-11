import request_handler
import decimal
import tariff


t = tariff.Tariff()


def calc_handler(request):
    r = request_handler.RequestHandler(request)
    
    cost = r.declared_price * t.get_rate(r.date, r.cargo_type)
    cost = cost.quantize(decimal.Decimal('1'), rounding=decimal.ROUND_UP)
    
    return request.Response(json={'price': cost.__str__()})


def error_handler(request, exception):
    return request.Response(json={'error': exception.__str__()})
