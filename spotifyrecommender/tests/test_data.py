from data.track_cleaner import clean_tracks
from data.track_cleaner import get_audio_analysis
import seaborn as sns
import matplotlib.pyplot as plt

def check_dataframe(liked):
    df = clean_tracks(liked)
    if(liked):
        print("--------------------")
        print("Liked Cleaned Tracks")
        print("--------------------")
    else:
        print("------------------------")
        print("Not Liked Cleaned Tracks")
        print("------------------------")
    
    print(df.tail())
    print("------------------------")
    print("Shape: {}".format(len(df)))
    print("------------------------")


def plot_basic_figures(liked):
    df = clean_tracks(liked)
    if(liked):
        print("-------------")
        print("Liked Artists")
        print("-------------")
    else:
        print("-----------------")
        print("Not Liked Artists")
        print("-----------------")

    plt.figure(figsize=(20,30))
    sns.countplot(df['first_artist'])
    plt.xticks(rotation=90)
    plt.show(block=True)



def console_tester():
    print("\nAll tests will be executed:\n")

    check_dataframe(False)
    check_dataframe(True)
    plot_basic_figures(False)
    plot_basic_figures(True)
    