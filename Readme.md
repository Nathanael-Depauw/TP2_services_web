Ce projet est une imitiation d'un service de gestion de pret immobilier. Pour le lancer, utilisez les commandes suivantes :

$ python listener.py

$ uvicorn service_banque:app --reload --host="127.0.0.1" –port=8002

$ uvicorn service_composite:app --reload --host="127.0.0.1" –port=8000

$ uvicorn service_visit:app --reload --host="127.0.0.1" –port=8001

puis déposez un fichier de demande sous le format :

Nom
Prix
Adresse
Description

dans le dossier demands
