# Cat-Vs-Dog-Classification-Api
A flask webapp to classify the Cat Vs Dog in a List of Images.The web app can take single or batch input in base64 format of image and predict the presence of leaves and distinguish of object. 

## Description: 
The Model is build and trained using inception model. The user have option to upload a image as a single or batch input in base64 format. API can be tested using PostMan. 
The api checks following conditions - 
1. If the uploaded List containes base64 format images or not(empty list error - No image selected).
2. If the uploaded List containes empty string inside.(empty string error - 0 image length).

The image is then converted into .jpg format and stored into a folder and each image is 
then scanned for prediction using <b>predict_binary(image_name)</b>->(created function in app.py) and necessary adjustments to the image are done , this process is repeated till all images have been scanned and all predictions are combined to make a List of output and stored in a list <b>predict_list</b>(var defined inside app.py)
The input and output are given in POST method at url:http://0.0.0.0:5000/

## Sample Input 
Body: {
"image_list":[“List of images in base64 format”]
}

## Sample Ouput

## No image

<img src="assert/02.png" width="700" height="380" />

## Single image

<img src="assert/01.png" width="700" height="380" />

## Multiple image 

<img src="assert/03.png" width="700" height="380" />

## Back_End: 
Python, Flask  


## Libraries_used: 

### Flask libraries
<pre>
from flask import Flask, request
</pre>
### lib for base64 to image conv
<pre>
import base64
</pre>

### tensorflow libraries
<pre>
from tensorflow import keras
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
</pre>

## RUN: 
0. Download model from the google drive from given link below
<pre>https://drive.google.com/drive/folders/1_KqT8_8D6sVp3hV-TvbFwY_bVr7sX83A?usp=sharing</pre>
1. Clone the repo   
2. Create environment  
3. pip install -r requirement.txt
4. change dir path inside project according to your model location.
4. python app.py  


## Demo:  

<img src="/flask_demo.gif" width="800" height="480" />

