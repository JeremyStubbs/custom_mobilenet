This repo uses transfer learning with a mobilenet v2 to create a model that can detect articles of clothing. The beauty of this repo is it can easily be applied to any set of pictures to create a custom object detection and localization model.

create_model.ipynb walks through training the model from scratch. 

Load_model.ipynb allows you to load the pretrained model for immediate use. 

Localization.ipynb attempts to use heat maps to localize the recognized object. The sources for this are https://alexisbcook.github.io/2017/global-average-pooling-layers-for-object-localization/ and http://cnnlocalization.csail.mit.edu/Zhou_Learning_Deep_Features_CVPR_2016_paper.pdf. 

To generate a bounding box from the heat map, you to create a binary map from the color map array called "final_arr" (they used a value of 20% of max value).Then take the bounding box that covers the largest connected component in the segmentation map. 

The images were taken from https://www.kaggle.com/datasets/agrigorev/clothing-dataset-full. The model is sadly overfitted to the data which is of poor quality. There are too few pictures in each category, significant overlap and they are all at the same angle. Some improvements that could be made are:
1) Data augmentation as described on https://www.tensorflow.org/tutorials/images/transfer_learning
2) One could gather pictures of people in various articles of clothing and create tf records in which one picture could be trained for multiple classes simulataneously. This would force the model to recognize boundaries between the articles of clothing.
Ultimately, 3D vision is necessary to highly accurately identify an article of clothes as a folded plane.
