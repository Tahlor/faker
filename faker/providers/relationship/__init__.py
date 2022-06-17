from .. import BaseProvider, ElementsType

localized = True


class Provider(BaseProvider):
    relationships: ElementsType = (
        "brother", "sister", "father", "mother", "cousin", "daughter", "son", "aunt", "parent", "son", "daughter",
        "child", "husband", "wife", "spouse", "sibling", "grandfather", "grandmother", "grandparent", "grandchild",
        "grandpa", "grandma", "mom", "dad", "aunt", "uncle", "nephew", "niece", "cousin", "guardian"
    )

    def relationship(self) -> str:
        return self.random_element(self.relationships)
