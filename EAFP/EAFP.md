EAFP:
```python
try:
    x = my_dict["key"]
except KeyError:
    # handle missing key
```

LBYL:
```python
if "key" in my_dict:
    x = my_dict["key"]
else:
    # handle missing key
```
