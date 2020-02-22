from keras_segmentation.models.unet import vgg_unet
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import os
model = vgg_unet(n_classes=2 ,  input_height=416, input_width=608  )

# load weights into model
model.load_weights("model_unet_21Feb_1.h5")

#to test the trained model
#files =os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedDataset/")

# for file in files:
#     print(file)
#     try:
#         out = model.predict_segmentation(
#         inp="/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedDataset/"+file,
#         out_fname="/Users/abhinav/Documents/Foot Data and Manipulations/Testing/Output 1st Epoch/"+file
# )
#     except Exception as e:
#         print(e)
#         continue

#To further train model

model.train(
    train_images =  "/Users/abhinav/Documents/Foot Data and Manipulations/Training/AugmentedDataset/",
    train_annotations = "/Users/abhinav/Documents/Foot Data and Manipulations/Training/AugmentedAnnotations/",
    checkpoints_path = "/tmp/vgg_unet_22Feb", epochs=1
)
model.save_weights("model_unet_22Feb_2.h5")

#print(model.evaluate_segmentation( model,os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedDataset/")  , os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedAnnotations/") ) )