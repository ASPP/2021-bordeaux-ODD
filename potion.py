from potion_stuff import *


class Potion:

    def __init__(self, name):
        """This is a class for brewing potions."""
        self.colour = 'there-is-no-potion-so-the-potion-has-no-color'
        self.cooked = False
        self.container = None
        self.heat_source = None
        self.ingredients = []
        self.simmer_duration = -1
        self.name = name

    def setup(self, container=None, heat_source=None):
        """Add a container and/or heat_source to the potion.

        Updates container and heat_source attributes in the class instance.

        Parameters
        ----------
        container : str, optional
            The name of the container to brew the potion in.
        heat_source : str, optional
            The name of the heat source used to cook the potions
        """
        if container == None:
            print(f'You have not specified a container - where do you think you will brew your potion?')
        if heat_source == None:
            print(f'You have not specified a heat source - how will you cook the potion?')
        self.container = container
        self.heat_source = heat_source

    def add_ingredients(self, ingredients=None):
        """Add ingredients to the potion.

        Updates ingredients and colour attributes in the class instance.

        Parameters
        ----------
        ingredients : array_like, optional
            A list of ingredients (str) to add to the potion.
        """
        if ingredients is None:
            print(f'You have added no ingredients - have you spilt them on the floor again?')
        else:
            self.ingredients = ingredients
            self.colour = "transparent"


def make_example_potion(name):

    my_potion = Potion(name=name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=old_kettle, heat_source=eternal_flame)
    # Simmer for 5 hours.
    simmer(my_potion, duration=5)

    return my_potion


my_name = 'ASPP participant'
my_potion = make_example_potion(my_name)
# Let Snape inspect the potion
inspection_by_Snape(potion=my_potion, target_potion='example_potion')


def make_python_expert_potion(name):
    print("I am a Python Expert")
    # todo: write this function!
    return

    



