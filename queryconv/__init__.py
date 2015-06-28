from .converters import mongodb
from .exceptions import QueryConverterTypeError


__all__ = ['convert']


def convert(query_type, condition, formatters=None):
    if query_type == 'mongodb':
        return mongodb.convert(condition, formatters)

    raise QueryConverterTypeError
