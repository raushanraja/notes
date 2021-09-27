Unit 2. GIS

|Unit 2.|GIS|
|-|-|
| Raushan|21/02/2020 19:45|
* * *

- [1. GIS (Geographic Information System)](#1-gis-geographic-information-system)
- [2. Components of a GIS](#2-components-of-a-gis)
  - [2.1 Hardware](#21-hardware)
  - [2.2 Software](#22-software)
  - [2.3 People](#23-people)
  - [2.4 Infrastructure](#24-infrastructure)
  - [2.5 Data](#25-data)
    - [2.5.1 Geospatial Data](#251-geospatial-data)
    - [2.5.2 Attribute Data](#252-attribute-data)
- [3. GIS Operation](#3-gis-operation)
  - [3.1 Spatial Data Input](#31-spatial-data-input)
  - [3.2 Attribute Data Management](#32-attribute-data-management)
  - [3.3 Data Display](#33-data-display)
  - [3.4 Data Exploration](#34-data-exploration)
  - [3.5 Data Analysis](#35-data-analysis)
  - [3.6 GIS Modelling](#36-gis-modelling)
- [4. Data Model](#4-data-model)
- [5.1. Raster Data Model](#51-raster-data-model)
- [5.2 Tesselation](#52-tesselation)
  - [5.2.1 Regualr Tesselation](#521-regualr-tesselation)
  - [5.2.2 Irregular Tesselation](#522-irregular-tesselation)
- [6. Geodesy](#6-geodesy)
- [7. Coordinate System:](#7-coordinate-system)
  - [7.1 Geographic cordinate system](#71-geographic-cordinate-system)
  - [7.2 Cartesian Coordinate System](#72-cartesian-coordinate-system)
- [8. Spatial Data](#8-spatial-data)
- [9. Map](#9-map)
  - [9.1 Spatial Entities](#91-spatial-entities)
    - [9.1.1 Point](#911-point)
    - [9.1.2 Line](#912-line)
    - [9.1.3 Area / Polygon](#913-area--polygon)
  - [9.2 Generalization](#92-generalization)
- [10. Map Projdection](#10-map-projdection)
  
<br/>

### 1. GIS (Geographic Information System)
+ `definition`: 
    + It is a set of tools for 
        + collecting
        + storing
        + retriving at will
        + transforming
        + and displaying
        
    spatial data  from the real world for a particular set of purpose.
+ `Geographic information`: Information about places on earth's surface.
+ Technology ncludes:
    + GIS
    + GPS &
    + Remote Sensing

### 2. Components of a GIS
+ Hardware
+ Software
+ People
+ Insfrastructure
+ Data

#### 2.1 Hardware
+ GIS runs on whole range of computer systems,
+ Ranging from Supercomputers to handheld devices.
+ Essential elements for effective GIS operation:
    + Preprocessor
    + Sufficient main and secondary storage
    + Quality display
    + Range of IO devices

#### 2.2 Software
+ Software allows and supports important task such as
    + Data input
    + Efficient data storage
    + Data transformation
    + Analysis
    + ANd appropriate output
+ Sofware can be as simple as a browser or a complete package from GIS verdor

#### 2.3 People
+ It referes to professionals & users
+ Who define the purpose and objective
+ And provice the reason and justification for using GIS.

#### 2.4 Infrastructure
+ It refers to 
    + physical
    + origanizational
    + administrative &
    + cultural environmnet
that supports GIS operation
+ It includes:
    + requisite skills
    + data standards
    + data clearinghouse &
    + general organizational patterns.

#### 2.5 Data
+ GIS handles spatial(geographical data).
+ These data are charactrized by information about
    + position
    + connections with feature and 
    + details of non-spatial charactristics
+ It can range from megebyte to petabyte.
+ Types:
    + Geospatial Data
    + Attribute Data

##### 2.5.1 Geospatial Data
+ These data describes locations of feature, which may be discrete or continuous.
+ `Discrete Feature` : 
    + Those features that can be distinguised individually.
    + Do not exists between observation.
    + Usages vector data model
    + Example: points(well), line(road), area(land use type).
+ `Continuous Feature` :
    + Exists spatially beween two observation
    + Usages raster data model
    + Example: Elevation, Precipitaion
+ The location of spatial features on earth's surface is based on geographic coordinate system with
    + `longitude`
    + `latitude`
+ The location of map features is based on plane coordinate system with x,y coordinates.

##### 2.5.2 Attribute Data
+ Attribute data describes the characteristics of spatial features.
+ For `raster data`, each cell has a value that represents attribute of spatial feature at that location.
+ For `vector data`, the amount of attribute associated with a spatial feature can vary.
    + Eg.: A road may have `length`, `speed limit` as attribute, where as a soil polygon have a dozens of attributes.



### 3. GIS Operation
#### 3.1 Spatial Data Input
    + Data acquisition
    + New data creation
    + Data edition
    + Data entry
    + Geometric Transformation 
    + Projection & Re-projection
#### 3.2 Attribute Data Management
    + Data entry & verification
    + Database management
    + Attribute data Manipulation
#### 3.3 Data Display
    + Map design and making
    + Cartographic symbol
#### 3.4 Data Exploration
    + Using:
        + Geospatial data query
        + Attribute data query
        + data visualization
#### 3.5 Data Analysis
    + Vector data analysis
    + Raster data analysis
    + path analysis
    + Geocoding
    + Spatial interpolation
    + Terrain Mapping
    + Viewshed (area of land visible from one or more observation points) and watershed (derive tropologica features such as flow direction, stream networks and boundaries)
#### 3.6 GIS Modelling
    + It reffers to use of a GIS and functionalities in building model iwhth geospatial data.
    + Model is grouped into four general types:
        + Binary
            + It rely on either vector based or raster based overlay
            + It queries overlay to seperate area based on criteria satisfaction.
        + Index
            + It also rely on overlay
            + It queries overlay to create index and ranks areas based on index value.
        + Regression
            + It also rely on overlay
            + It uasges overlay to analyze relationship between dependent and independent variable
        + Process
            + It usages existing environment process knowledge and qunatified it.
            + Eg.: soil erosion prediction.


### 4. Data Model
+ Data model represents how the data are organized and 
+ How they are used by the GIS.
+ GIS have traditionally used raster or vectors for map.


### 5.1. Raster Data Model
+ This data model is one of a family of tesselattions data model.
+ In this, individual cells are used as building blocks for creating point, line, area, network and surface entities.
+ These data models best represents the continouos spatial feature such as temperature, elevation, precepitation etc.

### 5.2 Tesselation
+ Tesselation is the tiling of suface using one or more geometric shapes with no overlaps and no gaps.
+ Also know as diecrete model, spatial resolution model, tiling or meshes.
+ Types
    + `regular`
        + `square`
        + `hexagonal`
        + `triangular`
    + `irregular`
        + `quadtree`
        + `cadestral zone`
        + `thessien polygon`
#### 5.2.1 Regualr Tesselation
+ The shape and size of all cells in a regular tesselation remains same.
+ Less complex than Irregular tesseltaion
+ It has diasdvantage, as it have less adaptability to spatial phenomena than irrgular tesselation.
+ Types:
    + `Square Cell`
    + `Hexagonal Cell`
    + `Traingular Cell`

#### 5.2.2 Irregular Tesselation
+ It divides the sapce into mutually disjoint cells.
+ The shape and size of cells are not same.
+ More complexity is present.
+ More adaptability towards spatial phenomena.
+ Typically leads to less memory use for storage.
+ Types:
    + `Quadtree`
    + `Cadestral zone`
    + `Thessien  polygon`

### 6. Geodesy
+ Concerned with the determination of the shape and sixe of earth.
+ As well with the elments: `gravity`, `magenatic field` `tides` `polar motion`
+ Relies on two terrestrail movement:
    + `Geomensturaion`: Measurement of earth as whole.
    + `Surveying` : Measurement of individual parts on earth's syrface.

### 7. Coordinate System:
+ A coordinate system is a number set that denotes a specific location within a reference system.
+ Typical coordinates are:
    + Two dimensional system with set(x,y)
    + Three dimensional system with set (x,yz,)
+ Coordinate systems used in GIS:
    + `Geographic coordinate system`
    + `Catesian coordinate system`

#### 7.1 Geographic cordinate system
+ It is three dimensinal positional reference system
+ It gives the position using 
    + `Longitude`
        + The longitude of a point is a horizontal angle measured in plane of equator between plane of meridian and plane of prime meridian.
    + `Latitude`
        + THe latitude of a point is the vertical angle measured at the center of earth between plane of equator and radius drawn to the point.
    + `Ellipsoidal Height`

#### 7.2 Cartesian Coordinate System
+ Named after Rene Descartes
+ Posisition are measured along intersecting plane at 2 or 3 dimension
+ Origin = Intersectiong point of all plane.
+ 2D model is divided into 4 quadrants.


### 8. Spatial Data
+ Sources:
    + Map
    + Land surveying
    + Aerial photograph
    + Satellited Images
    + GPS
+ Data Source based on collection
    + Primary Data: Collected through first hand observation
    + Secondfary Data : Collected by other individual or organization.
+ Modes/Dimension of data
    + `Spatial`
        + Convey the location of feature.
        + Used for data organized and analyzed by location.
    + `Thematic`
        + Convey the characteristic of data.
        + Reffered as attribute data.
        + Used for data organized and analyzed by theme
    + `Temporal`
        + Provides record of when data whas collected.
        + Used for data organized and analyzed by time.

### 9. Map
+ Maps are traditional form of storing, analysing and persenting spatial data.
+ Types:
    + `Thematic Map` : Repsresnts data related to a specific theme. Such as soil, temperature, pressure etc.
    + `Topographic Map` : Represents data relation to combination of different theme. Such as land use and culteral features on same map.
+ Issues in map processing:
    + Purpose of map
    + Scale
    + Features (Spatial Entities)
    + Representation of features (Point, Line, Area)
    + Generalization
    + Map projection
    + Spatial Reference system
    + Annotation of map (legends, text,keys)

#### 9.1 Spatial Entities
+ Map usages points, line and areas to represent a real world feature,
    these points, line and area are known as spatial entities.
+ The method(point/line/area) to represnet a feature will depend on scale used.

##### 9.1.1 Point
+ Points are used to represent smaller freatures,
+ Examples: Postbox, a tree, a well etc.
+ Point obejctes in reality can be in three dimensions also.

##### 9.1.2 Line
+ It is used to represent a feature that is linear in nature.
+ Example: road, electricity line, river etc.
+ It is ordered set of points (x,y) joined togehter.
+ Like points , it can also be in 3 dimension.

##### 9.1.3 Area / Polygon
+ Area is used to reperesent feature such as building, field or lake.
+ These features are very large in scale than point objects.
+ Area usages closed set of lines to represent these features.
+ Area entities  are also called polygons.
+ Types:
    + `Island Polygon`
    + `Adjacent Polygon`
+ A 3D area is surface which is used to represent topographical and non-topographical variable such as pollutant level, population densities.

#### 9.2 Generalization
+ The process of producing a graphic representation of a feature from larger scale to smaller scale.
+ All spatial data is generalization of real world feature.
+ Generalization is done because:
    + It is required
    + or, Because of limitaion in techinical procedure to priduce data
+ A geographic database connot contain perfect descrition, so the data needs to be slected to fit in limited memory availabe.
+ The process consists of three steps:
    + Why to generalize
    + When to genralize
    + How to generalize
        + Simplification
        + Smoothing
        + Aggregation
        + Merging
        + Collapse
        + Refinement
        + Displacement

### 10. Map Projdection
+   Map projection is the process of transformaing the Eeath's spherical surface to plane surface
+ And bridge the gap between two spatial reference system,
+ Map projection try to preserve following protery of real world features:
    + Area
    + Shape
    + Distance
    + Direction
+ Types:
    + Cylendrical
    + Conic
    + Planer

id: 3fdd8dfa20cb489a915b8bc14e62ddff
parent_id: 518c6219f58b4b0d9ea60f9d47a31fb2
created_time: 2020-02-21T14:11:07.675Z
updated_time: 2020-02-22T02:20:00.579Z
is_conflict: 0
latitude: 28.63310000
longitude: 77.22070000
altitude: 0.0000
author: 
source_url: 
is_todo: 0
todo_due: 0
todo_completed: 0
source: joplin-desktop
source_application: net.cozic.joplin-desktop
application_data: 
order: 0
user_created_time: 2020-02-21T14:11:07.675Z
user_updated_time: 2020-02-22T02:20:00.579Z
encryption_cipher_text: 
encryption_applied: 0
markup_language: 1
is_shared: 0
type_: 1