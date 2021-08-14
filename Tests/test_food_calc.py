from unittest import mock
from food_calculator import calc_food_order

def test_calc_food_order_valid():
  assert calc_food_order(5, 3, 7, 17) == 363.6
  
def test_calc_food_order_ValueError():
  with pytest.raises(ValueError):
    calc_food_order(-5, 3, 7, 17)
  
  with pytest.raises(ValueError):
    calc_food_order(5, True, 7, 17)
    
  with pytest.raises(ValueError):
    calc_food_order(5, 3, 'seven', 17)
    
  with pytest.raises(ValueError):
    calc_food_order(5, 3, 7, False)
    
def test_calc_food_order_no_order():
  assert calc_food_order(1, 0, 0, 10) == 0
  
  assert calc_food_order(1, 0, 0, 11) == 0
