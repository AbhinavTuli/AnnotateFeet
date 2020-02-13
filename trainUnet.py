from keras_segmentation.models.segnet import vgg_segnet

model = vgg_segnet(n_classes=2 ,  input_height=416, input_width=608  )

model.train(
    train_images =  "./ims/",
    train_annotations = "./anns/",
    checkpoints_path = "/tmp/vgg_unet_1" , epochs=1
)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")

 
# out = model.predict_segmentation(
#     inp="/Users/abhinav/Documents/KT/526.png",
#     out_fname="/tmp/out.png"
# )

import matplotlib.pyplot as plt
plt.imshow(out)

# evaluating the model 
print(model.evaluate_segmentation( inp_images_dir="./augfootprint/"  , annotations_dir="./augannotation/" ) )
