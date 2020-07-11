TESTS = [
    {
        'label': 'connect test'
    },
    {
        'label': 'date is not specified test',
        'key': 'error',
        'value': 'Please specify a \'date\''
    },
    {
        'label': 'cargo_type is not specified test',
        'json': {
            'date': '2020-07-01'
        },
        'key': 'error',
        'value': 'Please specify a \'cargo_type\''
    },
    {
        'label': 'declared_price is not specified test',
        'json': {
            'date': '2020-07-01',
            'cargo_type': 'Glass'
        },
        'key': 'error',
        'value': 'Please specify a \'declared_price\''
    },
    {
        'label': '2020-07-01 Glass 1000 test',
        'json': {
            'date': '2020-07-01',
            'cargo_type': 'Glass',
            'declared_price': '1000'
        },
        'key': 'price',
        'value': '35'
    }
]