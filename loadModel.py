from keras_segmentation.models.unet import vgg_unet
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import os
model = vgg_unet(n_classes=2 ,  input_height=416, input_width=608  )

# load weights into model
model.load_weights("model_train2.h5")

#to test the trained model
files =os.listdir("./ims/")

for file in files:
    print(file)
    try:
        out = model.predict_segmentation(
        inp="./ims/"+file,
        out_fname="./outmodifiedwts/"+file
)
    except:
        continue

#To further train model

# model.train(
#     train_images =  "./ims/",
#     train_annotations = "./anns/",
#     checkpoints_path = "./tmp/vgg_unet_1", epochs=1
# )
