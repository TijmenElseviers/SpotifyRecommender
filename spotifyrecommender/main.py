import sys
from data.track_cleaner import clean_console
from tests.test_data import console_tester
from recommendation.train_data import console_train_data

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
                clean_console()
        elif(choice == 3):
                console_train_data()
        else:
                menu = False
                

if __name__ == '__main__':
    main()