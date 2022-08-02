from faker.providers import BaseProvider, ElementsType
import random

localized = True

class Unit:
    udict = {
    "major_units" : [],
    "minor_units" : ["oz","oz."],
    }
    udict["minor_units_singular"] = ["ounce"] + udict["minor_units"]
    udict["minor_units_plural"] = ["ounces"] + udict["minor_units"]
    udict["major_units_singular"] = ["pound", "lb.", "lb"] + udict["major_units"]
    udict["major_units_plural"] = ["pounds", "lbs.", "lbs"] + udict["major_units"]

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
    """ Format variation: lbs/oz, decimal places
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # if "person_type" in kwargs:
        #     self.person_type = kwargs["person_type"]
        # else:
        #     self.person_type = "any"

    def weight(self, person_type="any") -> str:
        if person_type=="any":
            person_type = random.choices(population = ['baby','adult','child'], weights = [0.05, 0.7, 0.25])[0]

        if person_type=="baby":
            oz = max(random.gauss(7.5 * 16, 32), 4*16)
            lbs = oz/16
            formats = [f"{oz:.1f} {min_unit(oz)}",
                       f"{oz:.0f} {min_unit(oz)}",
                       f"{lbs:.0f} {maj_unit(lbs)} {oz - int(lbs) * 12:.1f} {min_unit(oz)}",
                       f"{lbs:.0f} {maj_unit(lbs)} {oz - int(lbs) * 12:.0f} {min_unit(oz)}",
                       f"{lbs:.1f} {maj_unit(lbs)}"]
            return random.choice(formats)

        elif person_type=="adult":
            lbs = max(random.gauss(180, 80),80)
            oz_remainder = (lbs - int(lbs)) * 15.49 # don't want it rounding to 16
            formats = [f"{lbs:.0f} {maj_unit(lbs)} {oz_remainder:.1f} {min_unit(oz_remainder)}",
                       f"{lbs:.0f} {maj_unit(lbs)} {oz_remainder:.0f} {min_unit(oz_remainder)}",
                       f"{lbs:.1f} {maj_unit(lbs)}"]
            return random.choice(formats)

        elif person_type=="child":
            lbs = max(random.gauss(50, 30),15)
            oz_remainder = (lbs - int(lbs)) * 15.49
            formats = [f"{lbs:.0f} {maj_unit(lbs)} {oz_remainder:.1f} {Unit.min_unit(oz_remainder)}",
                       f"{lbs:.0f} {maj_unit(lbs)} {oz_remainder:.0f} {min_unit(oz_remainder)}",
                       f"{lbs:.1f} {maj_unit(lbs)}"]
            return random.choice(formats)

if __name__=='__main__':
    from faker.generator import Generator
    weight = Provider(Generator())
    print([weight.weight() for i in range(10)])