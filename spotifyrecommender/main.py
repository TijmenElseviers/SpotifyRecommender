import sys
from data.track_cleaner import full_to_csv
from tests.test_data import console_tester
from recommendation.train_data import console_train_data
from helpers.general import select_category
from helpers.general import exit_text
from helpers.general import select_option
import time

def option_load_to_csv(liked):
        category = select_category(liked)

        print("---------------------------------")
        print("Starting Full Save to CSV ({})".format(category))
        start_time = time.perf_counter()
        full_to_csv(liked)
        end_time = time.perf_counter()
        print("Stopping Full Save to CSV ({})".format(category))
        print("Process took {0:0.4f} seconds".format(end_time - start_time))
        print("---------------------------------\n")

def main():
    menu = True
    while(menu):
        print("Select one of the following options:")
        options = ["Run tests - 1", "Load to CSV - 2", "Run training - 3"]
        choice = str(select_option(options))

        if(choice == "1"):
                console_tester()
        elif(choice == "2"):
               option_load_to_csv(True)
               option_load_to_csv(False)
        elif(choice == "3"):
                console_train_data()
        else:
                menu = False

if __name__ == '__main__':
    main()