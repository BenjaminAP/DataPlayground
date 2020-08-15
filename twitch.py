import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df_twitch_stream = pd.read_csv('csv_files/twitch/cleaner_twitch_stream.csv')
df_twitch_chat = pd.read_csv('csv_files/twitch/chat.csv')


def plot_top_views_per_game():
    views_per_game = df_twitch_stream.groupby('game').game.agg('count').to_frame('views').reset_index()
    views_per_game.sort_values(by='views', ascending=False, inplace=True, ignore_index=True)

    df = views_per_game[views_per_game.views > 1000]
    ax = plt.subplot()
    ax.set_title('Games with more than 1100 views')

    plt.xticks(rotation='vertical')

    plt.bar(x=range(len(df.game)), height=df.views, tick_label=df.game)
    plt.legend(['Twitch'])
    plt.show()
    plt.clf()


def pie_chart_lol_views_per_country():
    lol_views_per_country = df_twitch_stream[df_twitch_stream.game == 'League of Legends'] \
        .groupby('country').country.agg('count').to_frame('view_count').reset_index()
    lol_views_per_country.sort_values(by='view_count', ascending=False, inplace=True, ignore_index=True)
    colors = ['lightskyblue',
              'gold',
              'lightcoral',
              'gainsboro',
              'royalblue',
              'lightpink',
              'darkseagreen',
              'sienna',
              'khaki',
              'gold',
              'violet',
              'yellowgreen']

    plt.title('Lol Top Viewers per State')

    plt.pie(x=lol_views_per_country.view_count.head(12),
            labels=lol_views_per_country.country.head(12),
            colors=colors,
            explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            shadow=True,
            startangle=345,
            autopct='%1.0f%%',
            pctdistance=1.15)

    plt.legend(lol_views_per_country.country, loc='right')

    plt.show()

def clean_data():
    date_times = df_twitch_stream.time.str.split(pat=' ', expand=True)

    df_date = date_times[0]
    date = {'year': pd.DatetimeIndex(df_date).year,
            'month': pd.DatetimeIndex(df_date).month,
            'day': pd.DatetimeIndex(df_date).day}
    date = pd.DataFrame(data=date)

    for key, date_unit in date.items():
        df_twitch_stream[key] = date_unit

    df_time = date_times[1]
    time = {'hour': pd.DatetimeIndex(df_time).hour,
            'min': pd.DatetimeIndex(df_time).minute,
            'sec': pd.DatetimeIndex(df_time).second}
    time = pd.DataFrame(data=time)

    df_twitch_stream['hour'] = time.hour

    for key, time_unit in time.items():
        df_twitch_stream[key] = time_unit
    df_twitch_stream.to_csv('cleaner_twitch_stream.csv', index=False)

def lol_views_jan_1():

    jan_15_2015 = df_twitch_stream[(df_twitch_stream.year == 2015) &
                                   (df_twitch_stream.month == 1) &
                                   (df_twitch_stream.day == 1) &
                                   (df_twitch_stream.game == 'League of Legends')]
    views_per_hour = jan_15_2015.groupby('hour').hour.agg('count').to_frame('views').reset_index()
    views_per_hour.sort_values(by='hour', ascending=True, inplace=True, ignore_index=True)
    print(views_per_hour)

    ax = plt.subplot()
    plt.title("League of Legends Views in Jan,1")
    ax.set_xticks(range(len(views_per_hour.hour)))
    ax.set_xticklabels(views_per_hour.hour)

    plt.plot(views_per_hour.hour, views_per_hour.views)
    y_lower = views_per_hour.views - (views_per_hour.views * 0.15)
    y_upper = views_per_hour.views + (views_per_hour.views * 0.15)
    plt.fill_between(range(len(views_per_hour.hour)), y_lower, y_upper, alpha=0.2)

    plt.xlabel('hour')
    plt.ylabel('views')
    plt.show()

