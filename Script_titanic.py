#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:53:45 2023

@author: bastien
"""


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class Data():
    def __init__(self,fichier_csv):
        self.fichier_csv = fichier_csv
        self.data = None
    def read_file(self):
        self.data= pd.read_csv(self.fichier_csv,sep=";")
        return self.data
    def display_features(self):
        if self.data is None:  # Vérifier que la variable data a été initialisée
            self.read_file()
        head = self.data.head(3)
        tail = self.data.tail(3)
        columns = self.data.columns
        infos = self.data.info()
        return head, tail, columns, infos
    def clear_dataAge(self):
        self.data['Age'] = pd.to_numeric(self.data['Age'],errors='coerce')
        mean=self.data['Age'].mean()
        self.data['Age']=self.data['Age'].fillna(mean)
        return self.data['Age']
    def clear_dataSurvived(self):
        self.data['Survived'] = self.data['Survived'].replace('#No#', 'No') #On enlève les # pour la colonne 'Survived'
    def clear_dataSex(self):
        self.data['Sex'] = self.data['Sex'].replace(['male', 'female'], [1, 0])
    def test(self):
        #On attribut les variables X et Y aux colonnes correspondantes
        x=self.data[['Age', 'Sex', 'Pclass']]
        y=self.data['Survived']

        x_train, x_test, y_train, y_test = train_test_split(data_1,self.x, self.y, random_state=2, test_size=0.35)
        # Instanciation du modèle en définissant le nombre de voisins à utiliser
        knn = KNeighborsClassifier(n_neighbors=5)
        # Entraînement du modèle avec les données d'entraînement
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = knn.score(X_test, y_test)
        print(accuracy)

#print(data['Survived'].unique())


data_1=Data("Titanic_Passengers.csv")
data_1.display_features()
data_1.clear_dataAge()
data_1.clear_dataSex()
data_1.clear_dataSurvived()
data_1.test()


