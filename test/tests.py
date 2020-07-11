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
        'label': '2020-06-01 Glass 1000 test',
        'json': {
            'date': '2020-06-01',
            'cargo_type': 'Glass',
            'declared_price': '1000'
        },
        'key': 'price',
        'value': '40'
    },
    {
        'label': '2020-06-01 Other 1000 test',
        'json': {
            'date': '2020-06-01',
            'cargo_type': 'Other',
            'declared_price': '1000'
        },
        'key': 'price',
        'value': '10'
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
    },
    {
        'label': '2020-06-30 Other 1000 test',
        'json': {
            'date': '2020-06-30',
            'cargo_type': 'Other',
            'declared_price': '1000'
        },
        'key': 'price',
        'value': '10'
    },
    {
        'label': '2020-07-01 Glass 68923 test',
        'json': {
            'date': '2020-07-01',
            'cargo_type': 'Glass',
            'declared_price': '68923'
        },
        'key': 'price',
        'value': '2413'
    }
]