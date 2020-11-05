import json
import os
import numpy as np
import pandas as pd

resource_folder = 'resources/'
filedir = os.path.dirname(os.path.realpath('__file__'))

def get_file(filename):
    relative_path = os.path.join(filedir, resource_folder+filename)
    return json.load(open(relative_path))

def get_saved_data(liked):
    filename = "playlist_{}.csv".format(str(liked).lower())
    relative_path = os.path.join(filedir, resource_folder+filename)

    return pd.read_csv(relative_path, index_col=0)