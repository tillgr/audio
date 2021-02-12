# vue_app
**[Visual] Audio Lab Web Application Prototype.**  

Institut für Software- und Multimediatechnik, Professur für Mediengestaltung  
Technische Universität Dresden, Fakultät Informatik  
WiSe 2020/2021  
Till Große, Markus Forbrig

## Project setup
```
npm install
```
For this Application to run properly you need to provide the audio files from  
[FSDKaggle2018 | Zenodo](https://zenodo.org/record/2552860#.YCZS2C1oRp8). 
([*direct Link*](https://zenodo.org/record/2552860/files/FSDKaggle2018.audio_train.zip?download=1))
(last accessed on the 12th of February 2020)  

The directory "EXTRACT_FSDKaggle2018.audio_train" containing the audio files  
then needs to be placed alongside the repository.


### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

## Project structure
* App.vue:
    * Basic App Component
    * Contains Navbar, Sidebar and MainView as child components
    * Handles Window resizing and checkbox changes (from Sidebar)
* Components
    * Navbar:
        * Application and window title
    * Sidebar:
        * Contains animated SampleGlyph to demonstrate the  
        feature -> visualisation representation.
        * Contains a checkbox for each feature to turn display on and off  
        These Checkboxes emit custom events that are then handled in the parent  
        App.vue
    * MainView:
        * Class-like, holds data for Glyphgraph, View, Audio, etc.    
        * Contains Methods that draw Glyphgraph (d3.js, svg in html),  
        play audio if glyph is clicked (clickOnGlyph),  
        create circleAttributes for each single Glyph from given Data,  
        control SVG transformation and scrolling for Zoom-Events.    
        * This Component includes ZoomControls as a child component
    * ZoomControls:  
        * Contains zoom in (+) and toom out (-) buttons that emit custom  
        events when clicked. These custom events are then handled in MainView.

