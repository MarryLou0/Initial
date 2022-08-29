from random import choice
# lists of possible foods that will be randomly chosen, grouped by mood
# group 0 is most comforting,
# group 1 is fast and easy to get,
# group 2 is the most healthy one

foods = [['pizza', 'gnocchi', 'pasta', 'tiramisu', 'dumplings', 'ramen'],
         ['tacos', 'tom yum', 'burrito', 'quesadilla', 'pad thai'],
         ['salad', 'sushi', 'stir fry', 'tofu with rice', 'veg smoothie']]

# greet the user
print("Hello! It's time to choose best food for now :)")


# choose from mood groups
while True:
    try:
        mood = int(input("Please rate your today's mood in scale from 0 to 5: "))
        if mood < 2:
            print(f'Okay, poor thing, here is something you may like: {choice(foods[0])}')
            break
        elif 2<= mood <= 3:
            print(f'Not great, not terrible, huh? Here you go: {choice(foods[1])}')
            break
        elif mood >3:
            print(f'Good for you! Good mood means good food: {choice(foods[2])}')
            break
    except ValueError:
        print('Seems not quite right, could you rate your mood in proper scale 0-5? ')







