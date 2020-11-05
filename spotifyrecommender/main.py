import sys
from data.track_cleaner import full_to_csv
from tests.test_data import console_tester
from recommendation.train_data import console_train_data
import time

def main():
    menu = True
    while(menu):
        print("Run tests press: 1")
        print("Run data loader to CSV press: 2")
        print("Run training press: 3")
        print("-------------------------------")
        print("To exit press any other key!")
        print("-------------------------------")
        print("Make your choice: ")
        choice = int(input())

        if(choice == 1):
                console_tester()
        elif(choice == 2):
                print("---------------------------------")
                print("Starting Full Save to CSV (Liked)")
                print("---------------------------------\n")
                start_time = time.perf_counter()
                full_to_csv(True)
                end_time = time.perf_counter()
                print("---------------------------------")
                print("Stopping Full Save to CSV (Liked)")
                print("Process took {0:0.4f} seconds".format(end_time - start_time))
                print("---------------------------------\n")
                print("---------------------------------")
                print("Starting Full Save to CSV (Not liked)")
                print("---------------------------------\n")
                start_time = time.perf_counter()
                full_to_csv(False)
                end_time = time.perf_counter()
                print("---------------------------------")
                print("Stopping Full Save to CSV (Liked)")
                print("Process took {0:0.4f} seconds".format(end_time - start_time))
                print("---------------------------------\n")
        elif(choice == 3):
                console_train_data()
        else:
                menu = False
                

if __name__ == '__main__':
    main()