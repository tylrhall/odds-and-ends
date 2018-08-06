#This is code to plot histograms of assay data, grouped by lithology, weathering, or ore type.
import pandas as pd
import matplotlib.pylab as plt

#read the data
df = pd.read_csv('merged.csv')

#change data types.
df['stratigraphy'] = df['stratigraphy'].astype('category')
df['oretype'] = df['oretype'].astype('int64')
df['weathering'] = df['weathering'].astype('int64')
df['assay'] = df['assay'].astype('float64')

#plot histograms, in this case, assay values for each lithology. Grade minimum is zero, grade maximum is 1.0 (0% to 100%)
df.hist(column='assay', by='stratigraphy', bins = 20, xlabelsize = 6, range=(0, 1.0))
plt.show()
