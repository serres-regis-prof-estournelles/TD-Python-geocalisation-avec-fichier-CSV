import pandas as pd
import folium

# Fonction pour obtenir les coordonnées GPS de la ville depuis le fichier CSV
def obtenir_coordonnees_de_csv(nom_ville, fichier_csv):
    data = pd.read_csv(fichier_csv, sep=';')  # Assurez-vous que le séparateur correspond à votre fichier
    ville_data = data[data['ville'] == nom_ville]

    if not ville_data.empty:
        latitude = ville_data['latitude'].values[0]
        longitude = ville_data['longitude'].values[0]
        return latitude, longitude
    else:
        print(f"Coordonnées non trouvées pour {nom_ville}.")
        return None, None

# Fonction principale
def main():
    fichier_csv = "./villes_coo.csv"  # Remplacez par le chemin relatif ou absolu correct vers votre fichier CSV
    nom_ville = input("Entrez le nom de la ville (Première lettre en majuscules) : ")

    # Obtenir les coordonnées GPS de la ville depuis le fichier CSV
    latitude, longitude = obtenir_coordonnees_de_csv(nom_ville, fichier_csv)

    if latitude is not None and longitude is not None:
        # Placer la ville sur la carte avec le nom de la ville comme étiquette
        carte = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker([latitude, longitude], popup=nom_ville).add_to(carte)
        folium.Marker([latitude, longitude], tooltip=nom_ville).add_to(carte)  # Ajoutez cette ligne pour l'étiquette

        # Enregistrer la carte au format HTML
        carte.save("carte.html")
        print(f"La carte a été enregistrée sous le nom 'carte.html'.")
    else:
        print("Coordonnées non trouvées. Vérifiez le nom de la ville ou le fichier CSV.")

if __name__ == "__main__":
    main()
