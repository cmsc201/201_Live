cats = {}
cats["tybalt"] = "tabby"
cats
{'tybalt': 'tabby'}
cats["jules"] = "tuxmaster general"
cats
{'tybalt': 'tabby', 'jules': 'tuxmaster general'}
cats[0]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 0
cats[0] = "This is not an ideal amount of cats"
cats[0]
'This is not an ideal amount of cats'
cats
{'tybalt': 'tabby', 'jules': 'tuxmaster general', 0: 'This is not an ideal amount of cats'}
cats[None] = "will it blend"
cats[None}]
  File "<input>", line 1
    cats[None}]
             ^
SyntaxError: invalid syntax
cats[None]
'will it blend'
cats[[1,2]] = "line?"
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'list'
cats["tybalt"] = "softy"
cats["tybalt"]
'softy'
del cats[0]
cats["tybalt"] = ["softy", "tabby"]
cats["tybalt"]
['softy', 'tabby']
stuff = "jeff"
cats["kitty"] = stuff
key = "kitty"
cats[key]
'jeff'
cats["tybalt"]
['softy', 'tabby']
cats["tybalt"].append("squeaker")
cats
{'tybalt': ['softy', 'tabby', 'squeaker'], 'jules': 'tuxmaster general', None: 'will it blend', 'kitty': 'jeff'}
features = {"weight": 20, "colors": ["black", "white"]}
cats["jules"] = features
cats
{'tybalt': ['softy', 'tabby', 'squeaker'], 'jules': {'weight': 20, 'colors': ['black', 'white']}, None: 'will it blend', 'kitty': 'jeff'}
cats['tybalt'][0].upper()
'SOFTY'
dogs = {"charlie": "the best no contest"}
[cats, dogs]
[{'tybalt': ['softy', 'tabby', 'squeaker'], 'jules': {'weight': 20, 'colors': ['black', 'white']}, None: 'will it blend', 'kitty': 'jeff'}, {'charlie': 'the best no contest'}]
animals = [cats, dogs]
cats["recursion"] = cats
