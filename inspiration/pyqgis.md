---
marp: true
paginate: true
style: |

  section::after {
    color: white;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 3rem;

  }

  .center {
    text-align: center;
  }

  .topbar {
  padding-top: 125px;
  }

    .top50 {
  padding-top: 50px;
  }

      .top100 {
  padding-top: 100px;
  }

        .top150 {
  padding-top: 150px;
  }
  img{background-color:transparent}

  header {
        display: grid;
        grid-template-rows: 1fr;
        grid-template-columns: 1fr 1fr;
        grid-gap: 10px;
        box-sizing: border-box;
        justify-content: center;
        width: 100%;
    }

    header img {
        height: 50px;
    }

  footer {
        display: grid;
        grid-template-columns: 1fr max-content;
        #background-color: #bb2e29;
        color: white;
        align-content: right;
        font-size: 20px;
    }

  h1 {
  font-size: 70px;
  color: white;
    }  
  h2 {
  font-size: 50px;
  color: white;
    }

  h3 {
  font-size: 30px;
  color: white;
    }
    
  .slide_heaader {
    position:absolute;top:90px;left:75px;right:75px;font-size:50px;

  }

  li::marker {
  color: #397c67;
    }

   li {
  color: white;
  padding: 0px;
  font-size:30px;
  }

   p {
  color: white;
  padding: 0px;
  padding-top: 30px;
  font-size:30px;
  }

  img[alt~="center"] {
      display: block;
      margin: 0 auto;
    }

      .container {
    display: flex;
  }
  .col {
    flex:1;
    padding-right: 20px;
    padding-left: 20px;
    padding-top: 120px;

  }
    .col_tight {
    flex:1;
    padding-right: 20px;
    padding-left: 20px;
    padding-top: 60px;

  }

  .center_img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  }

header:  ![alt text](../ressources/images/logo/septima.svg "Title")

footer: Python-scripting i QGIS med PyQGIS  





        
---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:200px;left:75px;right:75px;font-size:70px;">Python-scripting i QGIS med PyQGIS.</h1>
<h2 style="position:absolute;top:360px;left:75px;right:75px;font-size:45;">Morten Fuglsang</h2>
<h3 style="position:absolute;top:430px;left:75px;right:75px;font-size:30;">12.05.2026</h3>


--- 

<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">INTRODUKTION</h1>

* QGIS har et avanceret Python API kendt som PyQGIS. 
* Næsten alle operationer, du kan udføre ved hjælp af QGIS, kan udføres ved hjælp af API'et.
* Dette giver udviklere mulighed for at skrive kode til at bygge nye værktøjer, tilpasse grænsefladen og automatisere arbejdsgange.


---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">PRÆSENTATION</h1>

<div class="columns">
<div>

## Hvem er jeg ?
* Ph.D i Geoinformatik fra AAU/AU
* Undervist GIS i snart 15 år
* Aldeles selvlært i Python
* GIS konsulent hos Septima
* Svært glad for PyQGIS til automatiseringer


</div>
<div class="">

## Hvem er i ?

</div>
</div>

--- 

<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">AGENDA</h1>

<div class="columns">
<div class="top50">

Vi kommer primært til at beskæftige os med Python scripting afviklet i QGIS, men afslutningsvis skal vi også forsøge at køre scripts uden at have QGIS åben.


</div>
<div class="top100">

* Frokost er kl 11.30
* Pauser tager vi ad hoc

</div>
</div>


---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">FORMATET</h1>

<div class="columns">
<div class="top150">

Mix mellem:
* Slides
* Gennemgang i dokumentationen
* PyQGIS kogebogen
* Forskellige typer øvelser


</div>
<div class="top50">

Røde opgaver løser I selv, blå opgaver løser vi sammen...
<br/>
![w:260](../ressources/images/assignments.png)

De fulde kodeeksempler finder I i `docs/eksempler.md`.


</div>
</div>

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Hvad bruger jeg PyQGIS til ?</h1>

```python
# Trin 1/4: Setup af scenarier og mapper
INPUTS = ['nutid-T10', 'nutid-T20', 'nutid-T50', 'nutid-T100']
BASEPATH = 'C:/Temp'

for scenario in INPUTS:
  input_folder = f'{BASEPATH}/{scenario}'
  output_folder = f'{BASEPATH}/output_{scenario}'
  os.makedirs(output_folder, exist_ok=True)

  if not os.path.isdir(input_folder):
    print(f'Skipping {scenario}: input folder not found')
    continue

  tif_files = [f for f in os.listdir(input_folder) if f.endswith('.tif')]
```

---


```python
# Trin 2/4: Loop filer og byg input/output stier
for scenario in INPUTS:
  input_folder = f'{BASEPATH}/{scenario}'
  output_folder = f'{BASEPATH}/output_{scenario}'

  if not os.path.isdir(input_folder):
    continue

  tif_files = [f for f in os.listdir(input_folder) if f.endswith('.tif')]

  for idx, filename in enumerate(tif_files, start=1):
    print(f'Processing {scenario}: {idx}/{len(tif_files)}')
    input_path = f'{input_folder}/{filename}'
    output_path = f"{output_folder}/{filename.rsplit('.', 1)[0]}.fgb"

    if os.path.exists(output_path):
      continue

    raster = QgsRasterLayer(input_path, filename.rsplit('.', 1)[0])
    if not raster.isValid():
      print(f'Could not read raster: {input_path}')
      continue
```

---

```python
# Trin 3/4: Reclassify rasteren (køres inde i fil-loopet)
reclass = processing.run('native:reclassifybytable', {
  'INPUT_RASTER': raster,
  'RASTER_BAND': 1,
  'TABLE': ['0', '1000', '1'],
  'NO_DATA': -9999,
  'RANGE_BOUNDARIES': 2,
  'NODATA_FOR_MISSING': False,
  'DATA_TYPE': 5,
  'OUTPUT': 'TEMPORARY_OUTPUT'
})
```

---


```python
# Trin 4/4: Polygonize + cleanup (køres inde i fil-loopet)
processing.run('gdal:polygonize', {
  'INPUT': reclass['OUTPUT'],
  'BAND': 1,
  'FIELD': 'DN',
  'EIGHT_CONNECTEDNESS': False,
  'EXTRA': '',
  'OUTPUT': output_path
})

if os.path.exists(reclass['OUTPUT']):
  os.remove(reclass['OUTPUT'])
```


--- 
<!-- backgroundColor: #b8063b -->
<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">OPSTART</h1>

## Indlæs QGIS projektet der ligger i /project

Det indeholder:
* Datalag og styling
* Printlayout

Opret en kopi af projektet - vi kommer til at bokse rundt med det...

---


<!-- backgroundColor: #2e495c -->

![w:750 center](img/project.png)


---



<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">RESSOURCER</h1>

Vi skal bruge forskellige ressourcer i dag : 

* https://docs.qgis.org/latest/
* https://qgis.org/pyqgis/master/

Åben dem i jeres browsere så i har dem klar...


---




<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">Struktur</h1>

* PyQGIS er som tidligere nævnt bygget efter objektorienteret programmering (OOP)-principper.

* Hver klasse repræsenterer typisk en "ting" i GIS-verdenen:

* Eksempel: QgsVectorLayer (et vektorlag), QgsRectangle (en udstrækning), QgsSymbol (et grafisk symbol).

---

Data håndteres gennem metoder kaldet:

* Getters: Metoder, der henter værdier fra objektet (f.eks. .extent(), .name()).

* Setters: Metoder, der opdaterer værdier i objektet (f.eks. .setName(), .setExtent()).

* Initialisering, der opretter nye objekter (layer = QgsVectorLayer(...))

Mange objekter kan "bygges sammen" — fx kan et lag (QgsVectorLayer) få et renderer-objekt (QgsRenderer), som igen indeholder symbol-objekter (QgsSymbol).

---


<!-- backgroundColor: white -->

https://github.com/webgeodatavore/qgis-class-diagram
https://labs.webgeodatavore.com/partage/diagramme_principal.html

![w:700 center](../ressources/images/diagramme_principal.svg)

---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:75px;left:75px;right:75px;font-size:50px;">Hvad skal vi bruge i dag ?</h1>
<img src="./img/overblik.png" width="800" class="center_img">


---


<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">Et par ord om generativ AI</h1>

* PyQGIS opbygningen er enormt og kompliceret - den kan være meget svær at navigere i...

* ChatGPT har et overblik som vi selv kan få meget svært ved at skabe os, den er virkelig god til at bygge PyQGIS kode, som meget ofte virker (Dokumentationen er god, den gætter sjældent...)


--- 

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Den indbyggede python editor</h1>

Vi arbejder i dag i den indbyggede python editor. 
Det er muligt at få QGIS til at bruge VS Code, men det er hacky og virker ikke altid...

<img src="./img/console.png" width="1200">

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Hvad kan man ?</h1>

<img src="./img/editor.png" width="950" class="center_img" style="margin-top:60px;">

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Hvad skal man passe på ?</h1>

Man skal gemme sine scripts ofte - og egentlig helst altid før du kører noget.
Det kræver ikke ret meget at få QGIS til at vælte, og den tager det hele med ned... Det er ærgeligt at miste kode på den måde

---


<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Dataprocessering eller kartografi ??</h1>

Hvad målet er med dit PyQGIS script, definerer hvad du har brug for...

* Hvis du skal lave kort eller præsentationer, så har du brug for QGIS interfacet med lag og struktur.

* Skal du analysere data og lave et data output, behøver du ikke lagvælgeren eller et projekt for den sags skyld... 

---


<!-- backgroundColor: #397c67 -->
<h1 style="position:absolute;top:340px;left:75px;right:75px;font-size:50px;">QGIS projektet og T.O.C</h1>

---

<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Indlæsning af lag</h1>

Når vi skal arbejde med lag, er der et par steder vi kan søge viden

Class dokumentationen (Hvad?):
* https://qgis.org/pyqgis/master/core/QgsVectorLayer.html

Cookbook (Hvordan?) :

* https://docs.qgis.org/3.34/en/docs/pyqgis_developer_cookbook/loadlayer.html


---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Eksempler fra cookbook</h1>

<img src="./img/vectorlayers1.png" width="600" class="center_img" style="margin-top:60px;">

<img src="./img/vectorlayers2.png" width="600" class="center_img" style="margin-top:60px;">

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Eksempler fra docs</h1>

<img src="./img/docs_layers.png" width="600" class="center_img" style="margin-top:60px;">

---


<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Adgang til projektets egenskaber</h1>

Når det kommer til QGIS projektet i PyQGIS, så har det skiftet navn et par gange, og derfor skal man være obs på resultater fra nettet...

* QgsMapLayerRegistry (gammel metode)

* QgsProject (Ny metode)
---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Aktuelle projekt</h1>



```python
project = QgsProject.instance()
print(project.crs())

mycrs = QgsCoordinateReferenceSystem(4326)
project.setCrs(mycrs)

```

https://qgis.org/pyqgis/3.40/core/QgsProject.html


---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Lag i projektet ? </h1>

Med OOP tankegangen skal vi være OBS på hvad vi spørger efter...

```python
project = QgsProject.instance()
layers = project.mapLayers()
for layer in layers :
    print(layer)    
    
layers = project.mapLayers().values()
for layer in layers:
    print(layer)
```
Giver ikke samme svar, hvad tror i der vises her ?

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Tilføje lag</h1>

For at tilføje et lag, skal vi bruge referencen til vores projekt, og en sti til filen vi ønsker at læse ind.
</br>

```python

  filename = 'C:/Septima/pyqgis_kursus/project/data/jernbane.geojson'

  layer = QgsVectorLayer(filename, "jernbane", "ogr")
  QgsProject.instance().addMapLayer(layer)

```
---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Tilføje lag fra service</h1>

For en wfs, er der en specifik URI streng der kan bygges :

```python
uri = "srsname='EPSG:25832' typename='ve:store_solcelleanlaeg' url='https://gisp.bpst.dk/ve/wfs'"
layer = QgsVectorLayer(uri, "WFS_Layer", "WFS")
QgsProject.instance().addMapLayer(layer)
```
For WMS er den lidt mere kompliceret, da det kræver kendskab til services bagved
```python
uri = (
  "https://tilecache6-miljoegis.mim.dk/gwc/service/wms?VERSION=1.1.1&TILED=true&crs=EPSG:25832&format=image/gif"
  "&layers=theme-arter_kystarealer&styles&tileMatrixSet=theme-arter_kystarealer-wmsc-229&tilePixelRatio=0"
  "&url=https://tilecache6-miljoegis.mim.dk/gwc/service/wms?VERSION%3D1.1.1%26TILED%3Dtrue"
)

rlayer = QgsRasterLayer(uri, 'theme-arter_kystarealer', 'wms')
QgsProject.instance().addMapLayer(rlayer)
```

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">QLR filer ?</h1>

Vi kan også relativt uproblematisk loade en QLR fil ind - dette kræver blot en adresse på filen.

* `.qlr` beskriver et lag (kilde + styling) og kan læses direkte ind i projektet.
* `.qml` er kun selve stylingen og bruges typisk på et allerede indlæst lag.

```python
qlr_path = "C:/Septima/pyqgis_kursus/ressources/skaermkort.qlr"
qlr_layers = QgsLayerDefinition().loadLayerDefinitionLayers(qlr_path)
QgsProject.instance().addMapLayers(qlr_layers)

```

---
<!-- backgroundColor: #b8063b -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Indlæsning</h1>

I filen ressources.txt ligger en URI til en WFS service - byg en streng der kan indlæse et lag fra denne WFS service i QGIS. Hvis du er modig, så prøv også at bygge en fra en GetCapabilities.

I mappen ressources ligger også en .qlr fil med det dæmpede skærmkort - læg den til projektet også.

---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Indlæsning - løsning</h1>

```python
uri = "srsname='EPSG:25832' typename='pdk:theme_pdk_zonekort_v' url='https://geoserver.plandata.dk/geoserver/wfs'"
layer = QgsVectorLayer(uri, "WFS_Layer", "WFS")
QgsProject.instance().addMapLayer(layer)


qlr_path = "C:/Septima/pyqgis_kursus/ressources/skaermkort.qlr"
qlr_layers = QgsLayerDefinition().loadLayerDefinitionLayers(qlr_path)
QgsProject.instance().addMapLayers(qlr_layers)
```

---




<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Eksport af data</h1>

<div class="container">
<div class="col_tight" >

QGIS benytter Gdal til at skrive data - og der skal angives et 'driver-navn' der passer til det format man ønsker

</div>
<div class="col_tight">


<img src="./img/gdal_drivers.png" width="450" class="center_img" style="margin-top:0px;">
https://gdal.org/en/stable/drivers/vector/index.html

</div>
</div>

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Eksempel</h1>

```python

layer = QgsProject.instance().mapLayersByName("jernbane")[0]

options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = 'GPKG'
options.layerName = 'Jernbane'
QgsVectorFileWriter.writeAsVectorFormatV3(layer, 'c:/temp/jernbane.gpkg', QgsProject.instance().transformContext(), options)

```

https://qgis.org/pyqgis/master/core/QgsVectorFileWriter.html

---
<!-- backgroundColor: #b8063b -->
<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">Eksport</h1>

Lav et script, der looper projektets TOC igennem, og eksporterer lag i projektet til en folder.
* lad navnet på laget blive filnavnet
* Eksperimenter med formater - lav mindst tre forskellige filtyper

---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Løsning - eksport</h1>

```python
options = QgsVectorFileWriter.SaveVectorOptions()

for layer in QgsProject.instance().mapLayers().values():
    print(layer.name())
    
    if layer.name() == 'bebyggelse':
        options.driverName = 'GPKG'
        options.layerName = layer.name()
        QgsVectorFileWriter.writeAsVectorFormatV3(layer, f'c:/temp/{layer.name()}.gpkg', QgsProject.instance().transformContext(), options)
    elif layer.name() == 'jernbane':
        options.driverName = 'GeoJSON'
        QgsVectorFileWriter.writeAsVectorFormatV3(layer, f'c:/temp/{layer.name()}.geojson', QgsProject.instance().transformContext(), options)
    elif layer.name() == 'skov':
        options.driverName = 'FlatGeobuf'
        QgsVectorFileWriter.writeAsVectorFormatV3(layer, f'c:/temp/{layer.name()}.fgb', QgsProject.instance().transformContext(), options)
    else:
        pass
```

---




<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Fjerne lag fra TOC</h1>

For at fjerne et lag igen, skal vi både bruge referencen til projektet, men selvfølgelig også til det lag vi ønsker at fjerne.

</br>

```python
layer = QgsProject.instance().mapLayersByName("jernbane")[0]
QgsProject.instance().removeMapLayer(layer.id())
```

Hvorfor bruger vi [0] ?


---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Lag træ'et</h1>

Indtil nu, har vi bare læst lag ind, og de bliver lagt til afhængigt af aktive lag.
Men QGIS lag-træet er en kompleks størrelse, der kan have grupper, undergrupper m.m.

```python
root = QgsProject.instance().layerTreeRoot()
print (root)
print (root.children())
```
<img src="./img/tree.png" width="1250" class="center_img" style="margin-top:0px;">

https://www.qgis.org/pyqgis/master/core/QgsLayerTree.html


---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Loop gennem træ'et</h1>

```python
root = QgsProject.instance().layerTreeRoot()
for child in root.children():
    if isinstance(child, QgsLayerTreeGroup):
        print(f'- Group: {child.name()}')
        for subchild in child.children():
            if isinstance(subchild, QgsLayerTreeLayer):
                layer = subchild.layer()
                print(f'- layer in group: {layer.name()}')
    elif isinstance(child, QgsLayerTreeLayer):
        print(f'- layer: {child.name()}, ID: {child.layerId()}')
```
<img src="./img/tree2.png" width="550" class="center_img" style="margin-top:0px;">


---

<!-- backgroundColor: #2665d1 -->
<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:50px;">Lad os lige prøve det sammen... </h1>

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Rokere rundt på TOC'en</h1>

Dette kan sagtens blive sindssygt omstændigt, og derfor heller ikke noget vi dykker langt ned i. 
- Det bliver bare utroligt træls at printe senere, når vi ikke kan styre rækkefølgen på lag...


---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Lad os lave nogle byggesten</h1>

```python
root = QgsProject.instance().layerTreeRoot()
shapeGroup = root.addGroup("Gruppe1")

layer1 = QgsVectorLayer("Point", "Layer 1", "memory")
layer2 = QgsVectorLayer("Polygon", "Layer 2", "memory")
QgsProject.instance().addMapLayer(layer1)
QgsProject.instance().addMapLayer(layer2)
```

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Flyt lag til gruppe</h1>

```python
root = QgsProject.instance().layerTreeRoot()
layer_node = root.findLayer(QgsProject.instance().mapLayersByName('Layer 1')[0].id())
group_node = root.findGroup("Gruppe1")

group_node.addChildNode(layer_node.clone())
root.removeChildNode(layer_node)
```

I praksis, så flytter du ikke laget - du laver en kopi, og sletter det oprindelige lag...

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Den anden vej rundt ?</h1>

```python
for child in group_node.children():
    if child.nodeType() == child.Layer and child.name() == 'Layer 1':
        layer_node = child
        root.addChildNode(layer_node.clone())
        group_node.removeChildNode(layer_node)

```
---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Flytte lag op og ned</h1>

Hvis du ikke har markeret et lag i TOC, så kommer nye lag til Øverst.
```python
root.removeChildNode(layer_node) 
root.addChildNode(layer_node)
```
Det er ikke altid det giver mening, så må man flytte dem 
(Træ'et indexeres fra 0, - så i dette tilfælde bliver det først)

```python
root.removeChildNode(layer_node)
root.insertChildNode(0, layer_node)
```
---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Tænd og sluk lag</h1>

Synligheden af et lag relaterer sig ikke til laget, men til Træ'et . Derfor skal vi ind via roden og finde laget.
Herefter er det en property der sættes til True/False om laget skal vises

```python
layer_name = "skov"
layer_node = root.findLayer(QgsProject.instance().mapLayersByName(layer_name)[0].id())
layer_node.setItemVisibilityChecked(False)
```

---

<!-- backgroundColor: #b8063b -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Organiser projektet</h1>

Opret en kopi af projektet med et nyt navn - nu skal vi rode i det...

* Opret en gruppe der hedder GeoDK, flyt GeoDanmark lagene derind
* Hvis i ikke har skærmkortet, så læg det til igen, og placer det nederst.
* Slå kommunelaget fra, så det ikke vises.
* Placer bebyggelse under Geodanmark-gruppen




---

<!-- backgroundColor: #397c67 -->
<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:50px;">Lag og Features </h1>

---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Lag og features</h1>

<div class="container">
<div class="col_tight" >



* Et lag indeholder features
* Et lag har et koordinatsystem og en geometritype

* En feature indeholder :
  * En geometri
  * Attributter


</div>
<div class="col_tight">


<img src="./img/overblik_feature.png" width="450" class="center_img" style="margin-top:0px;">


</div>
</div>

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Loope features for lag</h1>

For adgang til features på et layer, benyttes to metoder:
* getFeatures() på layer
* attributes() på de enkelte features

```python
layer = QgsProject.instance().mapLayersByName("bebyggelse")[0]

for feat in layer.getFeatures():
    #print(feat.attributes())
    print(feat.attribute('navn_1_skrivemaade'))
```
https://qgis.org/pyqgis/3.34/core/QgsFeature.html

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Editere feature</h1>

Hvis vi skal editere features, så skal laget sættes i edit-mode, ligesom i GUI'en. Dette gøres i Python med en with edit-syntaks:

```python
layer = QgsProject.instance().mapLayersByName("bebyggelse")[0]

with edit(layer):
    for feature in layer.getFeatures():
        if feature['objectid'] == '478699':
            feature['navn_1_skrivemaade'] = 'Mortenstrup'
        layer.updateFeature(feature)
```
https://qgis.org/pyqgis/3.40/core/QgsVectorLayer.html#qgis.core.QgsVectorLayer.updateFeature

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Oprette nyt lag</h1>



<div class="container">
<div class="col_tight" >



Hvis vi skal lave et tomt lag i brugerfladen, så vil vi typsik lave et scratch-layer.

Her kan vi opsætte geometri, koordinatsystem og kolonner i brugerfladen
- Det skal vi nu gøre i koden


</div>
<div class="col_tight">


<img src="./img/scratchlayer.png" width="400" class="center_img" style="margin-top:0px;">


</div>
</div>

---

Oprettelse af et nyt layer sker ved at kalde constructor-metoden på QgsVectorLayer, den tager tre elementer:

* En streg med crs og geometritype
* Et navn til laget
* typen - 'memory' hvis det er et scratchlag, det er klart det nemmeste her...

```python
layer = QgsVectorLayer('Point?crs=EPSG:25832', 'New Point Layer', 'memory')
```

https://qgis.org/pyqgis/3.40/core/QgsVectorLayer.html

---

<h1 style="position:absolute;top:75px;left:75px;right:75px;font-size:50px;">Tilføj attribut til lag</h1>

Nu har vi et helt tomt lag, nu skal vi bygge attributter, så vi har nogle felter at udfylde - her møder vi lagets dataprovider første gang...

```python
layer = QgsVectorLayer('Point?crs=EPSG:25832', 'New Point Layer', 'memory')
provider = layer.dataProvider()
fields = QgsFields()
fields.append(QgsField('name', QVariant.String))
provider.addAttributes(fields)
layer.updateFields()
```

https://qgis.org/pyqgis/3.34/core/QgsVectorDataProvider.html
https://qgis.org/pyqgis/3.40/core/QgsFields.html
https://qgis.org/pyqgis/3.40/core/QgsField.html

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Tilføj feature til lag</h1>

Vi skal nu oprette en ny feature - dette sker med QgsFeature class'en
Vi skal sætte to ting :
* Featurens geometri
* Featurens attributter 


```python
    feature = QgsFeature()
    feature.setGeometry(QgsGeometry.fromPoint(QgsPoint(0, 0)))
    feature.setAttributes(['test'])
```
https://qgis.org/pyqgis/3.40/core/QgsGeometry.html

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Muligheder for geometrioprettelse</h1>


<div class="container">
<div class="col_tight" >

Geometrier kan oprettes med en masse forskellige set-operationer, der tager forskeliige inputs:
* WKT - oprettes ud fra informationerne i WKT'en
* Resten skal oprettes med den tilsvarende class-definition 

</div>
<div class="col_tight">


<img src="./img/geometry_create.png" width="550" class="center_img" style="margin-top:0px;">


</div>
</div>

--- 

<h1 style="position:absolute;top:x;left:75px;right:75px;font-size:50px;">Sletning af features</h1>

</br>
</br>

```python
layer = QgsProject.instance().mapLayersByName("bebyggelse")[0]
provider = layer.dataProvider()

# Sæt laget i edit-mode før vi ændrer data
layer.startEditing()

# Find det feature der skal slettes
for feature in layer.getFeatures():
    if feature['objectid'] == '478699':
  fid = feature.id()
  provider.deleteFeatures([fid])
  break

layer.commitChanges()
layer.stopEditing()
```
<img src="./img/startediting.png" width="450" class="center_img" style="margin-top:10px;">

---
<!-- backgroundColor: #b8063b -->
<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">Lagoprettelse</h1>

## Opret fra bunden et lag af typen polygon
* Benyt den wkt der ligger i ressources.txt som geometri
* Opret tre attributter, og tildel værdier til dem

* Eksporter laget, så det gemmes på din computer som geojson

---
<!-- backgroundColor: #2e495c -->

```python
layer = QgsVectorLayer('Polygon?crs=EPSG:25832', 'Polygon Layer', 'memory')
QgsProject.instance().addMapLayer(layer)

provider = layer.dataProvider()
fields = QgsFields()
fields.append(QgsField('id', QVariant.Int))
fields.append(QgsField('name', QVariant.String))
fields.append(QgsField('type', QVariant.String))
provider.addAttributes(fields)
layer.updateFields()

feature = QgsFeature()
feature.setGeometry(QgsGeometry.fromWkt('POLYGON((...))'))
feature.setAttributes([1, 'test', 'Polygon'])

provider.addFeature(feature)
layer.updateExtents()
```


---
<!-- backgroundColor: #397c67 -->

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:50px;">Styling og labels</h1>

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Intro og disclaimer</h1>

Styling i QGIS kan hurtigt blive voldsomt avanceret, og vi kommer ikke til meget mere end lige ridse i overfladen i dag.
<img src="./img/styling.png" width="450" class="center_img" style="margin-top:10px;">

Det er utroligt meget nemmere at danne en QML fil til sit script i ro og mag, og så lægge den på.

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Styling dialogerne</h1>

<img src="./img/styling_dialog.png" width="950" class="center_img" style="margin-top:10px;">

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Undersøg et layer style</h1>

Et layer har pr. default en renderer når den lægges til TOC. Denne kan vi se hvordan er bygget op.

```python
  layer = QgsProject.instance().mapLayersByName("vejmidte")[0]
  renderer = layer.renderer()
  print(renderer.dump())

```
https://qgis.org/pyqgis/3.40/core/QgsFeatureRenderer.html

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Grundigere undersøgelse (1/3)</h1>

```python
# Del 1: Single symbol
layer_name = "skov"
layers = QgsProject.instance().mapLayersByName(layer_name)

  if renderer.type() == 'singleSymbol':
    symbol = renderer.symbol()
    print("Single symbol layer style:")
    for symbol_layer in symbol.symbolLayers():
      print(f"  Symbol layer type: {symbol_layer.layerType()}")
      print(f"  Properties: {symbol_layer.properties()}")
  else:
    print(f"Renderer type: {renderer.type()}")
```

---


```python
# Del 2: Categorized symbol
layer_name = "skov"
layers = QgsProject.instance().mapLayersByName(layer_name)

  if renderer.type() == 'categorizedSymbol':
    print("Categorized symbol layer style:")
    for category in renderer.categories():
      print(f"  Value: {category.value()}, Label: {category.label()}")
      symbol = category.symbol()
      for symbol_layer in symbol.symbolLayers():
        print(f"    Symbol layer type: {symbol_layer.layerType()}")
        print(f"    Properties: {symbol_layer.properties()}")
  else:
    print(f"Renderer type: {renderer.type()}")
```

---


```python
# Del 3: Graduated symbol
layer_name = "skov"
layers = QgsProject.instance().mapLayersByName(layer_name)

  if renderer.type() == 'graduatedSymbol':
    print("Graduated symbol layer style:")
    for range_ in renderer.ranges():
      print(f"  Range: {range_.lowerValue()} - {range_.upperValue()}, Label: {range_.label()}")
      symbol = range_.symbol()
      for symbol_layer in symbol.symbolLayers():
        print(f"    Symbol layer type: {symbol_layer.layerType()}")
        print(f"    Properties: {symbol_layer.properties()}")
  else:
    print(f"Renderer type: {renderer.type()}")
```
---



<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Single style</h1>

Hvis vi skal lave en 'single symbol' stil til et linjelag, så bruger vi QgsLineSymbol.createSimple

```python
  layer = QgsProject.instance().mapLayersByName("navngivenvej")[0]
  symbol = QgsLineSymbol.createSimple({'color': 'red', 'width': '0.5'})
  renderer = QgsSingleSymbolRenderer(symbol)
  layer.setRenderer(renderer)

  layer.triggerRepaint()
```
https://qgis.org/pyqgis/3.40/core/QgsLineSymbol.html

---


<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Symboltyper</h1>

QGIS 'smager' på laget, og finder ud fra geometrien ud af hvad det er for at lag, hvis vi bruger 'defaultSymbol' - Dette er det samme der sker når et lag læses ind. Her er det kun farven der sættes. 

Hvsi vi vil grundigere til værks, så skal vi bruge de underliigende typer :

https://qgis.org/pyqgis/3.40/core/QgsMarkerSymbol.html
https://qgis.org/pyqgis/3.40/core/QgsLineSymbol.html
https://qgis.org/pyqgis/3.40/core/QgsFillSymbol.html

---

```python
symbol = QgsLineSymbol.createSimple({'color': 'red', 'width': '0.8'})

symbol = QgsFillSymbol.createSimple({
    'color': 'lightblue',
    'outline_color': 'darkblue',
    'outline_width': '0.5',
    'style': 'solid'
})
symbol = QgsMarkerSymbol.createSimple({
    'name': 'circle',
    'color': 'red',
    'size': '3',
    'outline_color': 'black',
    'outline_width': '0.5'
})
```

---

<!-- backgroundColor: #b8063b -->

Prøv om i kan ændre stylingen på et af de lag i projektet der benytter 'single symbol' visning.

---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Løsning</h1>

```python

layer = QgsProject.instance().mapLayersByName("skov")[0]
symbol = QgsFillSymbol.createSimple({
    'color': 'pink',
    'outline_color': 'gold',
    'outline_width': '0.5',
    'style': 'solid'
})
renderer = QgsSingleSymbolRenderer(symbol)
layer.setRenderer(renderer)

layer.triggerRepaint()

```

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Kategoriseret style</h1>

En kategoriseret style benytter en værdi og en label. Dertil skal der laves en style-visning til kategorien - her skal vi bruge en QgsRendererCategory

https://qgis.org/pyqgis/master/core/QgsRendererCategory.html


---


```python
layer = QgsProject.instance().mapLayersByName("layer_name")[0]
attribute_name = "area"
categories = []

# Define symbol for 'land'
land_symbol = QgsSymbol.defaultSymbol(layer.geometryType())
land_symbol.setColor(QColor("green"))
land_category = QgsRendererCategory("land", land_symbol, "Land")
categories.append(land_category)

# Define symbol for 'city'
city_symbol = QgsSymbol.defaultSymbol(layer.geometryType())
city_symbol.setColor(QColor("gray"))
city_category = QgsRendererCategory("city", city_symbol, "City")
categories.append(city_category)

# Create the categorized renderer
renderer = QgsCategorizedSymbolRenderer(attribute_name, categories)

# Apply the renderer to the layer
if renderer is not None:
    layer.setRenderer(renderer)
    layer.triggerRepaint()
```


---

<!-- backgroundColor: #b8063b -->
<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">Styling</h1>

Lav en kategoriseret stilart til vejmidte temaet. Benyt attributten 'trafikart' der har to værdier 'Motorvej' og 'Al færdsel'

---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">Løsning Styling </h1>

```python
# Del 1: Find lag og start kategorier
layers = QgsProject.instance().mapLayersByName("vejmidte")
if not layers:
  # Guard clause: stop tidligt hvis laget ikke findes i projektet
    print("Lag 'vejmidte' blev ikke fundet.")
else:
  # mapLayersByName returnerer en liste, derfor tager vi første match
    layer = layers[0]
  # Attributten der styrer kategoriseringen
    field_name = 'trafikart'
  # Her samler vi alle QgsRendererCategory-objekter
    categories = []
```
---

```python
# Del 2: Definer kategorier
# Kategori for features hvor trafikart == 'Motorvej'
symbol_motorvej = QgsLineSymbol.createSimple({'color': 'red', 'width': '0.8'})
category_motorvej = QgsRendererCategory('Motorvej', symbol_motorvej, 'Motorvej')
categories.append(category_motorvej)

# Kategori for features hvor trafikart == 'Al færdsel'
symbol_alfaerdsel = QgsLineSymbol.createSimple({'color': 'blue', 'width': '0.6'})
category_alfaerdsel = QgsRendererCategory('Al færdsel', symbol_alfaerdsel, 'Al færdsel')
categories.append(category_alfaerdsel)
```

---

```python
# Del 3: Anvend renderer og opdater visningen
# Knyt kategorierne til attributfeltet
renderer = QgsCategorizedSymbolRenderer(field_name, categories)
layer.setRenderer(renderer)

# Tving kortet til at tegne laget igen med den nye stil
layer.triggerRepaint()

# Samlet version (hvis du vil køre det på én gang):
# put del 1, 2 og 3 i samme else:-blok
```


---

<!-- backgroundColor: #397c67 -->

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:50px;">Print og printcomposeren </h1>

---
<!-- backgroundColor: #2e495c -->

I princippet kan vi bygge et printlayout op gennem kode, på samme måde som vi ville gøre manuelt. 

Vi dropper elementer ind i kortet, og fortæller koden hvor det skal placeres på canvas, og hvilken størrelse elementet skal have.

Derefter har vi adgang til properties på elementerne, så vi kan få dem til at se ud som vi vil.

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Printlayouts og manager</h1>

Først skal vi gennem projektet og finde de printlayouts der allerede eksisterer 


```python
project = QgsProject.instance()
layout_manager = project.layoutManager()
```
https://qgis.org/pyqgis/3.40/core/QgsLayoutManager.html#qgis.core.QgsLayoutManager

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Eksisterende layouts</h1>

```python
layouts = layout_manager.printLayouts()
for layout in layouts:
    print(f"Layoutnavn: {layout.name()}")
```

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Print et layout ud</h1>

```python
project = QgsProject().instance()

layout = project.layoutManager().layoutByName('Oversigt')
path = "c:/temp/print.png"

exporter = QgsLayoutExporter(layout)
settings = QgsLayoutExporter.ImageExportSettings()
result = exporter.exportToImage(path, settings)
```
https://qgis.org/pyqgis/3.40/core/QgsLayoutExporter.html

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Layout fra template fil ?</h1>

```python
template_path = "/path/to/template.qpt"

layout = QgsPrintLayout(project)
layout.initializeDefaults()

doc = QDomDocument()
with open(template_path, 'r') as f:
    doc.setContent(f.read())

layout.loadFromTemplate(doc, QgsReadWriteContext())

```

---

```python
layout.setName("MyPrint")
manager = project.layoutManager()
manager.addLayout(layout)

map_item = layout.itemById("Map")
if isinstance(map_item, QgsLayoutItemMap):
    map_item.zoomToExtent(project.extent())

exporter = QgsLayoutExporter(layout)
pdf_path = "/path/to/output.pdf"
exporter.exportToPdf(pdf_path, QgsLayoutExporter.PdfExportSettings())

```
---
<!-- backgroundColor: #b8063b -->

Der ligger i projektet en print-template der hedder 'Oversigt'
Prøv om i kan lave et print med den og gem som billede... 

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Løsning print</h1>

```python
project = QgsProject().instance()
layout = project.layoutManager().layoutByName('Oversigt')

fileName = "c:/temp/myprint.png"
exporter = QgsLayoutExporter(layout)
settings = QgsLayoutExporter.ImageExportSettings()
result = exporter.exportToImage(fileName, settings)
```

---
<!-- backgroundColor: #397c67 -->

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:50px;">Processing toolboxen</h1>

---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Processing tools</h1>

<div class="container">
<div class="col_tight" >

<img src="./img/buffer.png" width="500" class="center_img" style="margin-top:60px;">

</div>
<div class="col_tight">

<img src="./img/python_command.png" width="300" class="center_img" style="margin-top:60px;">

<br/>


```python

processing.run("native:buffer", 
  {
    'INPUT':'C:/Septima/pyqgis_kursus/project/data/bebyggelse.geojson',
    'DISTANCE':100,
    'SEGMENTS':5,
    'END_CAP_STYLE':0,
    'JOIN_STYLE':0,
    'MITER_LIMIT':2,
    'DISSOLVE':False,
    'SEPARATE_DISJOINT':False
    ,'OUTPUT':'TEMPORARY_OUTPUT'
  }
)

  ```



</div>
</div>

---





<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Kald fra python-script</h1>

<div class="container">
<div class="col_tight" >

Du får ingen fancy progressbar m.m. - her er det ren eksekvering.

Du skal gemme resultatet i en variabel, og selv lægge laget til.

Resultatet er en dictionary med outputs (der kan være flere resultater fra et værktøj)


</div>
<div class="col_tight">


```python

layer = processing.run("native:buffer", 
  {
    'INPUT':'C:/Septima/pyqgis_kursus/project/data/bebyggelse.geojson',
    'DISTANCE':100,
    'SEGMENTS':5,
    'END_CAP_STYLE':0,
    'JOIN_STYLE':0,
    'MITER_LIMIT':2,
    'DISSOLVE':False,
    'SEPARATE_DISJOINT':False
    ,'OUTPUT':'TEMPORARY_OUTPUT'
  }
)

QgsProject.instance().addMapLayer(layer['OUTPUT'])

```



</div>
</div>

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Modeller</h1>

Hvis du har oprettet modeller i QGIS, kan de køres på samme måde som øvrige tool:

```python
params = {
    'INPUT': '/path/to/input/layer.shp',
    'BUFFER': 10,
    'OUTPUT': '/path/to/output.shp'
}

result = processing.run("model:dit_modelnavn", params)
```

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Modeller som filer ?</h1>

```python
model_path = "/path/to/your_model.model3"
model = QgsProcessingModelAlgorithm()
model.loadFromFile(model_path)

QgsApplication.processingRegistry().addAlgorithm(model)

params = {
    'INPUT': '/path/to/input.shp',
    'OUTPUT': '/path/to/output.shp'
}
result = processing.run(model.id(), params)

```

---
<!-- backgroundColor: #b8063b -->

Vindmølle-laget vi har hentet fra Plandata.dk er landsdækkende.
Lav et script der benytter processing værktøjet 'CLIP' til at reducere features til vores kommunegrænse.
Beregn herefter en 500m buffer på clip resultatet via værktøjet 'BUFFER'

Brug GUI'en til at danne koden for dig, og sæt den ind i dit script.

- Lad scriptet lægge det nye lag til projektet efterfølgende, giv det et sigende navn...

Hvis du er hurtig, prøv at byg det som model og kør den via PyQGIS

---
<!-- backgroundColor: #2e495c -->

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Løsning - processing</h1>
<br/>
<br/>

```python
clip_layer = processing.run("native:clip",
 {
  'INPUT':'WFS://https://gisp.bpst.dk/ve/wfs?request=GetFeature&typename=ve:vindmoeller',
  'OVERLAY':'C:/Septima/pyqgis_kursus/project/kommune.geojson',
  'OUTPUT':'TEMPORARY_OUTPUT'})
buffer_layer = processing.run("native:buffer",
 {
  'INPUT':clip_layer['OUTPUT'],
  'DISTANCE':500,
  'SEGMENTS':5,
  'END_CAP_STYLE':0,
  'JOIN_STYLE':0,
  'MITER_LIMIT':2,
  'DISSOLVE':False,
  'SEPARATE_DISJOINT':False,
  'OUTPUT':'TEMPORARY_OUTPUT'})

QgsProject.instance().addMapLayer(buffer_layer['OUTPUT'])
```

---


<!-- backgroundColor: #397c67 -->

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:50px;">Selvstændige scripts</h1>


---
<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Afvikling udenfor QGIS </h1>

* Det er muligt at afvikle sine python-scripts mod det Python-Miljø som QGIS har i sin distro. 

* Det er kringlet at få lavet et Python env. der gør det muligt at køre QGIS scripts, men det kan lade sig gøre...

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">python-qgis.bat </h1>

<div class="container">
<div class="col_tight" >

- Afhængigt af installationen af QGIS, ligger denne fil enten i qgis/bin eller i OSGEO4W/bin
- Er du på en LTR distribution, hedder filen desuden også '-ltr' bagefter.
- Her kan python filer køres mod QGIS python... 

</div>
<div class="col_tight">


<img src="./img/qgis-python.png" width="600" class="center_img" style="margin-top:60px;">

</div>
</div>

--- 
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Imports</h1>


<div class="container">
<div class="col_tight" >

Python-konsollen og editor er 'supercharged' ved opstart af QGIS - alle imports er foretaget for os.

Hvis vi skal lave scripts der skal kunne køre udenfor QGIS, skal vi selv stå for disse imports.

</div>
<div class="col_tight">


<img src="./img/imports.png" width="600" class="center_img" style="margin-top:60px;">

</div>
</div>

---


<!-- backgroundColor: #2e495c -->

Jeg har lavet filen scripts\standalone.py til jer - den indeholder følgende :

```python
from qgis.core import QgsApplication, Qgis
import sys
import os

## Denne skal sættes til den rigtige sti til QGIS installation
qgisPrefixPath = "C:/OSGeo4W/apps/qgis-ltr/"

QgsApplication.setPrefixPath(qgisPrefixPath, True)
qgs = QgsApplication([], False)
qgs.initQgis()

sys.path.append(f"{qgisPrefixPath}/python/plugins")
import processing
from processing.core.Processing import Processing
from processing.script.ScriptUtils import *
Processing.initialize()
```
---

<!-- backgroundColor: #b8063b -->
<h1 style="position:absolute;top:100px;left:75px;right:75px;font-size:50px;">Lad os til sidst prøve at bygge et script... </h1>

Med udgangspunkt i standalone.py, byg et flow der :

* Åbner en af filerne fra datamappen og indlæser som lag i scriptet
* Laver 'et eller andet sjovt' fra processing toolbaren 
* Skriver resultatet til en fil

---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Hjemmeopgave</h1>

På Dawa kan du få en fil med adresser for en kommune som csv:

https://api.dataforsyningen.dk/adresser?kommunekode=0326&format=csv

* Byg et PyQGIS-script, der henter denne fil, og laver den om til et validt QGIS-lag med geometri og attributter.
(QGIS kan gøre det selv, men jeg ser gerne I gør det 'i hånden': opret et tomt lag, opret relevante attributter og geometri, og læg data i.)

Data gemmes som en geopackage til sidst... 

---



<!-- backgroundColor: #2e495c -->
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Tak for i dag...</h1>

<div class="container">
<div class="col_tight" style="margin-top:60px;">

* Nu kan I begynde at eksperimentere med små scripts
* I har fået indblik i hvordan PyQGIS er bygget op af OOP classes
* Fået en god ide om hvordan dokumentationen læses

</div>
<div class="col_tight">

<img src="./img/programmer.jpg" width="500" style="margin-top:0px;">

</div>
</div>


---

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:80px;">Avanceret print</h1>
---

---


```python
project = QgsProject.instance()
manager = project.layoutManager()
layout = QgsPrintLayout(project)
layoutName = "TestLayout" 
layouts_list = manager.printLayouts()

for layout in layouts_list:
    if layout.name() == layoutName:
        manager.removeLayout(layout)

layout = QgsPrintLayout(project)
layout.initializeDefaults()
layout.setName(layoutName)
manager.addLayout(layout)
```
---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Tilføje et kort-element til layoutet</h1>

```python
map = QgsLayoutItemMap(layout)

map.attemptSetSceneRect(QRectF(20, 20, 200, 100))

rectangle = QgsRectangle(492679.7, 6108883.58, 549488.76, 6137370.13)

map.setExtent(rectangle)
layout.addLayoutItem(map)

```

--- 
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Centerpunkt og skala i stedet for extent?</h1>

```python
map = QgsLayoutItemMap(layout)
map.attemptSetSceneRect(QRectF(20, 20, 200, 100))
center_x = 520000
center_y = 6120000
center = QgsPointXY(center_x, center_y)
scale = 50000
width_mm = 200
height_mm = 100
width_mapunits = (width_mm * scale) / 2000
height_mapunits = (height_mm * scale) / 1000
xmin = center_x - width_mapunits / 2
xmax = center_x + width_mapunits / 2
ymin = center_y - height_mapunits / 2
ymax = center_y + height_mapunits / 2
```

---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Scalebar </h1>

```python
scaleBar = QgsLayoutItemScaleBar(layout)
scaleBar.setLinkedMap(map)
scaleBar.setStyle('Single Box')
scaleBar.setUnits(QgsUnitTypes.DistanceUnit.DistanceKilometers)
scaleBar.setSegmentSizeMode(1)
scaleBar.setNumberOfSegmentsLeft(0)
scaleBar.setNumberOfSegments(3)
scaleBar.setMinimumBarWidth(10)
scaleBar.setMaximumBarWidth(50) 
scaleBar.setUnitLabel("KM")
scaleBar.setMinimumSize(QgsLayoutSize(90, 10, QgsUnitTypes.LayoutMillimeters)) 
scaleBar.setHeight(2)
scaleBar.setPos(20, 155)
layout.addItem(scaleBar)
```
---
<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Signaturforklaring </h1>

```python
legend = QgsLayoutItemLegend(layout)
legend.setAutoUpdateModel(False)
legend.adjustBoxSize()
legend.setId('Legend')
layout.addLayoutItem(legend)
legend.setFrameEnabled(True)
legend.setFrameStrokeWidth(QgsLayoutMeasurement(0.3))
legend.setTitle('Legende')
legend.attemptMove(QgsLayoutPoint(240, 10, QgsUnitTypes.LayoutMillimeters))
legend.attemptResize(QgsLayoutSize(104, 40, QgsUnitTypes.LayoutMillimeters))
```


---

<h1 style="position:absolute;top:300px;left:75px;right:75px;font-size:80px;">Gradueret styling og labels</h1>

---


<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Graduated style</h1>

En gradueret style, skal bruge lidt mere - her skal vi lave ranges.

En style indeholder :

* Nedre grænse
* Øvre grænse
* symbol
* label 

https://qgis.org/pyqgis/master/core/QgsGraduatedSymbolRenderer.html
https://qgis.org/pyqgis/3.40/core/QgsRendererRange.html

---

```python
    symbol_under = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol_under.setColor(QColor("lightgreen"))

    range_under = QgsRendererRange(
        0,                     # nederste grænse
        500,                   # øverste grænse (ikke medtagende)
        symbol_under,
        "Under 500"
    )
    ranges = [range_under]
    renderer = QgsGraduatedSymbolRenderer(
        attribute_name,
        ranges
    )
    layer.setRenderer(renderer)
    layer.triggerRepaint()
```
---

<h1 style="position:absolute;top:80px;left:75px;right:75px;font-size:50px;">Labels</h1>

Labels fra PyQgis, kan også blive sindssygt kompliceret - der er virkelig mange ting man kan sætte i QGIS label dialogen...

Her skal vi i første omgang bruge et QgsPalLayerSettings objekt

https://qgis.org/pyqgis/3.40/core/QgsPalLayerSettings.html

"Contains settings for how a map layer will be labeled."

---
```python

layer = QgsProject.instance().mapLayersByName("kommune")[0]

# Opret label settings
label_settings = QgsPalLayerSettings()
label_settings.fieldName = 'navn'
label_settings.placement = QgsPalLayerSettings.OverPoint

# Tilknyt labeling
labeling = QgsVectorLayerSimpleLabeling(label_settings)
layer.setLabeling(labeling)
layer.setLabelsEnabled(True)

# Opdater kortet
layer.triggerRepaint()

print(f"Labels sat på laget '{layer.name()}' med feltet 'navn'.")
```
