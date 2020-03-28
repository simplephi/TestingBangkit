# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:28:45 2020

@author: Bangkit Team
"""

# IMPORT LIBRARY
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.utils import plot_model
import matplotlib.pyplot as plt

# IMPORT DATASET
dataset = pd.read_csv("https://github.com/AkhmadMuzanni/TestingBangkit/releases/download/1/cardio_train.csv")

# DATA PREPARATION
# Drop unnececsssary column
data_train = dataset.drop(["id"], 1)

# Fix strange weight value
weight = []
for w in data_train["weight"]:
  weight.append(int(w.split('.')[0]))
data_train = data_train.drop(["weight"], 1)
data_train["weight"] = weight

# Fix strange attribute values
# delete height value that above 220
data_train = data_train.drop(data_train[data_train.height > 220].index)
# delete systolic blood pressure value that above 250
data_train = data_train.drop(data_train[data_train.ap_hi > 250].index)
# delete diastolic blood pressure value that above 200
data_train = data_train.drop(data_train[data_train.ap_lo > 200].index)