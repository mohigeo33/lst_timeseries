# Land surface temperature dynamics in a changing landscape: A time series analysis of Landsat imagery in Google Earth Engine

## 1. About the study
This study investigates the spatiotemporal patterns of land surface temperature (LST) and its relationship with land use/land cover (LULC) changes in an urban setting. The main objectives were to analyse seasonal variability, LST trends, and the response of LST to different LULC types in identified hotspots, including the correlation between them. A mixed-methods approach was employed, utilising remote sensing techniques and Landsat imagery to collect data. The sample included 462 images of the study area taken from 2000 to 2021, which were analysed using the cloud-based platform Google Earth Engine (GEE). The findings revealed significant seasonal variability in LST and a visual connection between LST and LULC changes in specific hotspots. No long-term trends in LST were observed, despite fluctuations. A strong positive correlation between built-up areas and LST was identified, while negative correlations were found between LST and water bodies and vegetation. These results support the notion that urbanisation and LULC changes are closely related to LST variations, emphasising the importance of considering local context and specific LULC changes when examining LST dynamics. The findings can inform urban planning and management strategies, such as incorporating green and blue infrastructure to moderate LST values and improve the urban environment. This study provides valuable insights into LST dynamics and the relationship between LST and LULC changes, with potential implications for urban planners, policymakers, and researchers working towards creating more sustainable and resilient urban environments.

## 2. Notebook files and their description
a) LST_Calculation.ipynb: Image pre-processing, Spectral indices calculation, LST estimation and statistical data extraction

b) Statistical_analysis.ipynb: Descriptive statistics, trend and correlation analysis

## 3. Required packages
### 3.1 For LST estimation and data extraction
import os

import sys

import ee

import geemap

import geopandas as gpd

import pandas as pd

from tqdm import tqdm

import math
### 3.2 For statistical analysis
import os

import pandas as pd

import matplotlib as mpl

import matplotlib.pyplot as plt

import statistics

import numpy as np

import seaborn as sns

import math

import altair as alt

import altair_transform

from scipy.stats import shapiro 

from scipy.stats import lognorm

from scipy.stats import kstest

from scipy.stats import norm

from sklearn.metrics import r2_score
## 4. Files needed to run the code externally
a) AOI.zip: the shapefile for area of interest

b) CSV files.zip: the csv files required for statistical analysis

## 5. Remarks
This code is created for research purposes. Upon use please provide appropriate references.

## test for interactive charts
Check out this [interactive visualization](https://mohigeo33.github.io/lst_timeseries/cloud_cover.html).

