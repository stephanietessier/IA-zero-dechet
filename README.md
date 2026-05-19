# IA Zéro Déchet — Assistant personnel de tri, réparation et réutilisation

Projet éducatif prêt pour GitHub et Google Colab. Il propose un assistant IA simple qui aide une personne à décider quoi faire avec un objet : **trier**, **réparer**, **donner**, **réutiliser**, **composter** ou **éviter l’achat inutile**.

> ⚠️ Données fictives réalistes. Les consignes de tri varient selon les municipalités : vérifiez toujours les règles locales.

## Objectifs progressistes

- Réduire les déchets à la source.
- Favoriser la réparation plutôt que le remplacement.
- Encourager le don, le partage et l’économie circulaire.
- Rendre les consignes de tri plus accessibles.
- Proposer une IA sobre, explicable et respectueuse de la vie privée.

## Fonctionnalités

- Recommandation automatique à partir d’un objet décrit en langage naturel.
- Score écologique estimé.
- Suggestions de réparation et de réutilisation.
- Détection de catégories : plastique, textile, électronique, verre, papier, métal, organique, encombrant.
- Application Streamlit locale.
- Notebook Colab prêt à exécuter.

## Structure

```text
ia_zero_dechet/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── data/
│   ├── items_zero_dechet.csv
│   └── ressources_locales.csv
├── src/
│   ├── __init__.py
│   ├── recommender.py
│   └── utils.py
└── notebooks/
    └── IA_Zero_Dechet_Colab.ipynb
```

## Installation locale

```bash
git clone https://github.com/votre-compte/ia-zero-dechet.git
cd ia-zero-dechet
pip install -r requirements.txt
streamlit run app.py
```

## Utilisation dans Colab

1. Ouvrir `notebooks/IA_Zero_Dechet_Colab.ipynb`.
2. Exécuter les cellules dans l’ordre.
3. Tester avec des objets comme :
   - téléphone brisé
   - pot de yogourt
   - vieux manteau
   - marc de café
   - bouteille de verre

## Exemple de résultat

Entrée : `vieux téléphone avec écran brisé`

Sortie possible :

- Catégorie : électronique
- Action prioritaire : réparer ou déposer en écocentre
- Pourquoi : contient des métaux rares et des composants polluants
- Réutilisation : transformer en caméra de sécurité, lecteur audio ou téléphone de secours
- Score écologique : 92/100

## Limites

Ce projet ne remplace pas les consignes officielles des villes, écocentres ou organismes de récupération. Il s’agit d’un prototype pédagogique.

## Améliorations possibles

- Connexion à une API municipale de collecte.
- Géolocalisation des écocentres.
- Reconnaissance d’image d’objets.
- Modèle NLP plus avancé.
- Mode hors ligne pour écoles et bibliothèques.
