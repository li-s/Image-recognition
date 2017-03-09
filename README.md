# Image-recognition

## Introduction

Image recognition tasks the machine in recognising and classifying objects displayed in images, outputting the object's label and confidence level from a fixed set of categories. The machine trains to recognise objects in images with changes of orientation, lighting, scale, etc. In this repository, I tested the model on 20 different image. Some examples are listed below with their level of confidence.

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
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file0.jpg" height="50">: "purse" (conf. = 7.63%) The label is wrong, which may be attributed to the tissue taking up a small proportion of the image, and is around the same colour of the desk.  
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file2.jpg" height="50">: "digital, watch" (conf. = 50.62%) The label is correct.  
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file3.jpg" height="50">: "purse" (conf. = 53.18%) The label is correct.  
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file5.jpg" height="50">: "tripod" (conf. = 10.94%) The label is wrong, which may be attributed to the metalic look of the pen looking more similiar to the leg of a tripod.  
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file10.jpg" height="50">: "traffic, light, traffic, signal, stoplight" (conf. = 10.77%) The label is wrong, which may be attributed to the training data being confined to the more modest image of a computer. The bright lights and screens of this computer may be confused with traffic signs and signals.  
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file14.jpg" height="50">: "lion, Panthera, leo" (conf. = 98.32%%) The label is correct.  
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file15.jpg" height="50">: "restaurant, eating, house, eating, place, eatery" (conf. = 19.08%) The label is correct. Although the picture shows a church, the small size of the building makes it quite indistinguishable from a normal house.  
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file18.jpg" height="50">: "pot, flowerpot" (conf. = 23.33%) The label is correct.  
<img src="https://github.com/li-s/Image-recognition/blob/master/data/file19.jpg" height="50">: "crane" (conf. = 50.43%) The label is correct.


## API reference
+ `models.py`: The KGG 19 model which i will be using.

## miscellaneous

### Readings
+ [Beginner guide to CNN](https://adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/)
+ [Neural networks](http://neuralnetworksanddeeplearning.com/chap1.html)
+ [Watch this](https://www.youtube.com/watch?v=AgkfIQ4IGaM)
+ [VGG 19 Research paper](https://arxiv.org/pdf/1409.1556.pdf)
+ [Reserach paper simplified](http://www.robots.ox.ac.uk/~vgg/practicals/cnn/)
