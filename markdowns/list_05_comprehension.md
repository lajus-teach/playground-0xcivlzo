# Construction d'une liste par compréhension

On peut construire une liste en énumérant chaque élément ou de manière itérative:
```python runnable
l = [0, 1, 4, 9, 16]
print(l)
l = []
for i in range(5):
    l.append(i*i)
print(l)
```

On peut aussi procéder par compréhension:
```python runnable
l = [ i*i for i in range(5) ]
print(l)
```

On peut lire cette instruction de la manière suivante: `l` est la liste des valeurs `i*i` pour `i` alant de 0 à 5. 

```python runnable
l = [ i*(j*j) for i in range(5) for j in range(3) ]
print(l)
```
