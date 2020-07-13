import japronto
from calc_handler import calc_handler


if __name__ == '__main__':
    app = japronto.Application()
    app.router.add_route('/calc', calc_handler, "POST")
    app.run(worker_num=4)
