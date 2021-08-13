from unittest import mock
import calc_food

@mock.patch("calc_food.input", create=True)
def test_calc_food_order_valid(mock_input):
  mock_input.side_effect = [3, 2, 1, 5]
  
  assert calc_food.calc_food_order() == (3*10 + 2*20 + 1*30 - 5)*1.2
  mock_calc.assert_called_with(3, 10)
  mock_calc.assert_called_with(2, 20)
  mock_calc.assert_called_with(1, 30)
  
@mock.patch("calc_food.input", create=True)
def test_calc_food_order_invalid_input(mock_input):
  mock_input.side_effect = [True]
  
  with pytest.raises(ValueError):
    calc_food.calc_food_order()
    
@mock.patch("calc_food.input", create=True)
def test_calc_food_order_no_order(mock_input):
  mock_input.side_effect = [1, 0, 0, 12, 1, 0, 0, 13]
  
  assert calc_food.calc_food_order() == 0
  assert calc_food.calc_food_order() == 0
