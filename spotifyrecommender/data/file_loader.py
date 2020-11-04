import json
import os

resource_folder = 'resources/'
filedir = os.path.dirname(os.path.realpath('__file__'))

def get_file(filename):
    relative_path = os.path.join(filedir, resource_folder+filename)
    return json.load(open(relative_path))