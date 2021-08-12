"""Calculates the amount of dog food to order based on user inputs of dogs and food available."""
from enum import Enum


class dog_food_ratio_enum(Enum):
  """Enum for the dog food ratio to size of dog"""
  small = 10
  medium = 20
  large = 30


def calc_food_order():
  """Calculates the amount of dog food to order in lbs based of user input. The user inputs 
  include number of small, medium and large dogs respectively plus the amount of food leftover.
  This function defaults to calculating 20% more than necessary. Just in case.
  """
  print("How many small dogs are present (as integer)? ")
  num_small_dogs = int(input())
  print("How many medium dogs are present (as integer)? ")
  num_medium_dogs = int(input())
  print("How many large dogs are present (as integer)? ")
  num_large_dogs = int(input())
  print("How much dog food is present (in lbs)? ")
  leftover_food = int(input())
  
  print("Calculating next month's food order...")
  small_dog_food = _calc_dog_food(num_small_dogs, dog_food_ratio_enum.small.value)
  medium_dog_food = _calc_dog_food(num_medium_dogs, dog_food_ratio_enum.medium.value)
  large_dog_food = _calc_dog_food(num_large_dogs, dog_food_ratio_enum.large.value)
  food_needed = (small_dog_food + medium_dog_food + large_dog_food)
  
  print(f"Amount of dog food to order is: {(food_needed - leftover_food)*1.2} lbs.")

def _calc_dog_food(num_dogs, dog_food_ratio):
  """Returns the amount of dog food to order per number of dogs and dog size in lbs.
  
  :param num_dogs: Number of dogs to calculate food for
  :type num_dogs: int
  :param dog_food_ratio_enum: Dog food ratio
  :type dog_food_ratio_enum: int
  :return: Calculated amount of dog in lbs
  :rtype: int
  :raises ValueError: If values provided are not ints
  """
  if not isinstance(num_dogs, int):
    raise ValueError(f"The value given for 'num_dogs' is not an integer; The value given was {num_dogs}.")
  breakpoint()
  if not isinstance(dog_food_ratio, int):
    raise ValueError(f"The value given for 'dog_food_ratio' is not an integer; The value given was {dog_food_ratio}.")
    
  return num_dogs * dog_food_ratio

if __name__ == "__main__":
    calc_food_order()
