from keras.layers 
import Input, Lambda, Dense, Flatten
from keras.models
import Model
import tensorflow as tf
from tensorflow.keras.applications.vgg16
import preprocess_input
from keras.applications.vgg16 
import VGG16
from keras.preprocessing
import image
from keras.preprocessing.image 
import ImageDataGenerator
from keras.models 
import Sequential
from tensorflow
import keras
import numpy as np
from glob 
import glob
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from google.colab 
import drive
drive.mount('/content/drive')
IMAGE_SIZE = [224, 224]
train_path = '/content/drive/MyDrive/SIH_TRAIN1'
test_path = '/content/drive/MyDrive/SIH_TEST1'
from PIL 
import Image 
import os 
from IPython.display 
import display
from IPython.display 
import Image as _Imgdis


# creating a object  

folder = train_path+'/D'


onlyblightfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
print("Working with {0} images".format(len(onlyblightfiles)))
print("Image examples: ")


for i in range(6):
    print(onlyblightfiles[i])
    display(_Imgdis(filename=folder + "/" + onlyblightfiles[i], width=240, height=240))
    dnet=VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)
dnet.input
for layer in dnet.layers:
  layer.trainable = False
folders = glob('/content/drive/MyDrive/SIH_TRAIN1/*')
print(len(folders))
x = Flatten()(dnet.output)
prediction = Dense(len(folders), activation='softmax')(x)
model = Model(inputs=dnet.input, outputs=prediction)
model.summary()
train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')
test_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')
    train_set = train_datagen.flow_from_directory(train_path,target_size = (224, 224),batch_size = 8,class_mode = 'categorical')
    test_set = test_datagen.flow_from_directory(test_path,target_size = (224, 224),batch_size = 8,class_mode = 'categorical')
    from datetime import datetime
from keras.callbacks import ModelCheckpoint
model.compile(loss='categorical_crossentropy',metrics=['accuracy'],optimizer='adam')


checkpoint = ModelCheckpoint(filepath='/content/drive/MyDrive/S_I_H/mymodel.h5',verbose=2, save_best_only=True)

callbacks = [checkpoint]

start = datetime.now()

model_history=model.fit_generator(train_set, validation_data=test_set, epochs=300, steps_per_epoch=25, validation_steps=32, callbacks=callbacks ,verbose=2)
duration = datetime.now() - start
print("Training completed in time: ", duration)

_# Plot training & validation loss values
plt.plot(model_history.history['accuracy'])
plt.plot(model_history.history['val_accuracy'])
plt.title('CNN Model accuracy values')  
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
folders
from keras.models 
import load_model
import cv2
import numpy as np


class_names = ['D','ESCS','VSCS','DD','SCS','CS'] # fill the rest

model = load_model('/content/drive/MyDrive/S_I_H/mymodel.h5')

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

img = cv2.imread('/content/drive/MyDrive/SIH_TEST1/ESCS/3DIMG_17MAY2021_0300_L1C_ASIA_MER_VIS.jpg')
img = cv2.resize(img,(224,224))
img = np.reshape(img,[1,224,224,3])
classes = np.argmax(model.predict(img), axis = -1)
print(classes)

names = [class_names[i] for i in classes]

print(names)
