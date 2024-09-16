La première et la deuxième partie du projet, "Prédiction du meilleur défenseur de l’année de la NBA", a été réalisée par : 
MESSILI Islem
BA Bintou
BINA Ayoub


Instruction pour lancer le notebook:

Environnement Python : Assurez-vous d'avoir un environnement Python fonctionnel installé sur votre système.

Dépendances : Installez les dépendances nécessaires qui ce trouve au debut de chaque notebook.

Exécution du code : Une fois le notebook ouvert, exécutez chaque cellule dans l'ordre.


Contenu de chaque notebook :

All_DPOY_Winners_By_Year:

Ce notebook extrait tous les tableaux des votes pour le DPOY par année.

DPOY_Winners:

Ce notebook extrait tous les joueurs ayant remporté le prix DPOY de 1993 à 2023.

All_teams:

Ce notebook extrait les statistiques (team_opponent et team_misc) de toutes les équipes de la NBA.

All_Players:

Ce notebook extrait les statistiques (per_game, per_100_poss, et advanced) de tous les joueurs ayant joué entre 1993 et 2023. Il fusionne également toutes les statistiques de chaque joueur pour créer un grand ensemble de données de 2789 joueurs et 16283 lignes.

Adding_Additional_att_to_players:

Ce notebook ajoute des attributs supplémentaires aux joueurs, incluant des ressources additionnelles.

Char_selection_Mutual_info:

Ce notebook effectue la sélection d'attributs en utilisant l'information mutuelle pour identifier les caractéristiques les plus pertinentes pour le modèle de prédiction.

Char_selection_Person_R:

Ce notebook utilise le coefficient de corrélation de Pearson pour sélectionner les attributs en fonction de leur corrélation avec la variable cible.

Char_selection_SelectFromModel:

Ce notebook utilise la méthode SelectFromModel pour sélectionner les attributs les plus importants basés sur un modèle d'apprentissage automatique, il est utilise avec Random Forest et XGBOOST.

Kendall's_Tau_Implementation:

Ce notebook implémente le coefficient de corrélation de Kendall Tau pour tester la stabilité des sélections d'attributs entre différentes tranches de 5 ans et différentes méthodes de sélection d'attributs.

DPOY_winner vs Non_DPOY_winner:

Ce notebook compare un joueur ayant remporté le prix DPOY avec un autre qui ne la pas remporté, en analysant les différences de leurs statistiques et performances.

Predct+Eval_model_RDF+MI_ALL :

Ce notebook entraîne et évalue un modèle Random Forest avec la sélection d'attributs par Information Mutuelle (MI) sur l'ensemble complet des données.

Predct+Eval_model_RDF+MI_PERIOD :

Ce notebook entraîne et évalue un modèle Random Forest avec la sélection d'attributs par Information Mutuelle (MI) sur des périodes de 5 a 9 ans.

Predct+Eval_model_RDF+RDF_ALL :

Ce notebook entraîne et évalue un modèle Random Forest avec la sélection d'attributs par Random Forest (SelectFromModel) sur l'ensemble complet des données.

Predct+Eval_model_RDF+RDF_PERIOD :

Ce notebook entraîne et évalue un modèle Random Forest avec la sélection d'attributs par Random Forest (SelectFromModel) sur des périodes de 5 a 9 ans.

Predct+Eval_model_XGB+PersonsR_ALL :


Ce notebook entraîne et évalue un modèle XGBoost avec la sélection d'attributs par le coefficient de corrélation de Pearson sur l'ensemble complet des données.

Predct+Eval_model_XGB+PersonsR_PERIOD :

Ce notebook entraîne et évalue un modèle XGBoost avec la sélection d'attributs par le coefficient de corrélation de Pearson sur des périodes de 5 a 9 ans.

Predct+Eval_model_XGB+XGB_ALL :

Ce notebook entraîne et évalue un modèle XGBoost avec la sélection d'attributs par XGBoost (SelectFromModel) sur l'ensemble complet des données.

Predct+Eval_model_XGB+XGB_PERIOD :

Ce notebook entraîne et évalue un modèle XGBoost avec la sélection d'attributs par XGBoost (SelectFromModel) sur des périodes de 5 a 9 ans.

Script_Eval :

Ce notebook contient le script d'évaluation qui utilise les résultats des prédictions pour compter le nombre de classements corrects et évaluer la performance globale de chaque modèle.

Note: 
Assurez-vous de télécharger et d'installer un Chrome Driver compatible avec votre navigateur Chrome.