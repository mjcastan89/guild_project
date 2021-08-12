# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
"""Calculates the amount of dog food to order based on user inputs"""
from enum import Enum

class dog_enum(Enum):
  small = "small"
  medium = "medium"
  large = "large"
  
dog_food_ratios = {
  dog_enum.small.value: 10,
  dog_enum.medium.value: 20,
  dog_enum.large.value: 30
 }

# Change this to take user input instead
def calc_food_order():
  """Calculates the amount of dog food to order in lbs based of user input. This function defaults to calculating 20% more than necessary. Just in case."""
  print("How many small dogs are present (as integer)? ")
  num_small_dogs = input()
  print("How many medium dogs are present (as integer)? ")
  num_medium_dogs = input()
  print("How many large dogs are present (as integer)? ")
  num_large_dogs = input()
  print("How much dog food is present (in lbs)? ")
  leftover_food = input()
  
  print("Calculating next month's food order...")
  small_dog_food = _calc_dog_food(num_small_dogs, dog_enum.small.value)
  medium_dog_food = _calc_dog_food(num_medium_dogs, dog_enum.medium.value)
  large_dog_food = _calc_dog_food(num_large_dogs, dog_enum.large.value)
  food_needed = (small_dog_food + medium_dog_food + large_dog_food)
  
  print(f"Amount of dog food to order is: {(food_needed - leftover_food)*1.2} lbs.")

def _calc_dog_food(num_dogs, dog_size):
  """Returns the amount of dog food to order per number of dogs and dog size in lbs.
  
  :param num_dogs: Number of dogs to calculate food for
  :type num_dogs: int
  :param dog_size: Dog size to calculate food for
  :type dog_size: str
  :return: Calculated amount of dog in lbs
  :rtype: int
  :raises ValueError: If values provided are not ints
  """
  if not isinstance(num_dog, int):
    raise ValueError(f"The value given for 'num_dog' is not an integer; The value given was {num_dog}.")
  if not isinstance(dog_size, int):
    raise ValueError(f"The value given for 'dog_size' is not an integer; The value given was {num_dog}.")
    
  return num_dogs * dog_food_ratios[dog_size]

if __name__ == "__main__":
    calc_food_order()
