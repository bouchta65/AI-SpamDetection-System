# 📧 AI-SpamDetection-System  
Système Intelligent de Détection de Spams — BMSecurity

---

## 📌 Contexte du Projet

En tant que développeur IA chez **BMSecurity**, vous êtes chargé(e) de concevoir un système intelligent capable de détecter automatiquement les emails frauduleux (spams) afin de renforcer la sécurité des communications.  
Ce projet constitue la base d’une solution évolutive destinée à être intégrée dans les plateformes de messagerie de nos clients.

L’objectif est de développer un **modèle performant de classification (spam vs ham)** en utilisant des techniques avancées de **NLP (traitement du langage naturel)** et d’**apprentissage supervisé**.

---

## 🎯 Objectifs

- Construire un pipeline NLP complet.
- Nettoyer et vectoriser les emails.
- Entraîner et comparer plusieurs modèles ML.
- Optimiser et sélectionner le meilleur modèle.
- Déployer une application **Streamlit** permettant de prédire si un email est spam.
- Préparer une solution évolutive et intégrable.

---

## 🧠 Pipeline du Projet

### 🔍 1. Analyse des Données
- Inspection du dataset : colonnes, tailles, formats.
- Détection et traitement :
  - des valeurs manquantes
  - des doublons
- Analyse de l’équilibre des classes (spam vs ham).
- Visualisation : WordClouds pour spam & ham.

### 🧹 2. Prétraitement du Texte (NLP)
- Normalisation :
  - Conversion en minuscules.
  - Suppression de la ponctuation et caractères spéciaux.
- Nettoyage :
  - Suppression des doublons.
  - Élimination des lignes vides.
- Tokenisation.
- Suppression des stopwords.
- Stemming (PorterStemmer).
- Vectorisation : `TfidfVectorizer` ou `CountVectorizer`.

### 🤖 3. Entraînement des Modèles
- Entraînement de plusieurs modèles :
  - Logistic Regression  
  - Multinomial Naive Bayes  
  - SVM  
  - Random Forest  
  - etc.
- Comparaison des performances :
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  
- Optimisation si nécessaire.
- Sélection du meilleur modèle.

### 💾 4. Intégration & Déploiement
- Sauvegarde du meilleur modèle avec `pickle`.
- Intégration dans une application **Streamlit**.
- Interface permettant :
  - de saisir un email
  - d’obtenir une prédiction (Spam / Ham)
  - d’afficher la probabilité associée

---

## 📁 Structure du Projet (exemple)

