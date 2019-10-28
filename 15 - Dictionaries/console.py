ingred = {}
ingred["butter"] = "acne"
ingred
{'butter': 'acne'}
ingred["flour"] = "cupbread"
ingred
{'butter': 'acne', 'flour': 'cupbread'}
ingred["butter"]
'acne'
ingred["acne"]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'acne'
ingred["veg oil"] = "acne"
ingred
{'butter': 'acne', 'flour': 'cupbread', 'veg oil': 'acne'}
ingred["butter"] = "happy"
ingred
{'butter': 'happy', 'flour': 'cupbread', 'veg oil': 'acne'}
ingred["butter"] = ["happy", "acne"]
ingred
{'butter': ['happy', 'acne'], 'flour': 'cupbread', 'veg oil': 'acne'}
ingred["butter"]
['happy', 'acne']
ingred["butter"][1]
'acne'
ingred[1] = "not acne"
ingred
{'butter': ['happy', 'acne'], 'flour': 'cupbread', 'veg oil': 'acne', 1: 'not acne'}
ingred["cupbread"] = 2
ingred
{'butter': ['happy', 'acne'], 'flour': 'cupbread', 'veg oil': 'acne', 1: 'not acne', 'cupbread': 2}
ingred["butter"].append("some other thing")
ingred["butter"].append(12)
ingred
{'butter': ['happy', 'acne', 'some other thing', 12], 'flour': 'cupbread', 'veg oil': 'acne', 1: 'not acne', 'cupbread': 2}
animals = {}
animals["cat"] = "good"
animals["cat"] = "furry"
animals
{'cat': 'furry'}
