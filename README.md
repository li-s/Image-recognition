# Image-recognition

## Introduction

Image recognition tasks the machine in recognising and classifying objects displayed in images, outputting the object's label and confidence level from a fixed set of categories. The machine trains to recognise objects in images with changes of orientation, lighting, scale, etc. In this repository, I tested the model on 13 different image, with an accuracy of 70%. Some examples are listed below with their level of confidence.

Due to my lack of training data, and the similarity between image recognition is not very removed from handwritting recognition, with the only difference being the extra layers required for highly accurate image recognition as compared to the handwritting counterpart, I will be using the pre-trained [VGG 19 model for Keras](https://gist.github.com/baraldilorenzo/8d096f48a1be4a2d660d#file-vgg-19_keras-py) from VGG(visual geometric group), along with the relevant model [weights](http://www.image-net.org/challenges/LSVRC/2014/).

## Getting started

### Prerequisites

+ [Python3](https://www.python.org/download/releases/3.0/)
+ [numpy](http://www.numpy.org/)
+ [matplotlib](http://matplotlib.org/)
+ [keras](http://machinelearningmastery.com/handwritten-digit-recognition-using-convolutional-neural-networks-python-keras/)
+ [tensorflow](https://www.tensorflow.org/) (for keras machine learning)
+ [OpenCV](http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html)

### Usage

Run `predict.py` from models, and type in the desired file to be tested on. Must be located within the folder `data`. The function returns the most likely label of the object in the picture.

## Testing results
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file0.jpg" height="50">: "purse" (conf. = 7.63%), <img src="https://github.com/li-s/Image-recognition/blob/master/data/file10.jpg" height="50">: "desktop, computer" (conf. = 36.57%), <img src="https://github.com/li-s/Image-recognition/blob/master/data/file6.jpg" height="50">: "envelope" (conf. = 12.39%)

## API reference
+ `models.py`: The KGG 19 model which i will be using.

## miscellaneous

### Readings
+ [Beginner guide to CNN](https://adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/)
+ [Neural networks](http://neuralnetworksanddeeplearning.com/chap1.html)
+ [Watch this](https://www.youtube.com/watch?v=AgkfIQ4IGaM)
+ [VGG 19 Research paper](https://arxiv.org/pdf/1409.1556.pdf)
+ [Reserach paper simplified](http://www.robots.ox.ac.uk/~vgg/practicals/cnn/)
