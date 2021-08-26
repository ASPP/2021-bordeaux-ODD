import brewing.containers
import brewing.cooking
import brewing.ingredients as bwing
import brewing.inspection
import brewing.potion


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
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=brewing.containers.pewter_cauldron, heat_source=brewing.cooking.fire)
    
    list_ingredients = [bwing.fish_eyes, bwing.unicorn_hair, bwing.tea_leaves]
    my_potion.add_ingredients(ingredients=list_ingredients)
    
    dsimmer = 2
    brewing.cooking.simmer(my_potion, duration = dsimmer)
    
    # todo: write this function!
    return my_potion


if __name__ == "__main__":
    my_name = 'ASPP participant'
    #my_potion = make_example_potion(my_name)
    my_potion = make_python_expert_potion(my_name)
    # Let Snape inspect the potion
    #brewing.inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')
    brewing.inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')


