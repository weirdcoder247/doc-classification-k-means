# import packages
import pandas as pd
import numpy as np
import os
import re
import nltk

# Set working directory
os.getcwd()
os.chdir("C:\\Repositories\\doc-classification-k-means\\02_data")

# import data
data = pd.read_csv("abcnews-date-text.csv")
