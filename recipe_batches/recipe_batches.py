#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # take in a recipe and the ingredients you have.
    # compare the two -- if you have enough ingredients -> increment batch
    # decrement ingredients based on the matching recipe key/value.
    # if you don't -- return batch




    # keep track of values
    batches = 0
    no_ingredients = False

    while no_ingredients is False:
        for item in recipe:
            if item in ingredients.keys():
                if recipe[item] <= ingredients[item]:
                    # decrement the ingredients based on the recipe amount
                    ingredients[item] -= recipe[item]
                else:
                    no_ingredients = True
                    break
            else:
                # returning 0 because if the ingredient isn't in both dicts, we can't make it
                batches = 0
                no_ingredients = True
        # adding this to the bottom so it doesn't run the first time we go through the loop, and we have the chance to return 0 if we can't make the recipe
        if no_ingredients:
            break
        
        batches += 1

    return batches




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))