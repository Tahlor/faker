import pytest

from faker.ancestry.custom_row import RowBuilder

def test_provider_dict():
    R = RowBuilder(functions=["name", "address"], provider_dict_list=[{"provider": "faker.providers.address", "locale": "es"},
                                                                      {"provider": "faker.providers.person", "locale": "en_US"}
                                                                      ])
    print(R.gen_row())


def test_RowBuilder():
    R = RowBuilder(functions=["name", "address", "relationship", "job", "date"])
    print(R.gen_row())
