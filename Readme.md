# Exercice python programmation orienté objet

## Contexte :
Vous travaillez pour une bibliothèque et on vous demande de créer un système de gestion pour celle-ci. Ce système doit permettre de gérer les livres, les adhérents et les emprunts de livres.

## Objectifs :

L'exercice doit couvrir les principes suivants de la programmation orientée objet :

- Encapsulation
- Héritage
- Polymorphisme
- Abstraction

## Consignes : 

1. Créez une classe Livre avec les attributs suivants : titre (String), auteur (String), ISBN (String) et disponibilité (booléen). Implémentez les méthodes suivantes :

- un constructeur pour initialiser les attributs
- des getters et des setters pour chaque attribut
- une méthode `__str__` pour afficher les informations du livre de manière lisible

---

2. Créez une classe Adherent avec les attributs suivants : nom (String), prenom (String), identifiant (int) et emprunts (Liste de Livre). Implémentez les méthodes suivantes :

- un constructeur pour initialiser les attributs
- des getters et des setters pour chaque attribut
- une méthode pour ajouter un livre à la liste des emprunts
- une méthode pour retirer un livre de la liste des emprunts
- une méthode `__str__` pour afficher les informations de l'adhérent de manière lisible

--- 

3. Créez une classe abstraite Bibliotheque avec les attributs suivants : nom (String), adresse (String), livres (Liste de Livre) et adherents (Liste d'Adherent). Implémentez les méthodes suivantes :

- un constructeur pour initialiser les attributs
- des getters et des setters pour chaque attribut
- une méthode abstraite pour ajouter un livre à la bibliothèque
- une méthode abstraite pour retirer un livre de la bibliothèque
- une méthode abstraite pour enregistrer un nouvel adhérent
- une méthode abstraite pour supprimer un adhérent

---

4. Créez une classe BibliothequeMunicipale qui hérite de la classe Bibliotheque. Implémentez les méthodes abstraites de la classe mère et ajoutez les fonctionnalités suivantes :

- Emprunter un livre : Un adhérent peut emprunter un livre s'il est disponible. Mettez à jour la disponibilité du livre et ajoutez-le à la liste des emprunts de l'adhérent.
- Rendre un livre : Un adhérent peut rendre un livre. Mettez à jour la disponibilité du livre et retirez-le de la liste des emprunts de l'adhérent.

---

5. Créez un fichier main pour tester les classes et les méthodes implémentées. Créez quelques instances de Livre, Adherent et BibliothequeMunicipale pour vérifier que tout fonctionne correctement.

> Note : N'oubliez pas d'utiliser les principes d'encapsulation, d'héritage, de polymorphorphisme et d'abstraction tout au long de l'exercice.

--- 

6. (Bonus) Créez une classe BibliothequeUniversitaire qui hérite également de la classe Bibliotheque. Ajoutez des fonctionnalités spécifiques aux bibliothèques universitaires, telles que :

- Une liste des départements (Liste de String) associés à la bibliothèque
- Une méthode pour ajouter un département à la liste
- Une méthode pour retirer un département de la liste
- Implémentez les méthodes abstraites de la classe mère et ajoutez les fonctionnalités d'emprunt et de retour de livre en tenant compte des départements. Par exemple, vous pouvez limiter le nombre d'emprunts simultanés pour les adhérents ne faisant pas partie des départements associés à la bibliothèque.

--- 

7. Mettez en œuvre le principe de polymorphisme en créant une méthode qui prend en paramètre une instance de Bibliotheque et affiche des informations sur la bibliothèque (nom, adresse, nombre de livres, nombre d'adhérents, etc.). Testez cette méthode avec des instances de BibliothequeMunicipale et de BibliothequeUniversitaire.

--- 

> Une fois que vous avez terminé l'exercice, assurez-vous que votre code est bien structuré, lisible et commenté. Pensez à utiliser des noms de variables et de méthodes clairs et explicites. Vérifiez que toutes les fonctionnalités sont correctement implémentées et fonctionnent comme prévu.

## Grille d'évaluation :

Votre travail sera évalué en fonction des critères suivants :

Respect des consignes et des principes de la programmation orientée objet
- Clarté et lisibilité du code
- Fonctionnement correct des fonctionnalités implémentées
- Utilisation efficace des concepts avancés tels que le polymorphisme et l'abstraction (si applicable)
- Qualité des commentaires et de la documentation

## Autres informations :

Cet exercice a été généré par ChatGPT v4.

Prompt utilisé : 

```text
À partir de maintenant tu es un professeur expert en programme informatique, tu maitrise à la perfection la programmation orienté objet dans plusieurs langage de programmation. Tel que Python.

Tu es donc un professeur dans une université, c'est le moment des examens de fin d'année, et tu dois créer un exercice complet pour évaluer le niveau des élèves en programmation orienté objet. 

Crée un exercice complet, avec une ou plusieurs consigne, qui permet d'exercer chaque principe du développement orienté objet en Python. 
```