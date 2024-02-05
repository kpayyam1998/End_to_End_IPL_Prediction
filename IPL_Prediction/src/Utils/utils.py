import os
import sys
import pickle
import pandas as pd
import numpy as np
from src.Exception.customException import customexception

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise customexception(e,sys)
        l