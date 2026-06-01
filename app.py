import numpy as np # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

# Load the dataset
df=pd.read_csv('Data/UpdatedResumeDataSet.csv')
print(df.head(5))
print(df.shape)

print(df['Category'].value_counts())
