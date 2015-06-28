def convert(condition, formatters=None):
    mongo_cond = None
    operator = condition[0]

    logical_operators = {
        'and': '$and',
        'or': '$or',
        'nor': '$nor'
    }

    comparing_operators = {
        'neq': '$ne',
        'gt': '$gt',
        'gte': '$gte',
        'lt': '$lt',
        'lte': '$lte',
        'in': '$in',
        'nin': '$nin',
        'regex': '$regex'
    }

    if operator in logical_operators.keys():
        mongo_cond = {logical_operators[operator]: [convert(cond) for cond in condition[1:]]}
    else:
        key, value = condition[1:]

        if formatters and key in formatters.keys():
            value = formatters[key](value)

        if operator in comparing_operators.keys():
            mongo_cond = {key: {comparing_operators[operator]: value}}
        else:
            mongo_cond = {key: value}

    return mongo_cond
