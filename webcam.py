import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2     
from keras.preprocessing import image    
from keras.models import Model   
import time


model = tf.keras.models.load_model('saved_model_asl/my_model')

label_map = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]

threshold = 0.25

cap = cv2.VideoCapture(0)
last_time = time.time()


while True:
    success,img = cap.read()
    if time.time()-last_time > 0.5:
        last_time = time.time()
        resized = cv2.resize(img, (224, 224))
        resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        resized = cv2.cvtColor(resized, cv2.COLOR_GRAY2RGB)

        reshaped = resized.reshape(1, 224, 224, 3)

        predictions = model.predict(reshaped, verbose=0)

        max_val = np.amax(predictions)
        if max_val > threshold:
            print(label_map[np.argmax(predictions)])

        
    cv2.imshow("output",img)
   
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

