# Colorful Data
Evenly Distribute Color Palette To Objects

Easily Scale Color Palette 

# Example


```python
from ColorfulData_Package.ColorfulData import ColorfulData as CD
from bokeh.palettes import Turbo256
```

## Get_Colors()

#### Small 5 Item Request:
```python
CD.Get_Colors(5,Turbo256)
```
```terminal
['#30123b', '#3f98fe', '#3ff58a', '#dae236', '#f46516']
```


#### Large 300 Item Request:
```python
myPalette = CD.Get_Colors(300,Turbo256)
print(f'Items Returned: \n\t{len(myPalette)}\nSample: \n\t{myPalette[:10]}')
```
```terminal
Items Returned: 
	300
Sample: 
	['#30123b' '#30123b' '#311542' '#311542' '#32184a' '#32184a' '#341b51'
 '#341b51' '#351e58' '#351e58']
```
To accommodate 300 colors from a palete with only 256 colors, the returned pallete has ordered dupilcates

Here you see color #30123b is utilized at index 0 and 1.  Color #311542 is utilized at index 2 and 3


## Get_Colors_Matched()
```python
myList = ['a','a','b','c','b','d']

CD.Get_Colors_Matched(myList,Turbo256)
```
```terminal
array([['a', '#30123b'],
       ['b', '#2ab9ed'],
       ['c', '#9efd3e'],
       ['d', '#fc8624']], dtype='<U7')
```
