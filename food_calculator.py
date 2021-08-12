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
  
  :return: Amount of dog food to order in lbs
  :rtype: float
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
  small_dog_food = num_small_dogs * dog_food_ratio_enum.small.value
  medium_dog_food = num_medium_dogs * dog_food_ratio_enum.medium.value
  large_dog_food = num_large_dogs * dog_food_ratio_enum.large.value
  food_needed = (small_dog_food + medium_dog_food + large_dog_food) * 1.2

  if food_needed <= leftover_food:
      print(f"Current food need is: {food_needed} lbs and there are still {leftover_food} lbs leftover. No need to order more dog food.")
      return 0

  food_to_order = food_needed - leftover_food
  print(f"Amount of dog food to order is: {food_to_order} lbs.")
  return food_to_order

if __name__ == "__main__":
    calc_food_order()
