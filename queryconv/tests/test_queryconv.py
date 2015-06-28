import pytest
import queryconv
from unittest.mock import MagicMock


def test_convert_type_error():
    with pytest.raises(queryconv.exceptions.QueryConverterTypeError):
        queryconv.convert('non_type', ())


def test_convert_is_callable_with_mongodb_type(monkeypatch):
    monkeypatch.setattr('queryconv.converters.mongodb.convert', MagicMock(return_value=True))
    assert queryconv.convert('mongodb', ()) is True
