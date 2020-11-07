# Les listes et les tuples

De la même manière qu'une chaîne de caractères est un objet Python contenant 0, 1 ou plusieurs caractères, un *tuple* ou une *liste* 
est un objet Python pouvant contenir 0, 1 ou plusieurs objets Python.

Un *tuple* est un ensemble d'objets séparés par des `,` et une liste est un ensemble d'objets séparés par des `,` entre crochets: `[` et `]`.

```python runnable
tuple_exemple = 1, 2, 3
liste_exemple = [1, 2, 3]
print(type(tuple_exemple), tuple_exemple)
print(type(liste_exemple), liste_exemple)
print(type([tuple_exemple]), [tuple_exemple], [tuple_exemple][0])
```