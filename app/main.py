import japronto
from handlers import calc_handler, error_handler
from request_error import RequestError


if __name__ == '__main__':
    app = japronto.Application()
    
    app.router.add_route('/calc', calc_handler, "GET")
    app.add_error_handler(RequestError, error_handler)
    
    app.run()
