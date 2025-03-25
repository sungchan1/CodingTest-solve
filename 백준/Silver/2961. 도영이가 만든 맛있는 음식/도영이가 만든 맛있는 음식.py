from collections import  namedtuple
n = int(input())
result = float('inf')

Flavor = namedtuple("Flavor", ["sour", "bitter"])
ingredients = {}

bits = 1
for _ in range(n):
    sour, bitter = map(int, input().split())
    ingredients[bits] = (Flavor(sour, bitter))
    bits = bits << 1


for food_code in range(1, 2**n):
    sour = 1
    bitter = 0
    for ingredient_code in ingredients.keys():
        if food_code & ingredient_code:
            sour *= ingredients[ingredient_code].sour
            bitter += ingredients[ingredient_code].bitter
    result = min(result, abs(sour-bitter))


print(result)