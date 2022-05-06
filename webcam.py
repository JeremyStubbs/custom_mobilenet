import cv2
import numpy as np
import ast
import scipy   
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2     
from keras.preprocessing import image    
from keras.models import Model   
import time


new_model = tf.keras.models.load_model('saved_model_asl/my_model')

out1 = new_model.layers[-4].output

out2 = new_model.layers[-1].output


model = tf.keras.Model(inputs=new_model.input, 
    outputs=(out1, out2)) 

all_amp_layer_weights = model.layers[-1].get_weights()[0]

labels=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
threshold = 0.5

cap = cv2.VideoCapture(0)

while True:
    # time.sleep(0.5)
    success,img = cap.read()
    resized = cv2.resize(img, (224, 224))
    reshaped = resized.reshape(1, 224, 224, 3)
    
    last_conv_output, predictions = model.predict(reshaped)
    
    final_arr = []

    for val in predictions[0]:
        if val > threshold:
            index_of = np.where(predictions[0]==val)
            print(labels[index_of[0][0]], index_of[0][0])
        
    cv2.imshow("output",img)
   
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


##The following code "localizes", but causes the program to be too slow. 
# Need to train with bounding box. 
# Don't need to change the model much - just change final output layer to -3 (gap layer) for the box.