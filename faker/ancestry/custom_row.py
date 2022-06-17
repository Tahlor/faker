"""
# Eventually:
Create random text provider
Need a random formatter
"""

import faker
from faker import Faker
from faker import providers
from collections.abc import Sequence
from typing import List, Dict

fake = Faker()


class RowBuilder():
    def __init__(self, functions, provider_dict: List[Dict]=None):
        """
        R = RowBuilder(functions=["name", "address"], provider_dict=[{"provider":"faker.providers.address", "locale":"es"},
                                                                     {"provider":"faker.providers.name", "locale":"en_US"}
                                                                    ])
        Args:
            functions
            provider_dict [{provider, locale, options}]
        """
        if provider_dict:
            locales = []
            provider_names = []
            for provider_arg in provider_dict:
                if "locale" in provider_arg:
                    locales.append(provider_arg["locale"])
                else:
                    locales.append(None)
                provider_names.append(provider_arg["provider"])

            # Example
            # self.generator = Faker(["en_US", "es"],["faker.providers.address", "faker.providers.person"])
            self.generator = Faker(locales,provider_names)

        else:
            self.generator = Faker()
        self.functions = [getattr(self.generator, func) for func in functions]

    def gen_row(self):
        return [func() for func in self.functions]


