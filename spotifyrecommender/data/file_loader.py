import json

resource_folder = '../resources/'

def get_file(filename):
    return json.load(open(resource_folder + filename))