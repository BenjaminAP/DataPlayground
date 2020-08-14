import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sas

firearm_background_checks = pd.read_csv('csv_files/law_order/nics-firearm-background-checks.csv')

# cleaning month -> year, month columns
years_months_list = firearm_background_checks.month.str.split('-', expand=True)
firearm_background_checks['year'] = years_months_list[0]
firearm_background_checks['month'] = years_months_list[1]

puerto_rico = pd.read_csv('csv_files/law_order/puerto_rico_gun_background_check.csv')

puerto_rico_2018 = puerto_rico[puerto_rico.year == 2018]
print(puerto_rico_2018.id.count())

sas.barplot(
    data=puerto_rico_2018,
    x='month',
    y='handgun'
)

plt.show()