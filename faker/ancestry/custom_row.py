"""
# TO DO :
Create random text provider
Need a random formatter

#


"""

import faker
from faker import Faker
from faker import providers
from collections.abc import Sequence
from typing import List, Dict

#fake = Faker()

def mark_for_replacement(func, char):
    def modded_func(*args, **kwargs):
        return func(*args, **kwargs) + char
    return modded_func

class RowBuilder():
    def __init__(self, functions,
                 provider_dict_list: List[Dict]=None,
                 mark_for_replacement_fields=[],
                 replacement_char=None):
        """

        Args:
            functions:
            provider_dict_list:
            mark_for_replacement_fields:
            replacement_char:


        R = RowBuilder(
        functions=["name", "address", "weight"], provider_dict_list=[
            {"provider": "faker.providers.address", "locale": "fr_FR"},
            {"provider": "faker.providers.person", "locale": "en_US"},
            {"provider": "faker.providers.weight", "locale": "en_US", "config":{"person_type":"adult"}}
        ])
        ### WARNING!!!: All the configs get combined into one dictionary, make sure there are no shared keywords!

        # Generator example
            self.generator = Faker(["en_US", "es"],["faker.providers.address", "faker.providers.person"])

        Args:
            functions
            provider_dict [{provider, locale, options}]
        """
        if provider_dict_list:
            locales = []
            provider_names = []
            config = {}
            for provider_dict in provider_dict_list:
                locales += [provider_dict["locale"]] if "locale" in provider_dict else [None]
                if "config" in provider_dict:
                    config.update(provider_dict["config"])
                provider_names.append(provider_dict["provider"])

            self.generator = Faker(locales,provider_names)
            self.fallback = Faker()

        else:
            self.generator = Faker()
            self.fallback = None
        self.function_names = functions
        self.function_dict = {}

        for name in self.function_names:
            args=None
            # function can be a string or a dict with a value of {**kwargs}
            if isinstance(name,dict):
                args = next(iter(name.values()))
                name = next(iter(name.keys()))
            try:
                self.function_dict[name] = {"func":getattr(self.generator, name), "args":args}
            except Exception as e:
                if self.fallback:
                    self.function_dict[name] = {"func": getattr(self.fallback, name), "args": args}
                else:
                    raise e
            if name in mark_for_replacement_fields and not replacement_char is None:
                self.function_dict[name]["func"] = mark_for_replacement(self.function_dict[name]["func"], char=replacement_char)

    def gen_row(self):
        """ Just return the func + args for each function specified in RowBuilder

        Returns:

        """
        out = []
        for name,func_dict in self.function_dict.items():
            func = func_dict["func"]
            args = func_dict["args"]
            out.append(func(**args) if not args is None else func())
        return out

if __name__=='__main__':
    # R = RowBuilder(functions=["name", "address", "relationship", "job", "date", "height"])
    # print([R.gen_row() for x in range(0,16)])

    if True:
        R = RowBuilder(functions=["name", "address",
                                  {"weight":{"person_type":"adult"}},
                                  {"height":{"person_type":"adult"}}],
                   provider_dict_list=[{"provider": "faker.providers.address", "locale": "fr_FR"},
                                       {"provider": "faker.providers.person", "locale": "fr_FR"},
                                       {"provider": "faker.providers.weight", "locale": "en_US"},
                                       {"provider": "faker.providers.height", "locale": "en_US"}
                                        ],
                       mark_for_replacement_fields=["weight", "address"])
    else:
        R = RowBuilder(functions=["weight", "height"],
                       provider_dict_list=[{"provider": "faker.providers.weight", "locale": "en_US",
                                            "config": {"person_type": "adult"}},
                                           {"provider": "faker.providers.height", "locale": "en_US",
                                            "config": {"person_type": "adult"}}
                                           ])

    for i in [R.gen_row() for x in range(0,16)]:
        print(i)
