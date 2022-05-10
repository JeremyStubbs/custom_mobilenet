# Summary
This repo uses transfer learning with a mobilenet v2. The beauty of this repo is it can easily be applied to any set of pictures to create a custom object detection model. 

The American Sign Language model was trained for 3 epochs without any fine tuning and is decent on this dataset  https://www.kaggle.com/datasets/datamunge/sign-language-mnist. The The clothes images were taken from https://www.kaggle.com/datasets/agrigorev/clothing-dataset-full. 

# Files
create_model.ipynb walks through training the model from scratch. 

Load_model.ipynb allows you to load the pretrained models for immediate use. 

The saved_model directories contains the pretrained models.

# Comments
The models are sadly overfitted to the data which is of poor quality. There is insufficient variation in backgrounds. Some improvements that could be made are:
1) Data augmentation as described on https://www.tensorflow.org/tutorials/images/transfer_learning
2) One could gather pictures of people in various articles of clothing and create tf records in which one picture could be trained for multiple classes simulataneously. This would force the model to recognize boundaries between the articles of clothing.
How to do this:
- Your final activation will now need to be a sigmoid, since you will not predict a single class probability distribution anymore. Now you want each output neuron to predict a value between 0 and 1, with more than one neuron possibly having values close to 1.
- Your loss function should now be binary_crossentropy, since you will treat each output neuron as an independent prediction, which you will compare to the true label.
- You will want to change your label encoding to one-hot style now, each label having a len equal to num_classes, and having 1's only at those positions where the image has that class, the rest being 0's.


