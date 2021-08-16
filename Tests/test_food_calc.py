import pytest
from food_calculator import calc_food_order, max_dogs

def test_calc_food_order_valid():
  assert calc_food_order(5, 3, 7, 17) == 363.6
  
  assert calc_food_order(10, 10, 10, 0) == 720
  
@pytest.mark.parameterize("small_dogs, med_dogs, large_dogs, food", [(max_dogs + 1, 0, 0, 0), (0, max_dogs + 1, 0, 0), (0, 0, max_dogs + 1, 0), (11, 11, 11, 0)])
def test_calc_food_order_max_dogs(small_dogs, med_dogs, large_dogs, food):
  with pytest.raises(ValueError):
    calc_food_order(small_dogs, med_dogs, large_dogs, food)
  
@pytest.mark.parameterize("small_dogs, med_dogs, large_dogs, food", [(-5, 3, 7, 17), (5, -3, 7, 17), (5, 3, -7, 17), (5, 3, 7, -17)])
def test_calc_food_order_ValueError(small_dogs, med_dogs, large_dogs, food):
  with pytest.raises(ValueError):
    calc_food_order(small_dogs, med_dogs, large_dogs, food)
  
@pytest.mark.parameterize("small_dogs, med_dogs, large_dogs, food", [(5.2, 3, 7, 17), (5, True, 7, 17), (5, 3, "seven", 17), (5, 3, 7, False)])
def test_calc_food_order_TypeError(small_dogs, med_dogs, large_dogs, food):
  with pytest.raises(TypeError):
    calc_food_order(small_dogs, med_dogs, large_dogs, food)
    
def test_calc_food_order_no_order():
  # food_needed == leftover_food
  assert calc_food_order(1, 0, 0, 10) == 0
  
  # food_needed > leftover_food
  assert calc_food_order(1, 0, 0, 11) == 0
