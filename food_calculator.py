"""Do something here"""
from enum import Enums

dog_enum(Enums):
  small = "small"
  medium = "medium"
  large = "large"
  
dog_food_ratios = {
  dog_enum.small: 10,
  dog_enum.medium: 20,
  dog_enum.large: 30
 }

# Change this to take user input instead
def calc_food_order(num_small_dogs, num_medium_dogs, num_large_dogs, leftover_food):
  """Do more somethings"""
  small_dog_food = _calc_dog_food(num_small_dogs, dog_enum.small)
  medium_dog_food = _calc_dog_food(num_medium_dogs, dog_enum.medium)
  large_dog_food = _calc_dog_food(num_large_dogs, dog_enum.large)
  food_needed = (small_dog_food + medium_dog_food + large_dog_food)
  
  return (food_needed - leftover_food)*1.2

def _calc_dog_food(num_dogs, dog_size):
  """Do more somethings"""
  return num_dogs * dog_food_ratios[dog_size]

if __name__ == "__main__":
    calc_food_order()
