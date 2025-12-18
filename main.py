"""
Ce module permet de lire un fichier CSV contenant des listes d'entiers
et d'effectuer des opérations statistiques simples (min, max, somme, etc.).
"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    Retourne le contenu du fichier <filename> sous forme de liste de listes d'entiers.
    Utilise ';' comme séparateur de données.
    """
    data = []
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            for line in f:
                # Nettoyage de la ligne et découpage par le point-virgule
                clean_line = line.strip()
                if clean_line:
                    # Conversion de chaque morceau en entier
                    integers = [int(x) for x in clean_line.split(';') if x]
                    data.append(integers)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} est introuvable.")
    return data

def get_list_k(data, k):
    """Retourne la kième liste de la structure data (indice k)."""
    try:
        return data[k]
    except IndexError:
        return []

def get_first(l):
    """Retourne le premier élément de la liste l."""
    return l[0] if l else None

def get_last(l):
    """Retourne le dernier élément de la liste l."""
    return l[-1] if l else None

def get_max(l):
    """Retourne le maximum de la liste l."""
    return max(l) if l else None

def get_min(l):
    """Retourne le minimum de la liste l."""
    return min(l) if l else None

def get_sum(l):
    """Retourne la somme de la liste l."""
    return sum(l) if l else 0


#### Fonction principale

def main():
    """
    Fonction principale pour tester les fonctions secondaires.
    """
    # Chargement des données
    data = read_data(FILENAME)
    # Affichage de toutes les listes lues
    print("--- Contenu du fichier ---")
    for i, l in enumerate(data):
        print(f"Ligne {i} : {l}")
    # Test spécifique sur la liste à l'indice 37 (si elle existe)
    k = 37
    print(f"\n--- Test sur l'indice k={k} ---")
    list_k = get_list_k(data, k)

    if list_k:
        print(f"Liste récupérée : {list_k}")
        print(f"Premier élément : {get_first(list_k)}")
        print(f"Dernier élément : {get_last(list_k)}")
        print(f"Maximum         : {get_max(list_k)}")
        print(f"Minimum         : {get_min(list_k)}")
        print(f"Somme           : {get_sum(list_k)}")
    else:
        print(f"La liste à l'indice {k} n'existe pas ou est vide.")


if __name__ == "__main__":
    main()
