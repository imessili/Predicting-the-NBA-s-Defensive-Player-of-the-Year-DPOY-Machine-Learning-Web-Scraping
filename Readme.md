# Projet de Prédiction du Meilleur Défenseur de l'Année NBA (DPOY)

Ce projet se concentre sur la prédiction du prix NBA Defensive Player of the Year (DPOY) en combinant **web scraping**, **nettoyage de données**, **sélection d'attributs**, et **modèles de machine learning**.

## Aperçu du projet

Le projet est structuré en plusieurs notebooks, chacun focalisé sur une étape clé du processus de prédiction :

1. **All_DPOY_Winners_By_Year**
   - Extraction des votes pour le DPOY par année.

2. **DPOY_Winners**
   - Extraction de tous les joueurs ayant remporté le prix DPOY de 1993 à 2023.

3. **All_Teams**
   - Extraction des statistiques des équipes NBA (team_opponent et team_misc).

4. **All_Players**
   - Extraction des statistiques des joueurs (per_game, per_100_poss, et advanced) de 1993 à 2023, avec fusion en un seul ensemble de données.

5. **Adding_Additional_att_to_players**
   - Ajout d'attributs supplémentaires pour les joueurs à partir de sources externes.

6. **Méthodes de Sélection d'Attributs**
   - **Char_selection_Mutual_info** : Sélection basée sur l'information mutuelle.
   - **Char_selection_Pearson_R** : Sélection avec le coefficient de corrélation de Pearson.
   - **Char_selection_SelectFromModel** : Sélection basée sur Random Forest ou XGBoost.

7. **Implémentation de Kendall's Tau**
   - Implémente le coefficient de corrélation Kendall Tau pour tester la stabilité des sélections d'attributs sur différentes périodes de 5 ans.

8. **Comparaison Joueurs DPOY vs Non-DPOY**
   - Analyse des différences statistiques entre un joueur ayant remporté le DPOY et un joueur ne l'ayant pas remporté.

9. **Prédiction et Évaluation des Modèles**
   - Entraînement et évaluation de plusieurs modèles en utilisant différentes méthodes de sélection d'attributs.

## Technologies Utilisées

- **Python** : Langage principal pour le traitement et l'analyse des données.
- **Selenium & Web Scraping** : Utilisé pour extraire du contenu dynamique avec **Selenium**.
- **Pandas & NumPy** : Manipulation et nettoyage des données.
- **Scikit-learn** : Implémentation des modèles de machine learning.
- **XGBoost, Random Forest** : Algorithmes de prédiction.
- **Jupyter Notebooks** : Environnement de développement et d'exécution.
- **Matplotlib** : Visualisation des données.

## Instructions pour Lancer le Projet

1. Clonez le projet :
   ```bash
   git clone https://github.com/votre-repo-url.git
   ```

2. Ouvrez les notebooks dans **Jupyter** et exécutez les cellules dans l'ordre.

3. Suivez les instructions spécifiques à chaque notebook pour extraire les données, entraîner les modèles et évaluer les résultats.

## Prérequis

- **Python 3.x** : Assurez-vous que Python est installé.
- **Dépendances** : Installez les bibliothèques nécessaires.
- **Chrome Driver** : Téléchargez et installez un driver Chrome compatible avec votre navigateur.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

## Contact

Pour toute question ou suggestion, veuillez ouvrir une issue sur le repo ou me contacter à l'adresse suivante :

Email: **messiliislem@gmail.com**

---

# NBA Defensive Player of the Year Prediction (DPOY) Project

This project focuses on predicting the NBA Defensive Player of the Year (DPOY) award by combining **web scraping**, **data cleaning**, **feature selection**, and **machine learning models**.

## Project Overview

The project is divided into several notebooks, each focusing on a key step of the prediction process:

1. **All_DPOY_Winners_By_Year**
   - Extracts all voting tables for the DPOY by year.

2. **DPOY_Winners**
   - Extracts all players who have won the DPOY award from 1993 to 2023.

3. **All_Teams**
   - Extracts team statistics (team_opponent and team_misc) for all NBA teams.

4. **All_Players**
   - Extracts player statistics (per_game, per_100_poss, and advanced) for all players from 1993 to 2023 and merges them into one comprehensive dataset.

5. **Adding_Additional_att_to_players**
   - Adds additional attributes to players from external resources.

6. **Feature Selection Methods**
   - **Char_selection_Mutual_info**: Attribute selection based on mutual information.
   - **Char_selection_Pearson_R**: Attribute selection using Pearson correlation coefficient.
   - **Char_selection_SelectFromModel**: Attribute selection using Random Forest or XGBoost.

7. **Kendall's Tau Implementation**
   - Implements the Kendall Tau correlation coefficient to test the stability of feature selection across different 5-year intervals.

8. **DPOY vs Non-DPOY Player Comparison**
   - Compares a player who won the DPOY with one who did not, analyzing statistical differences.

9. **Prediction and Model Evaluation**
   - Trains and evaluates several models using different feature selection methods.

## Technologies Used

- **Python**: Core language for data processing and analysis.
- **Selenium & Web Scraping**: Web scraping with **Selenium** for extracting dynamic content.
- **Pandas & NumPy**: Data manipulation and cleaning.
- **Scikit-learn**: Implementation of machine learning models for predictive modeling.
- **XGBoost, Random Forest**: Algorithms for prediction.
- **Jupyter Notebooks**: Development and execution environment.
- **Matplotlib**: Data visualization.

## Setup Instructions

1. Clone the project:
   ```bash
   git clone https://github.com/your-repo-url.git
   ```

2. Open the notebooks in **Jupyter** and run the cells in order.

3. Follow the specific instructions in each notebook to extract the data, train the models, and evaluate the results.

## Dependencies

- **Python 3.x**: Make sure Python is installed.
- **Dependencies**: Install the required libraries.
- **Chrome Driver**: Download and install a Chrome Driver compatible with your browser.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, feel free to open an issue on the repository or contact me at:

Email: **messiliislem@gmail.com**
