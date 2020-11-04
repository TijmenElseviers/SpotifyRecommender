from data.track_cleaner import clean_tracks

def check_dataframe_like():
    liked = clean_tracks(True)
    print("--------------------")
    print("Liked Cleaned Tracks")
    print("--------------------")
    print(liked.tail())

def check_dataframe_nolike():
    notLiked = clean_tracks(False)
    print("------------------------")
    print("Not Liked Cleaned Tracks")
    print("------------------------")
    print(notLiked.tail())

def console_tester():
    print("\nAll tests will be executed:\n")

    check_dataframe_like()
    check_dataframe_nolike()
    