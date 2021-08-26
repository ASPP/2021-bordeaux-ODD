import brewing.potion
import brewing.containers
import brewing.cooking
import brewing.inspection
import brewing.ingredients


def make_example_potion(name):

    my_potion = brewing.potion.Potion(name=name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=brewing.containers.old_kettle, heat_source=brewing.cooking.eternal_flame)
    # Simmer for 5 hours.
    brewing.cooking.simmer(my_potion, duration=5)

    return my_potion


def make_python_expert_potion(name):
    print("I am a Python Expert")
    my_potion = brewing.potion.Potion(name=name)
    my_potion.setup(container=brewing.containers.pewter_cauldron, heat_source=brewing.cooking.fire)
    my_potion.add_ingredients([brewing.ingredients.tea_leaves, brewing.ingredients.unicorn_hair, brewing.ingredients.fish_eyes])
    brewing.cooking.simmer(my_potion, duration=2)
    # todo: write this function!
    return my_potion


if __name__ == "__main__":
    my_name = 'ASPP participant'
    my_potion = make_python_expert_potion(my_name)
    # Let Snape inspect the potion
    brewing.inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')


