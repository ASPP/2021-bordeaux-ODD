##import only the old_kettle object
#from brewing.containers import old_kettle
#print(old_kettle)

##import all the objects in ingredients but nothing else
#from brewing.ingredients import *
#print(snake_skin)
#print(fish_eyes)
#print(unicorn_hair)
#print(tea_leaves)

##import all the objects in the brewing package
#import brewing.cooking
#import brewing.ingredients
#import brewing.containers
#import brewing.inspection
#import brewing.make_potion
#import brewing.potion
#print(brewing.containers.old_kettle)

#write import cooking in the __init__.py file
import brewing as brw
print(brw.cooking.eternal_flame)
