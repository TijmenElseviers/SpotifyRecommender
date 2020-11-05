def select_category(liked):
    if(liked):
        return "Liked"

    return "Not Liked"

def exit_text():
    print("To exit press any other key!")
    print("Make your choice! ")
    separator()

def separator():
    print("-------------------------------")

def select_option(options):
    separator()
    for option in options:
        print("\t{}".format(option))
    exit_text()
    return input()