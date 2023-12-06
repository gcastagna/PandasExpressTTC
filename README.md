# pandaspickledpiperpeanuts

Introduction:
This Repository is dedicated to a project related to performance assessment of TTC bus delays. In this project, different data was collected and concatenated to form a big data-frame. The data was collected from several sources as depicted in the project’s workflow and three phases of Data Analytics Visualization, Geospatial Visualizations and Predictive model training were performed on the dataset.

![workflow2](https://github.com/gcastagna/PandasExpressTTC/assets/144471904/e996a241-5d95-48d9-b7c9-c82555d72156)


The project aimed to answer the following questions:
1-What was the overall performance of TTC bus service, and how they could improve their performance
2- How are the bus delays distributed in the city and their correlation with location, weather, land values, etc. 
3- Train a predictive model to predict the type of future delays by having access to some features related to the delays


**_Folders_**
_DataProcessingCleaned-1Dec2023_ – This foDataProcessingCleaned-1Dec2023 – This folder contains the workflow done to import, clean, concatenate and merge datasets that were used for the rest of this project. This folder is the heart of the dataset, and contains 5 subfolders, each with its own readme file:
_1)	Clean Bus Delays
2)	Clean Intersection Data
3)	RapidFuzz Delays to Stops
4)	Read and Clean Climate Data
5)	Merge Delays with Climate Data_
_TTC Route and Stop Data_ – This folder contains TTC bus route polylines and the Route and Stop text files
_Toronto Geospatial Data_ - This folder contains Toronto area shape files, as well as condo price data for the city. 
PredictiveModel – This folder contains the notebook used to create the machine-learning RandomForest model to predict the type of delay a user will experience. The folder also contains the RandomForest and analysis data that was used to train the model. 


**Notebooks**
_Geospatial playground _– This notebook was used to create the geospatial visualizations shown in the medium article, including delays by route, area, precipitation, and condo pricing. The notebook used data from the ‘TTC Route and Stop Data’ and ‘Toronto Geospatial Data’ folders, as well as the output from the DataProcessingCleaned folder. 
_DataAnalytics_ – This notebook was used to create all the analytical visualizations shown in the article, such as delays by month/year, category, issue and precipitation type. The notebook used data from the ‘Clean Bus Delays’ and ‘Merge Delays with Climate Data’ subfolders from the ‘DataProcessingCleaned-1Dec2023’ folder


**Medium Article Link** - 
