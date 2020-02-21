import segmentation_models as sm
import tensorflow as tf
import numpy as np
def ld_data(dir):
    image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
    BATCH_SIZE = 32
    IMG_HEIGHT = 224
    IMG_WIDTH = 224
    train_data_gen = image_generator.flow_from_directory(directory=str(dir),shuffle=True,target_size=(IMG_HEIGHT, IMG_WIDTH),)
BACKBONE = 'resnet34'
preprocess_input = sm.get_preprocessing(BACKBONE)

# load your data
x_train, y_train = ld_data("/Users/abhinav/Documents/Foot Data and Manipulations/Training/AugmentedDataset/"),ld_data("/Users/abhinav/Documents/Foot Data and Manipulations/Training/AugmentedAnnotations/")

# preprocess input
# x_train = preprocess_input(x_train)
# x_val = preprocess_input(x_val)

# define model
model = sm.Unet(BACKBONE, classes=2,encoder_weights='imagenet')
model.compile(
    'Adam',
    loss=sm.losses.bce_jaccard_loss,
    metrics=[sm.metrics.iou_score],
)

# fit model
# if you use data generator use model.fit_generator(...) instead of model.fit(...)
# more about `fit_generator` here: https://keras.io/models/sequential/#fit_generator
model.fit(
   x=x_train,
   y=y_train,
   #batch_size=16,
   epochs=100,
   steps_per_epoch=5
   #validation_data=(x_val, y_val),
)
model.save_weights("model_new_1.h5")