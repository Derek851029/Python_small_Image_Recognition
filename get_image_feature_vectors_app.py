import tensorflow as tf
import tensorflow_hub as hub
# For saving 'feature vectors' into a txt file
import numpy as np
# Glob for reading file names in a folder
import glob
import os.path

#module_handle = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4"
module_handle = "D:/AI_Image/AI_model"
module = hub.load(module_handle)

#################################################
#################################################
# This function:
# Loads the JPEG image at the given path
# Decodes the JPEG image to a uint8 W X H X 3 tensor
# Resizes the image to 224 x 224 x 3 tensor
# Returns the pre processed image as 224 x 224 x 3 tensor
#################################################
def load_img(path):
    # Reads the image file and returns data type of string
    print('load_img: path = ', path)
    img = tf.io.read_file(path)
    # Decodes the image to W x H x 3 shape tensor with type of uint8
    img = tf.io.decode_jpeg(img, channels=3)
    # Resizes the image to 224 x 224 x 3 shape tensor
    img = tf.image.resize_with_pad(img, 224, 224)
    # Converts the data type of uint8 to float32 by adding a new axis
    # img becomes 1 x 224 x 224 x 3 tensor with data type of float32
    # This is required for the mobilenet model we are using
    img = tf.image.convert_image_dtype(img,tf.float32)[tf.newaxis, ...]
    return img

#################################################
# This function:
# Loads the mobilenet model in TF.HUB
# Makes an inference for all images stored in a local folder
# Saves each of the feature vectors in a file
#################################################

def get_image_feature_vectors_app(path): #給app用, 分別原檔和app的
    # Definition of module with using tfhub.dev
    # module_handle = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4"
    # # Loads the module
    # module = hub.load(module_handle)
    # Loops through all images in a local folder

    for filename in glob.glob(''+path+'*.jpg'):
        print(filename)
        # Loads and pre-process the image
        img = load_img(filename)
        # Calculate the image feature vector of the img
        features = module(img)
        # Remove single-dimensional entries from the 'features' array  
        feature_set = np.squeeze(features)
        
        # Saves the image feature vectors into a file for later use
        outfile_name = os.path.basename(filename) + ".npz"
        
        out_path = os.path.join(path,outfile_name)
        # Saves the 'feature_set' to a text file
        np.savetxt(out_path, feature_set, delimiter=',')
#get_image_feature_vectors()