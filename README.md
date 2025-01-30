# Projet VSCode

## Objectif
Ce projet vise à collecter des données brutes depuis GitHub pour les stocker dans un datalake DuckDB. Ces données serviront à alimenter un modèle d’analyse défini lors de l’atelier précédent.

## Outil choisi
Pour la collecte des données, nous avons choisi **l’API REST de GitHub**. Cet outil offre une flexibilité importante et est compatible avec les modules Python tels que `requests` pour automatiser les appels.

## Sources de données
Repository VSCode

## Etape 1 API REST GITHUB
Ici, on utilise donc l'API REST de Github, afin de collecter un certain nombre de données relatif au repo VSCODE. Les différentes fonctions utilisant l'API sont comprises dans le fichier github_api.py, qui seront appelées dans le fichier main.py. 
Les données ainsi obtenus sont au format JSON.

![image-3.png](attachment:image-3.png)

On définit une Classe python, et chaque méthode de cette classe correspondra à un type différent d'informations du repo VCODE que l'on récupèrera.

## Etape 2 DUCKDB
Maintenant, l'objectif est de charger nos données dans un datalake DuckDB. 

### 1. JSON to PARQUET
La fonction définit dans le fichier utils.py permet de convertir nos données du format JSON au format parquet (orienté colonne). On utilise pour cela l'outil pyarrow.

![image-4.png](attachment:image-4.png)

### 2. PARQUET to DuckDB
Cette fonction sera appelée dans le script to_duckdb.py qui permet ensuite, de charger nos fichiers parquets dans un datalake DuckDB. Ces données bruts, seront ainsi stockées dans différentes tables, dans le schéma raw.

![image-2.png](attachment:image-2.png)

## Etape 3 DBT
Maintenant, nous allons chercher à terminer notre architecture décisionnelle, en transformant nos données d'une structure brute, à la modélisation définit plutôt dans notre diagramme ERD:

![image.png](attachment:image.png)

Pour cela, nous allons avec DBT créer 3 schéma différents (bronze,silver et gold). Chacun de ces schémas comprendra plusieurs modèles (1 modèle = 1 table)

Une fois nos différents modèles créés pour chacun de ces schémas, on lance la commandes dbt build pour vérifier la bonne éxécution de nos transformations:

![image-5.png](attachment:image-5.png)

Tout nos différents schémas sont ainsi créés:

![image-6.png](attachment:image-6.png)

### 1. Schéma Bronze
Ce schéma correspond aux données bruts. Même si le schéma bronze est identique au schéma raw, il permet de normaliser les formats de stockage, assurer une copie de sauvegarde et permet de vérifier que DBT fonctionne correctement.

![image-7.png](attachment:image-7.png)

### 2. Schéma Silver
Ce schéma est un intermédiaire entre le bronze et le gold, et permet d'effectuer des traitements sur nos données, comme: garder les colonnes nécessaires, filtrer les données, normaliser certaines colonnes, etc.

![image-8.png](attachment:image-8.png)

### 3. Schéma Gold
Ce schéma est le schéma final, celui qui répond à notre but initial. Il pourra servir à faire des analyses sur nos données, où faire du BI. Le temps de requêtage (pour des dashboards par exemple) sera réduit, car les traitements seront déjà effectués dans le schéma silver.

![image-9.png](attachment:image-9.png)


Pour notre diagramme ERD, nous avons choisis de nous focaliser sur la table contributions_fact_table:

![image-10.png](attachment:image-10.png)

Ainsi, le modèle dans le dossier gold a été créé dans ce but, afin d'obtenir une table qui corrrespond le plus possible à la table contributions_fact_table définit dans notre diagramme ERD:

![image-11.png](attachment:image-11.png)


## Etape 4: BI et Dashboard

On peut maintenant analyser nos données pour consulter diverses informations. En intégrant un scheduler, on pourrait obtenir des dashboards qui se mettent à jour automatiquement tous les jours par exemple.
Exemple: On a ajouté un modèle gold, pour obtenir la table top_contributors, qui nous permet de visualiser les contributeurs les plus actifs du projet VSCODE:

![image-12.png](attachment:image-12.png)

On peut aussi le visualiser via un plot (matplotlib ici):

![image-13.png](attachment:image-13.png)


Egalement, on peut créer un modèle pour visualiser le nombre de commits au cours d'une année:

![image-16.png](attachment:image-16.png)


![image-15.png](attachment:image-15.png)

On constate une chute du nombre de commits entre Noël et le nouvel an (plutôt prévisible), et un pic au mois de mars.



## Lancement
1. Créez un fichier .env en suivant l'exemple du fichier .env.example, et écrire votre tocken github.
2. Lancer le script main.py
3. Lancer le script to_duckdb.py
4. Dans le dossier dbt_project, lancer dbt build
5. Dans le dossier Atelier_DuckDB, lancer duckdb parquet_directory/data_lake.duckdb pour visualiser les tables.

## Documentation DBT

### Diagramme DAG

![image-14.png](attachment:image-14.png)

### Divers

![image-17.png](attachment:image-17.png)

![image-18.png](attachment:image-18.png)