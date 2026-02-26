# 🗺️ TD — Cartographie interactive avec Python et Folium

Ce TD vous apprend à exploiter un fichier CSV contenant ~39 000 villes françaises avec pandas, à rechercher des coordonnées GPS par nom de ville, puis à générer une carte interactive HTML grâce à Folium, en plaçant un marqueur cliquable sur la localisation trouvée.
#
Les prérequis sont très modestes : connaître les bases de Python (fonctions, boucles, conditions) suffit. Les bibliothèques pandas et Folium sont découvertes progressivement dans le TD, ce qui le rend accessible à des débutants encadrés.
---
#
❌ Pour des classes prépas, ce TD manque de profondeur théorique.
#
✅ En revanche, il reste très abordable pour BTS SIO, BUT Informatique 1ère année et Licence 1, voire NSI au lycée.
#
## 📁 Contenu du projet

| Fichier | Description |
|---|---|
| `villes_coo.csv` | Base de données de ~39 000 villes françaises (ville, latitude, longitude) |
| `villes_coordonnees.csv` | Fichier enrichi avec informations administratives (région, département, EPCI…) |
| `villes_coo.py` | Script Python principal à étudier et compléter |
| `carte.html` | Carte interactive générée automatiquement par le script |

---

## 🎯 Objectifs pédagogiques

- Lire et manipuler un fichier CSV avec **pandas**
- Rechercher des **données** dans un DataFrame par nom de ville
- Utiliser **Folium** pour générer une carte interactive
- Placer un **marqueur géolocalisé** et enregistrer le résultat en HTML
- Structurer un programme Python avec des **fonctions** et un bloc `main`

---

## ⚙️ Prérequis

- Python 3.x
- Les bibliothèques suivantes :

```bash
pip install pandas folium
```

---

## 🚀 Utilisation

1. Clonez le dépôt :

```bash
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
```

2. Lancez le script :

```bash
python villes_coo.py
```

3. Saisissez le nom d'une ville (première lettre en majuscule) :

```
Entrez le nom de la ville (Première lettre en majuscules) : Angers
La carte a été enregistrée sous le nom 'carte.html'
```

4. Ouvrez `carte.html` dans votre navigateur pour visualiser la carte.

---

## 🔍 Fonctionnement du script

```python
# 1. Lecture du CSV
data = pd.read_csv(fichier_csv, sep=';')

# 2. Recherche de la ville
ville_data = data[data['ville'] == nom_ville]

# 3. Génération de la carte
carte = folium.Map(location=[latitude, longitude], zoom_start=12)
folium.Marker([latitude, longitude], popup=nom_ville).add_to(carte)
carte.save("carte.html")
```

---

## 📊 Structure du fichier `villes_coo.csv`

```
ville;latitude;longitude
Angers;47.476657084;-0.556221025
Paris;48.853409;2.348800
Lyon;45.748000;4.849000
...
```

> Le séparateur est le point-virgule `;`. Le fichier contient environ **39 146 entrées**.

---

## 💡 Pistes d'amélioration

- Rendre la recherche **insensible à la casse** avec `.str.lower()`
- Afficher **plusieurs villes** simultanément sur la même carte
- Utiliser des **marqueurs colorés** 
- Cartographier toutes les communes d'un **département** depuis `villes_coordonnees.csv`

---

## 🛠️ Technologies utilisées

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/pandas-data--manipulation-lightblue?logo=pandas)
![Folium](https://img.shields.io/badge/Folium-mapping-green)
![HTML](https://img.shields.io/badge/Output-HTML-orange?logo=html5)

---

## 📄 Licence

Projet pédagogique — libre d'utilisation dans un cadre éducatif.
#
👤 Auteur : SERRES Régis - Enseignant - Lycée E de Constant, La Flèche (72) GitHub : @serres-regis-prof-estournelles
