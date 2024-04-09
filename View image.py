import tensorflow as tf
import json
import numpy as np
from matplotlib import pyplot as plt


# Avoid OOM errors by setting GPU Memory Consumption Growth
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus: 
    tf.config.experimental.set_memory_growth(gpu, True)
tf.config.list_physical_devices('GPU')


images = tf.data.Dataset.list_files('C:\\Users\\priya\\OneDrive\\Desktop\\project 911\\Data\\train + label\\train\\images\\*')
images.as_numpy_iterator().next()
def load_image(x): 
    byte_img = tf.io.read_file(x)
    img = tf.io.decode_jpeg(byte_img)
    return img
images = images.map(load_image)
images.as_numpy_iterator().next()
type(images)-