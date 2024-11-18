# Summary
This repo uses transfer learning with mobilenetv2 to create a custom object classification model. 

The American Sign Language model was trained for 3 epochs without any fine tuning and is decent on this dataset  https://www.kaggle.com/datasets/datamunge/sign-language-mnist. The The clothes images were taken from https://www.kaggle.com/datasets/agrigorev/clothing-dataset-full. 

# Files
create_model.ipynb walks through training the model from scratch. 

Load_model.ipynb allows you to load the pretrained models for immediate use. 

asl_create_image_dir.ipynb and move_images.py create the appropriate directories for training the model   

webcam.py lets you use a saved model on images captured from a webcam every 0.5 seconds    

The saved_model directories contains the pretrained models.


