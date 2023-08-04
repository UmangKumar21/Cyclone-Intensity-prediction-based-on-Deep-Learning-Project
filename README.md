# Cyclone-Intensity-prediction-based-on-Deep-Learning
This project is predicting the Intensity of the cyclone using Deep Learning.
Development of a deep CNN for Tropical Cyclone intensity estimation using half-hourly INSAT-3D IR(Indian National Satellite- 3D Infrared) Images and development of a web application for visualization of the imagery.

INSAT3D/3DR observations are available at every 30-minute interval and these observations are very useful in understanding the instantaneous structural changes during the evolution, intensification, and landfall of Tropical Cyclones.

Datasets of Cyclones captured by INSAT-3D over the Indian Oceans are available since 2014. These datasets can be used for training and testing of the Model. Traditional methods for Intensity estimation require accurate center determination for intensity estimation. Development of this estimation will be very useful during the initial stage of cyclone formation when the determination of an accurate center becomes difficult.

CNN: A convolutional neural network (CNN or convent) is a subset of machine learning. CNNs are particularly useful for finding patterns in images to recognize objects, classes, and categories. A convolution is essentially sliding a filter over the input.

VGG16: VGG16 refers to the VGG model, also called VGGNet. It is a convolution neural network (CNN) model supporting 16 layers. Accuracy is high compared with the mobile net model. VGG16 has 13 convolutional layers to extract features and 3 dense layers for classification. The VGG16 model can achieve a test accuracy of 92.7% in ImageNet, a dataset containing more than 14 million training images across 1000 object classes.

Cyclone Tauktae

From 14/05/2021 to 19/05/2021.
Images taken: 257
Cyclone Amphan -From 16/05/2020 to 21/05/2020.

Images taken: 200
Non-Cyclonic days: -20/05/2021 and 21/05/2021. -Images taken: 96

Total number of images taken: 553 (before augmentation).

Total number of images taken: 6000 (after augmentation).

Using the VGG16 model, considering two types of cyclones Tauktae and Amphan with images of 553 and with 300 epochs we got the accuracy of 0.8779.
