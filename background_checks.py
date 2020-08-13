import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sas

firearm_background_checks = pd.read_csv('nics-firearm-background-checks.csv')

# cleaning month -> year, month columns
years_months_list = firearm_background_checks.month.str.split('-', expand=True)
firearm_background_checks['year'] = years_months_list[0]
firearm_background_checks['month'] = years_months_list[1]

puerto_rico = firearm_background_checks[firearm_background_checks.state == "Puerto Rico"]

sas.barplot(
    data=puerto_rico,
    x='year',
    y='handgun'
)

plt.show()