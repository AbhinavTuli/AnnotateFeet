from keras_segmentation.models.unet import vgg_unet
import matplotlib.pyplot as plt


model = vgg_unet(n_classes=2 ,  input_height=416, input_width=608  )

model.train(
    train_images =  "/Users/abhinav/Documents/Foot Data and Manipulations/Training/AugmentedDataset/",
    train_annotations = "/Users/abhinav/Documents/Foot Data and Manipulations/Training/AugmentedAnnotations/",
    checkpoints_path = "/tmp/vgg_unet_2", epochs=1
)

# model_json = model.to_json()
# with open("model.json","w") as json_file:
#     json_file.write(model_json)

model.save_weights("model_17/2_1.h5")


# out = model.predict_segmentation(
#     inp="dataset1/images_prepped_test/0016E5_07965.png",
#     out_fname="/tmp/out.png"
# )

# plt.imshow(out)

# evaluating the model 
#print(model.evaluate_segmentation( inp_images_dir="/ims/"  , annotations_dir="/anns" ))
