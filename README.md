# AudioFeature-B

**Prototyp im Rahmen des Komplexpraktikums [Visual] Audio Processing**  
Institut für Software- und Multimediatechnik, Professur für Mediengestaltung  
Technische Universität Dresden, Fakultät Informatik  
WiSe 2020/2021  
Till Große, Markus Forbrig

**Aufbau des Repositorys:**
* AudioKPPython
    * Pythonskript zur Visuellen Analyse extrahierter Daten
    * Pythonskript zur Berechnung der Dimensionsreduktion (UMAP)
* ExtractionFSDKaggle2018
    * ZSHskript um kompilierten Essentia Extraktor auf alle FSDKaggle Datein   
    anzuwenden  
    (kompilierter Extraktor muss dafür in dieses Verzeichnis gelegt werden)
* images
    * Bilder für dieses Readme
* vue_app
    * Vue App Implementierung des Prototyps
    * Anleitung zum Ausführen des Prototypen separat in dem Verzeichnis

**Externe Ressourcen**
* Audio Datein: FSDKaggel2018  
    * Seite: [FSDKaggle2018 | Zenodo](https://zenodo.org/record/2552860#.YCZS2C1oRp8)
    * direkter Link: [FSDKaggle2018.audio_train.zip](https://zenodo.org/record/2552860/files/FSDKaggle2018.audio_train.zip?download=1)  
    (beide zuletzt Abgerufen am 12. Februar 2020)  
    Das Verzeichnis (Name: "EXTRACT_FSDKaggle2018.audio_train") mit den  
    Audiodatein muss dabei im gleichen Verzeichnis wie das Repository liegen.
* Die Pythonskripte nutzen u.a. folgende Packages
    * Numpy
    * Matplotlib (pyplot)
    * JSON
    * Pathlib
    * Collections
    * UMap
    * Sklearn (preprocessing)
    
