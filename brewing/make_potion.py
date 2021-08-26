
from brewing.potion import Potion
import brewing.containers
import brewing.cooking
import brewing.inspection


def make_example_potion(name):

    my_potion = brewing.Potion(name=name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)

    return my_potion


def make_python_expert_potion(name):
    print("I am a Python Expert")
    # todo: write this function!
    return


if __name__ == "__main__":
    my_name = 'ASPP participant'
    my_potion = make_example_potion(my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')


