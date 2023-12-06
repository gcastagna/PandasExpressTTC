# CME538 - PandasExpress / TTC Bus Delays

Introduction:
This Repository is created for 'The Big Project' for CME538 - Data Science, to understand the performance assessment of TTC bus delays. In this project, data was collected,  concatenated and cleaned to form a large data frame containing all of the TTC bus delays and their attributes. The data was collected from several sources, such as UofT and TTC, as depicted in the project’s workflow and follows three phases of Data Analytics Visualization, Geospatial Visualizations and Predictive model training performed on the dataset.


![workflow4](https://github.com/gcastagna/PandasExpressTTC/assets/144471904/428a7f50-f6e0-48f7-a51e-c64f1acb539d)




The project aimed to answer the following questions:

1 - What was the overall performance of TTC bus service, and how they could improve their performance?

2 - How are the bus delays distributed in the city and their correlation with location, weather, land values, etc? 

3 - Can we train a predictive model to predict the type of future delays by having access to some features related to the delays?

4 - How can we improve upon our current understanding of TTC delays?


**_Folders_**

_DataProcessingCleaned-1Dec2023_ – This foDataProcessingCleaned-1Dec2023 – This folder contains the workflow done to import, clean, concatenate and merge datasets that were used for the rest of this project. This folder is the heart of the dataset, and contains 5 subfolders, each with its respective readme file:

1)	Clean Bus Delays - Read raw bus data and concatenate it into one clean file.

2)	Clean Intersection Data - Extract geometry and name of city intersections to be integrated into Geopandas database. 
   
3)	RapidFuzz Delays to Stops - Use RapidFuzz to match each unique delay location to a unique stop or intersection location in GeoPandas
   
4)	Read and Clean Climate Data - Concatenate and clean hourly climate data
   
5)	Merge Delays with Climate Data - Bin delays into hourly intervals and merge with climate data from folder 4. 

_TTC Route and Stop Data_ – This folder contains TTC bus route polylines and the Route and Stop text files

_Toronto Geospatial Data_ - This folder contains Toronto area shape files, as well as condo price data for the city. 

_PredictiveModel_ – This folder contains the notebook used to create the machine-learning RandomForest model to predict the type of delay a user will experience. The folder also contains the RandomForest and analysis data that was used to train the model. 


**Notebooks**

_Geospatial playground_ – This notebook was used to create the geospatial visualizations shown in the medium article, including delays by route, area, precipitation, and condo pricing. The notebook used data from the ‘TTC Route and Stop Data’ and ‘Toronto Geospatial Data’ folders, as well as the output from the DataProcessingCleaned folder. 

_DataAnalytics_ – This notebook was used to create all the analytical visualizations shown in the article, such as delays by month/year, category, issue and precipitation type. The notebook used data from the ‘Clean Bus Delays’ and ‘Merge Delays with Climate Data’ subfolders from the ‘DataProcessingCleaned-1Dec2023’ folder


**Medium Article Link** - https://medium.com/@avery.hoffer/predicting-ttc-bus-delays-6926028327fe

**Presentation** - In the repository as 'Presentation.pdf'. This file is our team's final presentation displaying our methods and findings for the project.
