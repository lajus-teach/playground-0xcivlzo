# Construction d'une liste par compréhension

On peut construire une liste de trois manière différentes:
1. en énumérant chaque élément,
1. de manière itérative,
1. par comprehension.

```python runnable
# Enumération
l = [0, 1, 4, 9, 16]
print(l)
# Construction itérative
l = []
for i in range(5):
    l.append(i*i)
print(l)
# Par compréhension
l = [ i*i for i in range(5) ]
print(l)
```

On peut lire cette dernière instruction de la manière suivante: `l` est la liste des valeurs `i*i` pour `i` allant de 0 à 5.

---

La construction par compréhension peut utiliser plusieurs variables:

```python runnable
l = [ i+j for i in range(5) for j in range(3) ]
print(l)
# Est équivalent à la construction itérative:
l = []
for j in range(3):
    for i in range(5):
        l.append(i+j)
print(l)
```

Exemple:
```python runnable
l = [ i for j in range(2) for i in range(3, 5)]
```
?[Que vaut l ?]
-[ ] [1, 2, 3, 4]
-[ ] [1, 2, 1, 2]
-[ ] [1, 1, 2, 2]
-[ ] [3, 4]
-[ ] [3, 4, 3, 4]
-[X] [3, 3, 4, 4]

---

On peut utiliser le mot-clé `if` pour filtrer des éléments de la liste:

```python runnable
# On construit la liste de 0 à 20 en enlevant chaque multiple de 3:
l = [ i for i in range(21) if i % 3 != 0 ]
print(l)
# Est équivalent à la construction itérative:
l = []
for i in range(21):
    if i % 3 != 0:
        l.append(i)
print(l)
```
