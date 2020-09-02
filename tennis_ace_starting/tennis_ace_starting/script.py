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
plt.subplot(2,2,1)
plt.boxplot(df.ReturnPointsWon)

plt.subplot(2, 2, 2)
plt.scatter(df.Year, df.ReturnPointsWon)

plt.subplot(2, 2, 3)
plt.bar(df.Year, df.ReturnPointsWon)

plt.clf()

# plt.subplot(2, 2, 2)
# plt.scatter(df.Player, df.Winnings)
# plt.xticks(rotation=90)
#
# plt.subplot(2, 2, 1)
# plt.scatter(df.Player, df.BreakPointsOpportunities)
# plt.xticks(rotation=90)

fsr_points_won = df.FirstServeReturnPointsWon.values.reshape(-1, 1)
winning = df.Winnings
#
# plt.subplot(2, 1, 1)
# plt.scatter(fsr_points_won, winning)

fsr_points_won_train, fsr_points_won_test, winning_train, winning_test = train_test_split(fsr_points_won, winning, train_size=.8)

plt.subplot(2, 1, 1)
plt.scatter(fsr_points_won_train, winning_train, alpha=.4)

model = LinearRegression()
model.fit(fsr_points_won_train, winning_train)

win_predictions = model.predict(fsr_points_won_train)
plt.plot(fsr_points_won_train, win_predictions)

prediction = model.predict(fsr_points_won_test)


plt.subplot(2, 1, 2)
plt.scatter(winning_test, prediction, alpha=.7)


plt.show()






















## perform single feature linear regressions here:






















## perform two feature linear regressions here:






















## perform multiple feature linear regressions here:
