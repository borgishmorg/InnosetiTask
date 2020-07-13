import request_handler
import decimal
import tariff
import logger

t = tariff.Tariff()


def calc_handler(request):
    try:
        r = request_handler.RequestHandler(request)
        
        cost = r.declared_price * t.get_rate(r.date, r.cargo_type)
        cost = cost.quantize(decimal.Decimal('1'), rounding=decimal.ROUND_UP)
    except request_handler.RequestError as e:
        response = {'error': e.__str__()}
        logger.Logger().log(request=e.request, response=response)
    except tariff.TariffError as e:
        response = {'error': e.__str__()}
        logger.Logger().log(request=r.params, response=response)
    else:
        response = {'price': cost.__str__()}
        logger.Logger().log(request=r.params, response=response)
        
    return request.Response(json=response)
