This repo uses transfer learning with a mobilenet v2 to create a model that can detect articles of clothing.

create_model.ipynb walks through training the model from scratch. Load_model.ipynb allows you to load the pretrained model for immediate use. Localization.ipynb attempts to use this code https://alexisbcook.github.io/2017/global-average-pooling-layers-for-object-localization/ to localize with heat mapping from the gap layer.

The images were taken from https://www.kaggle.com/datasets/agrigorev/clothing-dataset-full