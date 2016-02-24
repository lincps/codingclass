# Fun Vibes (Paper Fortune) Game
# ahfarrell@gmail.com

from __future__ import print_function


def pick_colour():
    while True:
        print("pick a colour (red, blue, green, or orange):")
        colour = input().strip()

        if colour in ('red', 'blue', 'green', 'orange'):
            print("you have selected: " + colour)
            return colour
        else:
            print("you have not selected a valid colour: " + colour)


def pick_number():
    need_input = True
    while need_input:
        print("pick a number (between 1 and 8):")
        number = input().strip()

        if number in ('1', '2', '3', '4', '5', '6', '7', '8'):
            print("you have selected: " + number)
            return number
        else:
            print("you have not selected a valid number: " + number)


colour_choice = pick_colour()
number1_choice = pick_number()
print("And one more...")
number2_choice = pick_number()

if colour_choice == 'red' and number1_choice == '1' and number2_choice == '8':
    print("Be kind.")
elif colour_choice == 'blue' and number1_choice == '2' and number2_choice == '7':
    print("Be encouraging.")
elif colour_choice == 'green' and number1_choice == '3' and number2_choice == '6':
    print("Be thoughtful.")
elif colour_choice == 'orange' and number1_choice == '4' and number2_choice == '5':
    print("Be gentle.")
else:
    print("Be positive.")
