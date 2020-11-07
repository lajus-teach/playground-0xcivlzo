# Les listes et les tuples

De la même manière qu'une chaîne de caractères est un objet Python contenant 0, 1 ou plusieurs caractères, un *tuple* ou une *liste* 
est un objet Python pouvant contenir 0, 1 ou plusieurs objets Python.

Un *tuple* est un ensemble d'objets séparés par des `,` (éventuellement entre parenthèses). Par exemple on peut définir le tuple contenant les trois valeurs entières 1, 2 et 3 
de la manière suivante:

```python runnable
tuple_exemple = 1, 2, 3
tuple_exemple2 = (1, 2, 3)
print(type(tuple_exemple))
print(type(tuple_exemple2))
if tuple_exemple == tuple_exemple2:
    print("Ce sont bien les mêmes tuples:", tuple_exemple)
# Un tuple peut être vide.
tuple_vide = ()
print("Le tuple vide:", tuple_vide)
```
Une *liste* est un ensemble d'objets séparés par des `,` entre crochets: `[` et `]`:

```python runnable
liste_exemple = [1, 2, 3]
print(type(liste_exemple))
print("La liste:", liste_exemple)
# Une liste peut être vide
liste_vide = []
print("La liste vide:", liste_vide)
```

## Des conteneurs universels

Les listes et les tuples peuvent contenir **n'importe quels types d'objets**:

```python runnable
t1 = 1, 2, 3
t2 = 1.0, 1.5 , 2.5
t3 = True, False, False
t4 = "Hello", "World"
print(t1, t2, t3, t4, sep="\n")
```
Ils peuvent contenir des **objets de types différents**:

```python runnable
t = 1, 1.5, False, "Hello"
print(t)
```
Ils peuvent même contenir **d'autres tuples ou listes**:

```python runnable
# Une liste contenant 4 éléments:
l = [ 1.0, (1, 2, 3), [1, False], ("Tuple", ["Liste"]) ]
print(l)
```

## Opérations sur les tuples et listes

Pour manipuler les *tuples* et les *listes*, on peut utiliser les mêmes opérations que sur les chaînes de caractères[^­1]:
 * **Taille** à l'aide de la fonction `len()`:
```python runnable
print(len((1, 2, 3)))
print(len([1, 1.5, False, "Hello"]))
print(len([ 1.0, (1, 2, 3), [1, False], ("Tuple", ["Liste"]) ]))
```
 * **Concaténation** à l'aide de l'opération `+`
```python runnable
print([1, 2] + [3, 4])
print([1, 2] + [True, False])
print((1, 2) + (3.0, 4.0))
# Par contre l'instruction suivante échoue:
print([1, 2] + (3.0, 4.0))
```
 * **Appartenance**: le mot-clé `in`, à l'extérieur d'une boucle `for`, permet de tester l'appartenance:
```python runnable
l = [1, 1.5, False, "Hello"]
print(1.5 in l)
print(True in l)
print(1.0 in l)
print("H" in l)
```
 * **Itération**: le mot-clé `in`, à l'intérieur d'une boucle `for`, permet d'itérer sur les éléments de la liste:
```python runnable
l = [1, 1.5, False, "Hello"]
for el in l:
    print(el)
```
 * **Accès** au ième élément l'aide de l'opérateur `[i]`:
```python runnable
l = [1, 1.5, False, "Hello"]
print(l[0])
print(l[1])
print(l[-1])
```
 * **Sous-chaîne** à l'aide de l'opération `[i:j]`:
```python runnable
l = [1, 1.5, False, "Hello"]
print(l[1:3])
print(l[2:])
print(l[:-1])
```

## QCM

