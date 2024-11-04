###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = True
light_switch2 = True

bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2

if bulbs_on == 0:
    print(f'Switch one is off and switch two is off, so there are {bulbs_on} bulbs working')
elif bulbs_on == 1:
    print(f"Switch 1 is on and switch 2 is off so there is {bulbs_on} bulb working")
elif bulbs_on == 2:
    print(f'Switch one is off and switch two is on, so {bulbs_on} bulbs are working')
elif bulbs_on == 3:
    print(f"All the light switches are on, that means all the {bulbs_on} bulbs are working")


    

    

