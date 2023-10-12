import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, chi2, gaussian_kde
import seaborn as sns

# do not modify this cell
filename = 'power_consumption.csv'
df = pd.read_csv(filename)
df.head()

regions = list(df.region.unique())

# selection of a region
region = "Bretagne"
df_region = df[df.region == region]

moyenne = df_region.consumption.sum()/df_region.consumption.count()
print(f"moyenne: {moyenne}")
variance = sum([(x-moyenne)**2 for x in df_region.consumption])/(df_region.consumption.count()-1)
print(f"variance: {variance}")

