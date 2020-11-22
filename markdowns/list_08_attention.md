# Attention

Si vous modifiez une liste sur laquelle vous êtes en train d'itérer, cela peut mener à des résultats inattendus.

## Suppresion de l'élément courant

```python runnable
l = [ i for i in range(12) ]
for i in l:
    print('.', end='')
    l.remove(i)
print()
print(l)
```

```python runnable
j = 0
l = [ i for i in range(12) ]
for i in l:
    print('.', end='')
    del l[j]
    j += 1
print()
print(l)
```

En supprimant le j-ième élément d'une liste, le j+1-ième élément devient le nouveau j-ième élément. L'élément suivant de la liste sera donc l'ancien j+2-ième élément et le j+1-ième élément ne sera pas supprimé. On ne traverse la boucle que 6 fois au total. 

```python runnable
l = [ i for i in range(12) ]
for i in range(len(l)):
    print('.', end='')
    del l[i]
print()
print(l)
```

Ici c'est la même chose sauf que `len(l)` est évalué avant le début de la boucle, donc la boucle sera exécuté 12 fois. 
Après la 6-ième itération, 6 éléments ont été supprimés de la boucle et la liste a dorénavant une taille de 6. Lors de la 7-ième itération, on essaye de supprimer le 7-ième élément de la liste, mais vu que celui-ci n'existe pas (la taille de la liste est dorénavant 6), une erreur est retournée.

## Ajout d'un élément

```python runnable
l = [ i for i in range(12) ]
for i in range(len(l)):
    print('.', end='')
    l.append(l[i])
print()
print(l)
```

Vu que `len(l)` est évalué avant le début de la boucle, la boucle est exécutée 12 fois et on ajoute donc 12 éléments à notre liste.

```python runnable
l = [ i for i in range(12) ]
for i in l:
    print('.', end='')
    l.append(i)
print()
print(l)
```

Par contre, en itérant sur chaque élément de la liste, la boucle s'exécute tant qu'on n'arrive pas jusqu'à la fin de cette liste. Vu qu'on ajoute un élément à cette liste à chaque tour de boucle, cette boucle ne termine jamais.