import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sas

df = pd.read_csv('fatal-police-shootings-data.csv')
# pd.options.display.max_columns = 50
print(len(df.armed.unique()))
#
# sas.barplot(
#     data=df,
#     x='armed',
#     y='id'
# )

# plt.show()