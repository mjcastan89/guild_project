"""Calculates the amount of dog food to order based on user inputs of dogs and food available."""
from enum import Enum


class dog_food_ratio_enum(Enum):
  """Enum for the dog food ratio to size of dog"""
  small = 10
  medium = 20
  large = 30


def calc_food_order(num_small_dogs , num_medium_dogs, num_large_dogs, leftover_food):
  """Calculates the amount of dog food to order in lbs based of user input. The user inputs 
  include number of small, medium and large dogs respectively plus the amount of food leftover.
  This function defaults to calculating 20% more than necessary. Just in case.
  
  :param num_small_dogs: Number of small dogs to calculate food for
  :type num_small_dogs: int
  :param num_medium_dogs: Number of medium dogs to calculate food for
  :type num_medium_dogs: int
  :param num_large_dogs: Number of large dogs to calculate food for
  :type num_large_dogs: int
  :param leftover_food: Amount of food leftover in lbs
  :type leftover_food: int
  :return: Amount of dog food to order in lbs
  :rtype: float
  """
  if not isinstance(num_small_dogs, int) and num_small_dogs >= 0:
    raise ValueError(f"The value provided for small dogs is not a valid int; value provided was {num_small_dogs}.")
  if not isinstance(num_medium_dogs, int) and num_medium_dogs >= 0:
    raise ValueError(f"The value provided for medium dogs is not a valid int; value provided was {num_medium_dogs}.")
  if not isinstance(num_large_dogs, int) and num_large_dogs >= 0:
    raise ValueError(f"The value provided for large dogs is not a valid int; value provided was {num_large_dogs}.")
  if not isinstance(leftover_food, int) and leftover_food >= 0:
    raise ValueError(f"The value provided for leftover food is not a valid int; value provided was {leftover_food}.")
  if sum([num_small_dogs, num_medium_dogs, num_large_dogs]) > 30:
    raise ValueError(f"The total number of dogs is greater than 30; Shelter is overbooked by {sum([num_small_dogs, num_medium_dogs, num_large_dogs]) - 30}.")
  
  print("Calculating next month's food order...")
  small_dog_food = num_small_dogs * dog_food_ratio_enum.small.value
  medium_dog_food = num_medium_dogs * dog_food_ratio_enum.medium.value
  large_dog_food = num_large_dogs * dog_food_ratio_enum.large.value
  food_needed = small_dog_food + medium_dog_food + large_dog_food

  if food_needed <= leftover_food:
      print(f"Current food need is: {food_needed} lbs and there are still {leftover_food} lbs leftover. No need to order more dog food.")
      return 0

  food_to_order = round((food_needed - leftover_food) *1.2, 1)
  print(f"Amount of dog food to order is: {food_to_order} lbs.")
  return food_to_order

if __name__ == "__main__":
    calc_food_order(5, 3, 7, 17)
