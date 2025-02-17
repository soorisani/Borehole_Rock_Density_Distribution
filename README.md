# Geological Borehole Data Analysis for Rock Density and Distribution
# 📝 Table of Contents
- [Project Overview](#Overview)
- [Data Understanding](#data_undestanding)
- [Methods & Techniques](#Methods)
- [Libraries & Tools Used](#libs)
- [Technologies](#techs)
- [Project Implementation](#Implementation)
- [Results & Insights](#Insights)
- [Sample of Visualization/Result](#sample)
- [Conclusion & Future Work](#Conclusion)
- [Status](#status)
- [Setup](#setup)





## 1. Project Overview: <a name = "Overview"></a>
This project focuses on analyzing borehole geological data to identify rock density distributions and visualize subsurface structures. The goal is to utilize Python for data processing, visualization, and geospatial analysis, making the results useful for geological studies, resource exploration, and engineering applications. 

## 2. Data Understanding: <a name="data_undestanding"></a>
The dataset used in this project consists of borehole data with the following attributes: 
- **Depth (m)**: The vertical depth of the borehole measurement.
- **Rock Type**: The lithology of the rock at a specific depth.
- **Density (g/cm³)**: The density of the rock at each depth. The dataset is stored in CSV format and processed using Python. 

## 3. Methods & Techniques <a name = "Methods"></a>
### 3.1 Data Acquisition & Cleaning 
- Load data from a CSV file using
- Handle missing values and clean the dataset.
- Filter and categorize rock types based on density.
  
### 3.2 Data Analysis & Processing 
- Compute summary statistics (mean, median, standard deviation) using pandas.
- Identify high-density and low-density rock distributions.
- Analyze lithological trends with depth.
  
### 3.3 Visualization & Mapping
- Borehole lithology bar charts **using matplotlib**. 
- Create **3D geological models** using mpl_toolkits.mplot3d**.
- Overlay boreholegeological mapgeological map using **geopandas**.


## 4. Libraries & Tools Used: <a name = "libs"></a>
The following Python libraries 
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- Matplotlib: Working with [mplot3dolkits.mplot3d](https://matplotlib.org/stable/api/toolkits/mplot3d.html)
- [Geopandas](https://geopandas.org/en/stable/docs/user_guide/data_structures.html)  
- Rasterio: Working with [raster-based geompl_toolkits](https://pythonhosted.org/rasterstats/)

## 5. Project Implementation <a name = "Implementation"></a>
### 5.1 Data Loading & Preprocessing 
```
 import pandas as pd df = pd.read_csv("borehole_data.csv") print(df.head()) 
```
### 5.2 Borehole Lithology Visualization
```
import matplotlib.pyplot as plt
plt.bar(df["Depth (m)"], df["Density (g/cm³)"], color="brown") 
plt.xlabel("Depth (m)") 
plt.ylabel("Density (g/cm³)") 
plt.title("Borehole Lithology Distribution") 
plt.show() 
```

### 5.3 Geospatial Analysis with GeoPandas
```
import geopandas as gpd
gdf = gpd.read_file("geology_map.shp") 
gdf.plot(figsize=(10, 6)) 
plt.title("Geological Map Overlay") 
plt.show() 
```

### 5.4 3D Topographic Visualization
```
import numpy as np from mpl_toolkits.mplot3d
import Axes3D 
fig = plt.figure() 
ax = fig.add_subplot(111, projection="3d") 
x = np.linspace(0, 10, 100) 
y = np.linspace(0, 10, 100) 
X, Y = np.meshgrid(x, y) 
Z = np.sin(X) + np.cos(Y) 
ax.plot_surface(X, Y, Z, cmap="terrain") 
plt.show() 
```

## 6. Results & Insights <a name = "Insights"></a>
Identified rock types with high and low density distributions.
Successfully visualized lithology changes along depth.
Mapped geological structures using spatial data.

## 7. Conclusion & Future Work <a name = "Conclusion"></a>
This project demonstrates how Python can be leveraged for geological data analysis and visualization. Future improvements may include integrating machine learning to classify rock types based on additional geochemical and geophysical parameters.

## 8. Sample of Visualization/Result  <a name ="sample"></a>
For viewing a sample of result please check [here](https://github.com/soorisani/Borehole_Rock_Density_Distribution/commit/acacf0a6650e39526e8c05e52b96fc9c01854176)

## 9. Portfolio Contribution
### 9.1 Skills Demonstrated: 
Data wrangling, geospatial analysis, 3D visualization.

### 9.2 Technologies: <a name = "techs"></a>
- Python, 
- Pandas,
- Matplotlib,
- GeoPandas.

## 10. Potential Applications: 
Resource exploration, geotechnical engineering, geological mapping.

## 11. Status <a name="status"><a/>
Compeleted!
## 12. Setup <a name="setup"><a/>
> [!Tip]
> For setup follow steps [here](https://github.com/soorisani/Borehole_Rock_Density_Distribution/blob/main/Set%20Up.md) 


