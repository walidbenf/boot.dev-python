# Boot.dev Python
Les variables en python s'écrivent en Camel case exemple:
```python
hero_health = 100
```

On peut afficher la valeur d'une variable en mettant un f dans notre print et en encapsulant la variable:
```python
print(f"Walid a {hero_health} points de vie")
```
On peut utiliser le type None si jamais on a une variable qui n'a pas encore de valeur définie(par exemple la on peut définir age sur None et plus tard demander l'age à notre utilisateur:
```python
age = None
age = input("How old are you? ")
```

Toutes les fonctions doivent être définies avant d'être utilisées.
La plupart des développeurs Python résolvent ce problème en définissant d'abord toutes les fonctions de leur programme, puis en dernier
, ils appellent une fonction "point d'entrée". De cette façon, toutes les fonctions ont été lues par l'interpréteur Python avant que la première ne soit appelée.
```python
def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

# call entrypoint last
main()
```
Quand un programme ne contient pas de return il return None par défaut,
donc les 3 exemples suivants retourne la même chose
```python
def my_func():
    print("I do nothing")
    return None
```
```python
def my_func():
    print("I do nothing")
    return
```
```python
def my_func():
    print("I do nothing")
```
Les parametres sont les noms qu'on utilise pour se referer aux valeurs, alors que les arguments sont les valeurs en elles mêmes,
La différence entre les parametres et les arguments en code:

```python
# a et b sont les parametres
def add(a, b):
    return a + b

# 5 et 6 sont les arguments
sum = add(5, 6)
```
Floor division is like normal division except the result is floored afterward, which means the result is rounded down to the nearest integer. The // operator is used for floor division.
```python
7 // 3
# 2 (an integer, rounded down from 2.333)
-7 // 3
# -3 (an integer, rounded down from -2.333)
```
Python has built-in support for exponents - something most languages require a math library for.
```python
# reads as "three squared" or
# "three raised to the second power"
3 ** 2
# 9
```
Binary in Python
You can write an integer in Python using binary syntax using the 0b prefix:
```python
print(0b0001)
# Prints 1

print(0b0101)
# Prints 5
```
The built-in int function can convert a binary string to an integer. It takes a second argument that specifies the base of the number (binary is base 2). For example:
```python
# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
```
