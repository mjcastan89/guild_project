# guild_project
Guild Education take-home QA Engineer Project

## Description
This Python project will calculate the amount of dog food a specific dog shelter should order for the following month based on the present conditions. The user is able to input the number of small dogs, medium dogs, large dogs and the current amount of dog food (in lbs) and calculate how much the shelter should order. If there is more or equal amount of food left over to what is needed for the following month, the returned amount will be 0.

## Dependencies
* Python 3.6

## Usage
It should be pretty simple. Download the package and from a Python terminal run:
``bash
  python <local path to file>/food_calc.py
 ``
and follow the input requests for:
  * Number of small dogs present
  * Number of medium dogs present
  * Number of large dogs present
  * Number of food leftover (in lbs)
The module will return the amount of dog food to order for the following month in lbs.

## Contributing
Feel free to go crazy, but update those tests!!!
  
## Future plans
The dog size to dog food ratio is presently not modifiable, but set to this specific shelter's numbers. Ideally, there would be a way to modify this as the specific shelter deems fit. Could be their shelter is very active with their dogs or uses more dense dog food.
