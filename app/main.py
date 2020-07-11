import japronto

def calc_handler(request):
    return request.Response(json={'info':'Hello'})


if __name__ == '__main__':
    app = japronto.Application()
    app.router.add_route('/calc', calc_handler, "GET")
    app.run()
