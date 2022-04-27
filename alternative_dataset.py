import tensorflow as tf
import cv2

# Create pipeline
PATH = "/Users/jeremystubbs/Desktop/Python/Machine_Learning_NNs/Mobilenet/mobilenet_custom/archive/images.csv"
with open(PATH) as f:
    all_image_paths = [row.split(",")[0] for row in f]
with open(PATH) as f:
    all_image_labels = [row.split(",")[2] for row in f] 

# print(all_image_labels)
# print( all_image_paths)


def load_and_preprocess_image(path):
  return cv2.imread(path)

ds = tf.data.Dataset.from_tensor_slices((all_image_paths, all_image_labels))
print(ds)

# The tuples are unpacked into the positional arguments of the mapped function
def load_and_preprocess_from_path_label(path, label):
  return load_and_preprocess_image(path), label

image_label_ds = ds.map(load_and_preprocess_from_path_label)

# train_dataset=asdf
# validation_dataset=asdf