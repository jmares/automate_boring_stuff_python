import pyinputplus as pyip

extras = []
prices = {
    'bread': { 'wheat': 2.5, 'white': 2.0, 'sourdouch': 3.0 },
    'protein': { 'chicken': 2.5, 'turkey': 2.0, 'ham': 1.5, 'tofu': 3.5 },
    'cheese': { 'cheddar': 1.0, 'Swiss': 1.5, 'mozzarella': 2.0 },
    'extras': { 'mayo': 0.3, 'mustard': 0.3, 'lettuce': 0.6, 'tomato': 0.7}
}

price = 0

print('--- bread ---')
bread = pyip.inputMenu(['wheat', 'white', 'sourdouch'], numbered=True)

print('\n--- protein ---')
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)

print('\n')

if pyip.inputYesNo(prompt='Do you want cheese? ') == 'yes':
    print('\n--- cheese ---')
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
else:
    cheese = 0

if pyip.inputYesNo(prompt='Do you want mayo? ') == 'yes':
    extras.append('mayo')

if pyip.inputYesNo(prompt='Do you want mustard? ') == 'yes':
    extras.append('mustard')

if pyip.inputYesNo(prompt='Do you want lettuce? ') == 'yes':
    extras.append('lettuce')

if pyip.inputYesNo(prompt='Do you want tomato? ') == 'yes':
    extras.append('tomato')

amount = pyip.inputInt(prompt='How many sandwiches do you want? ', min=1)

price = prices['bread'][bread] + prices['protein'][protein]
if cheese:
    price += prices['cheese'][cheese]
for extra in extras:
    price += prices['extras'][extra]

total_price = price * amount
print('Total price: €' + str(total_price))