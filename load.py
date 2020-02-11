from keras_segmentation.models.unet import vgg_unet
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.models import model_from_json
# import numpy
# import os
model = vgg_unet(n_classes=2 ,  input_height=416, input_width=608)
model.load_weights("model.h5")

model.train(
    train_images =  "./ims/",
    train_annotations = "./anns/",
    checkpoints_path = "./tmp/vgg_unet_1", epochs=3
)

model_json = model.to_json()
with open("model.json","w") as json_file:
    json_file.write(model_json)
model.save_weights("model_train2.h5")
