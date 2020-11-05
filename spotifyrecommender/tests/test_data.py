from data.track_cleaner import clean_tracks
from data.track_cleaner import get_audio_analysis
from data.file_loader import get_saved_data
from helpers.general import select_category
from helpers.general import exit_text
from helpers.general import select_option
from helpers.general import separator
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time

def check_cleaning(liked):
    separator()
    print("{} Cleaned Tracks".format(select_category(liked)))
    separator()
    
    start_time = time.perf_counter()
    df = clean_tracks(liked)
    end_time = time.perf_counter()

    print(df.tail())
    separator()
    print("It took {:0.4f} seconds to clean {} tracks".format(end_time - start_time,len(df)))
    separator()



def check_basic_figures(liked):
    df = get_saved_data(liked)

    separator()
    print("{} Artists".format(select_category(liked)))
    separator()

    plt.figure(figsize=(20,30))
    sns.countplot(df['first_artist'])
    plt.xticks(rotation=90)
    plt.show(block=True)

def check_audio_analysis(liked, amount):
    df = clean_tracks(liked)

    separator()
    print("Audio Analysis for first {} tracks from \"{}\"".format(amount, select_category(liked)))
    separator()
    start_time = time.perf_counter()
    df_analyzed = get_audio_analysis(df.head(amount))
    end_time = time.perf_counter()
    separator()
    print("It took {:0.4f} seconds for the \"{}\" tracks to be analyzed".format(end_time-start_time, select_category(liked)))
    separator()
    print(df_analyzed)

def check_data_loading(liked):
    separator()
    print("{} Loaded Tracks".format(select_category(liked)))
    separator()

    start_time = time.perf_counter()
    df = get_saved_data(liked)
    end_time = time.perf_counter()
    print(df.tail())

    separator()
    print("It took {:0.4f} seconds to load {} tracks".format(end_time - start_time,len(df)))
    separator()

def console_tester():
    test_menu = True
    while(test_menu):
        options = ["Data cleaning - 1","Basic plotting - 2","Audio Analysis - 3","Loading data - 4"]
        choice = select_option(options)

        if(choice == "1"):
            check_cleaning(False)
            check_cleaning(True)
        elif(choice == "2"):
            check_basic_figures(False)
            check_basic_figures(True)
        elif(choice == "3"):
            amount = ""
            while(not amount or amount == "0" or amount == " "):
                print("Enter the amount of tracks to be analyzed:")
                amount = input()
            
            amount = int(amount)
            check_audio_analysis(False, amount)
            check_audio_analysis(True, amount)

        elif(choice == "4"):
            check_data_loading(False)
            check_data_loading(True)
        else:
            test_menu = False
    