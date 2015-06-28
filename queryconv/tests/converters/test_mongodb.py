import pytest
import logging
from queryconv.converters.mongodb import convert

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture
def _test_cases():
    cases = [
        (('eq', 'key', 'value'), {'key': 'value'}),
        (('neq', 'key', 'value'), {'key': {'$ne': 'value'}}),
        (('gt', 'key', 'value'), {'key': {'$gt': 'value'}}),
        (('gte', 'key', 'value'), {'key': {'$gte': 'value'}}),
        (('lt', 'key', 'value'), {'key': {'$lt': 'value'}}),
        (('lte', 'key', 'value'), {'key': {'$lte': 'value'}}),
        (('in', 'key', ['value1', 'value2']), {'key': {'$in': ['value1', 'value2']}}),
        (('nin', 'key', ['value1', 'value2']), {'key': {'$nin': ['value1', 'value2']}}),
        (('regex', 'key', r'^value.*'), {'key': {'$regex': r'^value.*'}}),
    ]

    for operator in [('and', '$and'), ('or', '$or'), ('nor', '$nor')]:
        cases.append(
            (
                (
                    operator[0],
                    ('eq', 'key', 'value'),
                    ('neq', 'key2', 'value2'),
                    ('gt', 'key3', 'value3')
                ),
                {
                    operator[1]: [
                        {'key': 'value'},
                        {'key2': {'$ne': 'value2'}},
                        {'key3': {'$gt': 'value3'}}
                    ]
                }
            )
        )

    cases.append(
        (
            (
                'and',
                ('eq', 'k', 'v'),
                ('neq', 'k2', 'v2'),
                (
                    'or',
                    ('gt', 'k2', 'v2'),
                    ('eq', 'k3', 'v3'),
                ),
            ),
            {
                '$and': [
                    {'k': 'v'},
                    {'k2': {'$ne': 'v2'}},
                    {'$or': [
                        {'k2': {'$gt': 'v2'}},
                        {'k3': 'v3'}
                    ]}
                ]
            }
        )
    )

    return cases


def test_transform(_test_cases):
    # logging.debug('')
    for condition, expected_query in _test_cases:
        # logging.debug(' {} ==> {}'.format(condition, expected_query))
        assert convert(condition) == expected_query


def test_transform_with_formatters():
    formatters = {'key': bool}
    condition = ('eq', 'key', 'value')
    expected = {'key': True}
    assert convert(condition, formatters=formatters) == expected
