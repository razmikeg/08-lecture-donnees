> [!CAUTION]
Ce travail s'effectue dans [l'environnement Github](https://perso.esiee.fr/~courivad/courses/utils/misc-01-github-environment.html)

# Lecture de données

En informatique, les données sont stockées de façon indépendante du programme qui les utilise. Il est donc nécessaire d’accéder à celles ci (depuis le programme) avec une fonction dédiée qui peut se décomposer en trois étapes:

- établir le lien avec la ressource physique qui les contient. Ce peut être un fichier local à la machine sur laquelle s’exécute le programme, ou un fichier distant accessible sur le réseau, une page web, etc. ;
- récupérer les données du fichier ;
- les retourner au programme appelant.

L'objectif de cet exercice est d'écrire une fonction de lecture des données contenues dans le fichier ``listes.csv`` et diverses fonctions manipulant des listes numériques.

Le fichier ``main.py`` contient :

- une fonction secondaire ``read_data()`` qui prend en argument un nom de fichier et retourne son contenu sous la forme d'une liste de `n` listes d'entiers si le fichier comporte `n` lignes.
- une fonction secondaire `get_list_k()` qui prend en argument la liste de listes retournée par `read_data()` et un indice ``k`` et retourne la kième liste.
- une fonction secondaire `get_first()` qui prend en argument une liste et retourne le premier élément de cette liste ;
- une fonction secondaire `get_last()` qui prend en argument une liste et retourne le dernier élément de cette liste ;
- une fonction secondaire `get_max()` qui prend en argument une liste et retourne le maximum de cette liste ;
- une fonction secondaire `get_min()` qui prend en argument une liste et retourne le minimum de cette liste ;
- une fonction secondaire `get_sum()` qui prend en argument une liste et retourne la somme de cette liste.
- la fonction principale ``main()`` dont le rôle est de faire appel aux fonctions secondaires pour vérifier leur bon fonctionnement.

## Tips

> [!TIP] Ouvrir le fichier
Utiliser la construction `with` et la fonction [`open()`](https://docs.python.org/3/library/functions.html#open) pour ouvrir le fichier. L'argument `file` est nécessaire. Il peut être fourni sous la forme d'une chaîne de caractères. L'argument `mode` est optionnel mais c'est une bonne pratique que de le fournir explicitement. On veut ici ouvrir le fichier en lecture. Quelle est la valeur à passer ? L'argument `encoding` est optionnel. Il est cependant vivement recommandé de le fournir. Pour l'essentiel on travaillera avec l'encodage universel `utf8` mais d'autres encodages sont parfois utilisés pour les fichiers français (`latin-1` ou `iso-8859-1`) ou sur le système d'exploitation Windows (`cp850`).

> [!TIP] Récupérer les données
La fonction `open()` renvoie un objet [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper), qui fournit quelques méthodes de lecture simples à manipuler. Parmi ces méthodes, [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines) est intéressante, car elle permet de récupèrer les données du fichier en une seule opération. Pour structurer le raisonnement, étudier l'objet retourné par [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines). Quelle est sa nature ? Quelle est sa taille ? Quelle est la nature des objets qu'il contient ?

> [!TIP] Retourner les données
Les données lues dans un fichier texte par [`readlines()`](https://docs.python.org/3/library/io.html#io.IOBase.readlines) sont retournées sous la forme d'une liste de chaines de caractères. Relire attentivement la consigne et jeter un oeil sur les doctests pour avoir une idée précise de l'attendu. Il sera efficace d'utiliser une *list comprehension* pour fabriquer une liste d'entiers pour chaque élément de la liste retournée.

<!-- START INSERT -->

## To do

1️⃣ Ecrire (ou modifier) le code de la fonction secondaire.

2️⃣ Si nécessaire, ajouter (ou modifier) les appels à la fonction secondaire logés dans la fonction principale ``main()``. Cela permet de tester la fonction secondaire sur quelques cas simples.

3️⃣ Exécuter le programme depuis le terminal. Tant que la fonction secondaire ne retourne pas les résultats attendus, répéter le cycle 1️⃣ 2️⃣ 3️⃣.

    $ python main.py

4️⃣ Lorsque les résultats obtenus à l'étape 3️⃣ sont satisfaisants, soumettre le code à une procédure de test plus robuste, les tests unitaires.

    $ pytest .python

Le score de test ``ST`` obtenu est le pourcentage de tests réussis. Tant que certains tests échouent, répéter le cycle 1️⃣ 2️⃣ 3️⃣ 4️⃣

5️⃣ Lorsque le score de test ``ST`` est satisfaisant, s'intéresser à la [qualité du code](https://perso.esiee.fr/~courivad/courses/utils/sources/python-23-codequality.html).

    $ pylint main.py

Si le score de qualité ``SQ`` n'est pas maximal, répéter l'étape 5️⃣ en tenant compte des messages dans le terminal

6️⃣ Lorsque les scores ``ST`` et ``SQ`` sont satisfaisants, pusher le travail vers votre repo distant. Ce travail est susceptible d'être pris en compte dans l'évaluation de l'unité.

    $ git add .
    $ git commit -m "un message explicatif"
    $ git push

> [!CAUTION]
En cas de soumissions multiples, seule la première est prise en compte.

<!-- END INSERT -->
