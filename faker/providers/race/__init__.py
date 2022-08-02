from .. import BaseProvider, ElementsType, HierarchicalProvider

localized = True

class Provider(HierarchicalProvider):
    races: ElementsType = ()

    race_mofidier: ElementsType = (
        "non-Hispanic"
    )
    def relationship(self) -> str:
        return self.random_element(self.relationships)
