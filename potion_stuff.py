import time


# containers
pewter_cauldron = 'pewter_cauldron'
copper_cauldron = 'copper_cauldron'
martini_glass = 'martini_glass'
old_kettle = 'old_kettle'

# ingredients
snake_skin = 'snake_skin'
fish_eyes = 'fish_eyes'


def stir(potion, direction):
    """Stirs the potion.

    Updates colour in the class instance.

    Parameters
    ----------
    potion : Potion instance
        The potion to be stirred.
    direction : {'clockwise', 'anti-clockwise'} str
        The direction in which the potions is to be stirred
    """
    if direction == "clockwise":
        potion.colour = "vomit-yellow"
        print('NO!! Your potion turns vomit-yellow. Did you stir in the right direction?')
    elif direction == "anti-clockwise":
        potion.colour = "newt-green"
        print('Your potion turns a lovely newt-green.')
    else:
        print("What are you doing to your potion??")
        print("You need to stir, not distribute the contents on the floor!")
    return


def simmer(potion, duration):
    """Cooks the potion.

    Updates simmer_duration and cooked attributes in the class instance.

    Parameters
    ----------
    potion : Potion instance
        The potion to be cooked.
    duration : int
        How long to cook the potion for [hours].
    """
    potion.simmer_duration = duration
    if duration < 2:
        print('Are you sure you are cooking the potion enough? Your ingredients look a bit raw...')
    elif duration > 5:
        print('Oops, you have fallen asleep at your desk! Are you sure you want to simmer this long?')
    else:
        potion.cooked = True
    return


unicorn_hair = 'unicorn_hair'
tea_leaves = 'tea_leaves'


def inspection_by_Snape(potion, target_potion='python_expert'):
    """Checks if potion was brewed correctly.

    Prints narration of inspection process - read to see if potion passed inspection.
    Snape checks container, heat_source, ingredients, and whether potion was cooked.
    If something is wrong, function returns at that point.

    Parameters
    ----------
    potion : obj 
        Instance of Potion (class from potion_class).
    target_potion: str, optional
        Name of potion to be checked by Snape. Currently possible potions are 'python expert', 'example_potion'
    """

    print('-------------------------------')
    if not potion:
        print(f'"There is no potion I can inspect!"')
        print(f'    (Tip: are you actually returning a proper potion and passing it to Snape?)')
        return

    print(f'A sour looking Snape walks towards you to inspect your {target_potion} potion.')
    print(f'"What do we have here, {potion.name}...?"')
    print_delay_dots()



    # set variables for each potion that need to be checked
    if target_potion == 'python_expert':
        expected_container = 'pewter_cauldron'
        expected_heat_source = 'fire'
        expected_ingredients = ['fish_eyes', 'tea_leaves', 'unicorn_hair']
        expected_cooked = True
        expected_simmer_duration = 2
    elif target_potion == 'example_potion':
        expected_container = 'old_kettle'
        expected_heat_source = 'eternal_flame'
        expected_ingredients = []
        expected_cooked = True
        expected_simmer_duration = 5
    else:
        print(f'"What is this, {potion.name}? This is not the name of an existing potion, check your spelling!"')
        print(f'    (Target potion was not recognised, please check your spelling.)')
        return

    # check that correct setup was used
    if potion.container == expected_container and potion.heat_source == expected_heat_source:
        print(f'You have used the correct setup, Snape cannot complain - he looks even more sour.')
    else:
        print(f'Snape smirks and remarks "You have used the wrong cauldron or heat, {potion.name}!" \n'
              f'With a flick of his wand he vanishes the potion. \n'
              f'"I am taking 10 points from Ravenclaw, {potion.name}. Start again!"')
        return

    print_delay_dots()

    # check if all ingredients are there
    if sorted(potion.ingredients) == expected_ingredients:
        print(f'You have used the correct ingredients, Snape cannot complain - his face darkens.')
    else:
        print(f'Snape smirks and remarks "You have used the wrong ingredients, {potion.name}!" \n'
              f'With a flick of his wand he vanishes the potion. \n'
              f'"I am taking 10 points from Gryffindor, {potion.name}. Start again!"')
        return

    print_delay_dots()

    # check that potion is cooked
    if potion.cooked == expected_cooked and potion.simmer_duration == expected_simmer_duration:
        print(f'The potion is cooked properly, Snape cannot complain - he is looking annyoyed now.')
    else:
        if potion.simmer_duration < expected_simmer_duration:
            print(f'Snape smirks and remarks "Your potion is undercooked!" \n')
        elif potion.simmer_duration > expected_simmer_duration:
            print(f'Snape smirks and remarks "Your potion is overcooked!" \n')
        print(f'With a flick of his wand he vanishes the potion. \n'
              f'"I am taking 10 points from Hufflepuff, {potion.name}. Start again!"')
        return

    print_delay_dots()

    print(f'Snape mutters "You got away this time, {potion.name}!", since there is nothing wrong with '
          f'your {target_potion} potion.')
    print_delay_dots()
    print(f'You pack your bags and leave as fast as you can to have a butterbeer at the lake!')

    return


# heat sources
fire = 'fire'
eternal_flame = 'eternal_flame'
breathe_on_cauldron = 'breathe_on_cauldron'



def print_delay_dots(dur=0.5, number=2):
    for i in range(number):
        time.sleep(dur)
        print('.')

