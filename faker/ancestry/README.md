# Create a new provider

Create a new folder under providers. Create an `__init__.py` defining the new provider like so:

    from .. import BaseProvider, ElementsType
    
    localized = True
    
    
    class Provider(BaseProvider):
        jobs: ElementsType = (
            "brother", "sister", "father", "mother", "cousin", "daughter", "son", "aunt", "parent", "son", "daughter",
            "child", "husband", "wife", "spouse", "sibling", "grandfather", "grandmother", "grandparent", "grandchild",
            "grandpa", "grandma", "mom", "dad", "aunt", "uncle", "nephew", "niece", "cousin", "guardian"
        )
    
        def relationship(self) -> str:
            return self.random_element(self.jobs)

Now you can run:
    
    from faker import Faker
    fake = Faker()
    fake.relationship()

Alternatively, you can create your own class and monkey-patch it in:

    from faker import Faker
    from faker.providers import BaseProvider
    
    # create new provider class
    class MyProvider(BaseProvider):
        def foo(self) -> str:
            return 'bar'
    
    # then add new provider to faker instance
    fake.add_provider(MyProvider)
    fake.foo()

