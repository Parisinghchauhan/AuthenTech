import tensorflow as tf
import json
import numpy as np
from matplotlib import pyplot as plt


gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus: 
    tf.config.experimental.set_memory_growth(gpu, True)
tf.config.list_physical_devices('GPU')


train_images = tf.data.Dataset.list_files('C:\\Users\\priya\\OneDrive\\Documents\\GitHub\\Authentic\\Data\\train\\images\\*.jpg')
def load_image(x): 
    byte_img = tf.io.read_file(x)
    img = tf.io.decode_jpeg(byte_img)
    return img
train_data = train_images.map(load_image)
train_data.as_numpy_iterator().next()
type(train_data)