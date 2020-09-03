import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('tennis_stats.csv')
print(df.head())
print(df.columns)
print(df.dtypes)

df.sort_values(by='Year', inplace=True)


# perform exploratory analysis here:
# load and investigate the data here:

df = pd.read_csv('tennis_stats.csv')

print(df.head())
print(df.columns)


# perform exploratory analysis here:

breakPointsOpportunities = df.BreakPointsOpportunities.values.reshape(-1, 1)
winnings = df.Winnings

plt.scatter(df.BreakPointsOpportunities, winnings)

model = LinearRegression()
model.fit(breakPointsOpportunities, df.Winnings)

win_predictions = model.predict(breakPointsOpportunities)

plt.plot(breakPointsOpportunities, win_predictions)

plt.clf()


breakPointsOpportunities_train,\
breakPointsOpportunities_test, \
winnings_train, \
winnings_test = train_test_split(breakPointsOpportunities, winnings, train_size=.8, test_size=.2)

# plt.scatter(breakPointsOpportunities_train, winnings_train, alpha=.4)

model.fit(breakPointsOpportunities_train, winnings_train)

print(model.score(breakPointsOpportunities_train, winnings_train))

win_predictions = model.predict(breakPointsOpportunities_test)

plt.scatter(winnings_test, win_predictions, alpha=.4)

# win_predictions = model.predict(breakPointsOpportunities_train)
#
# plt.scatter(winnings_train, win_predictions, alpha=.7)

plt.show()

plt.clf()




## perform single feature linear regressions here:






















## perform two feature linear regressions here:






















## perform multiple feature linear regressions here:
