from faker.providers import BaseProvider, ElementsType
import random

localized = True

class Unit:
    udict = {
    "major_units" : ["ft", "ft."],
    "minor_units" : ["in", "in."],
    }
    udict["minor_units_singular"] = ["inch"] + udict["minor_units"]
    udict["minor_units_plural"] = ["inches"] + udict["minor_units"]
    udict["major_units_singular"] = ["foot"] + udict["major_units"]
    udict["major_units_plural"] = ["feet"] + udict["major_units"]

    @staticmethod
    def unit(item, unit_type="major"):
        if item==1:
            return random.choice(Unit.udict[f"{unit_type}_units_singular"])
        else:
            return random.choice(Unit.udict[f"{unit_type}_units_plural"])

    @staticmethod
    def min_unit(item):
        return Unit.unit(item, unit_type="minor")

    @staticmethod
    def maj_unit(item):
        return Unit.unit(item, unit_type="major")

min_unit = Unit.min_unit
maj_unit = Unit.maj_unit

class Provider(BaseProvider):
    """ Format variation: feet/inches, decimal places
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # if "person_type" in kwargs:
        #     self.person_type = kwargs["person_type"]
        # else:
        #     self.person_type = "any"

    def height(self, person_type="any") -> str:
        if person_type=="any":
            person_type = random.choices(population = ['baby','adult','child'], weights = [0.05, 0.7, 0.25])[0]

        if person_type=="baby":
            inches = max(random.gauss(20, 3), 12)
            feet = inches/12
            formats = [f"{inches:.1f} {min_unit(inches)}",
                       f"{inches:.0f} {min_unit(inches)}",
                       f"{feet:.0f} {maj_unit(feet)} {inches - int(feet) * 12:.1f} {min_unit(inches)}",
                       f"{feet:.0f} {maj_unit(feet)} {inches - int(feet) * 12:.0f} {min_unit(inches)}",
                       f"{feet:.1f} {maj_unit(feet)}"]
            return random.choice(formats)

        elif person_type=="adult":
            feet = max(random.gauss(5.3,1),4)
            inches_remainder = (feet - int(feet)) * 11.49 # don't want it rounding to 12
            formats = [f"{feet:.0f} {maj_unit(feet)} {inches_remainder:.1f} {min_unit(inches_remainder)}",
                       f"{feet:.0f} {maj_unit(feet)} {inches_remainder:.0f} {min_unit(inches_remainder)}",
                       f"{feet:.1f} {maj_unit(feet)}"]
            return random.choice(formats)

        elif person_type=="child":
            feet = max(random.gauss(3.5, 1),2)
            inches_remainder = (feet - int(feet)) * 11.49
            formats = [f"{feet:.0f} {maj_unit(feet)} {inches_remainder:.1f} {Unit.min_unit(inches_remainder)}",
                       f"{feet:.0f} {maj_unit(feet)} {inches_remainder:.0f} {min_unit(inches_remainder)}",
                       f"{feet:.1f} {maj_unit(feet)}"]
            return random.choice(formats)

if __name__=='__main__':
    from faker.generator import Generator
    height = Provider(Generator())
    print([height.height() for i in range(10)])