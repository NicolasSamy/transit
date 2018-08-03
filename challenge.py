# Import des modules nécessaires

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from bokeh.plotting import figure
from bokeh.io import  push_notebook,output_notebook, show
output_notebook()  # pour un affichage en ligne

### Lecture du DataFrame

# Spécification du chemin
import os
os.chdir('/Users/nicolassamy/Challenge')
print('Répertoire actuel :', os.getcwd())

# Import du fichier
df = pd.read_csv('crowdfunding_challenge.csv', encoding='utf-8')

# Réduction du fichier à la taille du challenge DataScientest
df = df.iloc[:9999,:]

# Infos et vue d'ensemble du DataFrame
df.info()
df.head()

#Afficher les cinq premières lignes du jeu de données
#Quelle est la volumétrie du data set ?
#Quelles informations supplémentaires pouvez vous obtenir ?

###Afficher le nombre des valeurs uniques par colonne, que déduisez vous ?

#Si l'exploration s'est bien déroulée, vous avez remarqué que le data set comporte 15 colonnes. Certaines sont transparentes notamment l'ID, le nom, la devise, la date limite, la date de lancement et le pays. Pour les autres voici une courte description :
#
#main_category : Il y a 15 catégories principales pour le projet. Ces catégories principales classent généralement les projets en fonction du sujet et du genre auquel ils appartiennent.
#goal : le montant que le projet cherche à lever démarrer son activité. Le montant goal est une variable cruciale pour chaque projet car si elle est trop élevée, le projet peut ne pas réussir à augmenter cette somme d'argent et échouer. Si elle est trop faible, elle peut atteindre son objectif plus facilement mais les bailleurs de fonds pourraient ne pas être intéressés à s'engager davantage, et le projet risque de manquer de fonds pour aboutir.
#state : indique l'état d'avancement d'un projet
#plegded: le montant cumulé obtenu par l'intermédiaire de ses financeurs. Si le montant promis dépasse l'objectif, la société est considérée comme réussie. La variable «usd plegded» est la somme d'argent levée en dollars américains.
#Rappel : Si le montant total promis est inférieur à l'objectif, le projet échoue et la start-up ne reçoit aucun fonds.
#backers : le nombre de personnes qui ont soutenu le projet en promettant un certain montant.

#Quelle est la proportion de projets qui aboutissent ?
#Quelles modalités peut-on observer pour le champ state ?

#Filtrer la donnée en retenant seulement les projets qui ont réussi ou échoué ?

#Analyser l'influence de main_category sur le succès d'un projet à l'aide de visualisations. Que remarquez vous ?

#Transformer le type de données des colonnes deadline et launched en un type calendaire
#À partir des deux colonnes créer une nouvelle colonne length_days qui correspond à la durée de la campagne de crowdfunding
#Analyser l'influence de la durée sur le succès d'un projet ?
#Que constatez vous si vous croisez cette information avec l'information sur la catégorie ?

#Afficher maintenant la distribution du usd_goal_real qui est la conversion en dollars américain du goal ?

#Transformer ces distributions en distributions normales en appliquant la transformée logarithmique log(x+1) ?
#Afficher la nouvelle distribution du usd_goal_real ? Que constatez vous ?

#Créer un pairplot à l'aide du package seaborn qui visualise les relations entre les variables suivantes : (usd_goal_real,usd_pledged_real,length_days,backers,state) ?

#Qu'en déduisez vous ?

#Créer une nouvelle colonne class qui est la transformation binaire de la colonne state ?

#Créer une variable data dont laquelle vous stockez les features : usd_goal_real,length_days
#Stocker les données cibles class dans la variable target

#Diviser les matrices un ensemble d'entraînement et un ensemble de test

#Créer un classifieur de votre choix en suivant les étapes usuelles ?
#Charger la fonction f1_score du package sklearn.model_selection ?
#Evaluer votre propre modèle de classification ?

#Supprimer les lignes du dataframe df qui contiennent des valeurs manquantes ?
#Créer une variable data dont laquelle vous stockez les features : usd_goal_real,length_days,main_category ?
#Stocker les données cibles class dans la variable target?
#Charger le package preprocessing.scale et l'utiliser pour normaliser les variables :usd_goal_real,length_days du dataframe data ?
#En utilisant pd.get_dummies transformer la variable categorielle main_category en un ensemble de variables binaires type (0,1) ?

#Diviser les données en un ensemble d'entraînement (train_X et train_y) et un ensemble de test (test_X et test_y) ?

#Refaire la prédiction avec le même classifieur et évaluer sa précision et son f1_score ?

#Est ce que le preprocessing a amélioré la précision de votre modèle ?

#Essayer de changer les paramètres de votre modèle afin d'améliorer votre score ?

#Conseils pour améliorer la précision d'un modèle sont :
#
#Ajouter plus de données
#Traiter les valeurs manquantes et aberrantes.
#Ingénierie de features.
#Sélection de features
#Plusieurs algorithmes.
#Tunning du modèle.
#Méthodes d'ensemble
