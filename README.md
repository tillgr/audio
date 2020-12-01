# AudioFeature-B
Todo: 
* Cinder Anwendung 
    * audio features mit Essentia extrahieren 
    * später dann Visualisierung 

**up next**
* read extracted features from yaml file into cinder app


![timetable](/images/zeitplanKPAudio.png)

Features: 
* [x] avg Loudness (RMS, …) 
* [x] spectral flux
* [ ] FrequencyBands
* [x] SpectralCentroid
* [x] SpectralComplexity
* [ ] (SpectralPeaks)


* spectral 
* [x]  MelBands 
* [x]  MFCC 
* [x]  HFC 
* [x]  Spectral Contrast 
* [ ]  (Panning) 
* [x]  Inharmonicity/dissonace
 
* Time 
* [x]  ZCR 
* [ ]  Leq, LARM, Loudness and LoudnessVicker 

* Tonal  
* [x]  HPCP/ Chroma
* [ ]  PitchYinFFT 
* [ ]  (tuning frequency) 
* [x]  (key)
* [ ]  (use TonalExtractor?)

* Rhythm 
* [ ]  BpmHistogramDescriptors/ BpmHistogram
* [ ]  (TempoCNN)

* SFX descriptors 
* [ ]  TCToTotal 
* [ ]  (MaxToTotal and MinToTotal) 

* Other high-level descriptors 
* [x]  DynamicComplexity  

* [ ]  Additionally look for audio problems? 

![screenshot from consultation](/images/features_screenshot.png)
