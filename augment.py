<<<<<<< HEAD
datagen = ImageDataGenerator()
datagen.fit(train)
X_batch, y_batch = datagen.flow(X_train, y_train, batch_size=batch_size)
model.fit_generator(datagen, samples_per_epoch=len(train), epochs=epochs)
datagen = ImageDataGenerator(rotation_range=30, horizontal_flip=0.5)
datagen.fit(img)i=0

for img_batch in datagen.flow(img, batch_size=9):
    for img in img_batch:
        plt.subplot(330 + 1 + i)
        plt.imshow(img)
        i=i+1
    if i >= batch_size:
        break

def AHE(img):
    img_adapteq = exposure.equalize_adapthist(img, clip_limit=0.03)
    return img_adapteq

datagen = ImageDataGenerator(rotation_range=30, horizontal_flip=0.5, preprocessing_function=AHE)
=======
#augmenting the dataset of footprints before feeding it to the network for segmentation

import imgaug as ia
import imgaug.augmenters as iaa
import os
import numpy as np
from PIL import Image

seq = iaa.Sequential([
    iaa.Crop(px=(0, 100)), # crop images from each side by 0 to 16px (randomly chosen)
    iaa.Fliplr(0.5), # horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(0, 3.0)), # blur images with a sigma of 0 to 3.0
    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        #translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
        rotate=(-25, 25),
        shear=(-8, 8)
    ),
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    iaa.LinearContrast((0.75, 1.5)),
    iaa.Flipud(0.5)
],random_order=True)

def augment_seg( img , seg  ):
	
	aug_det = seq.to_deterministic() 
	image_aug = aug_det.augment_image( img )

	segmap = ia.SegmentationMapOnImage( seg , nb_classes=np.max(seg)+1 , shape=img.shape )
	segmap_aug = aug_det.augment_segmentation_maps( segmap )
	segmap_aug = segmap_aug.get_arr_int()

	return image_aug , segmap_aug

pics = os.listdir("/Users/abhinav/Documents/KT/pngfootprint/")
anns = os.listdir("/Users/abhinav/Documents/KT/finalannotation/")

ct=0
for i in range(2):
    for pic,ann in zip(pics,anns):
        ct+=1
        ipic = Image.open("/Users/abhinav/Documents/KT/pngfootprint/"+pic)
        iann = Image.open("/Users/abhinav/Documents/KT/finalannotation/"+ann)
        npic=np.asarray(ipic)
        nann=np.asarray(iann)
        # print(type(npic))
        # print(type(nann))
        augpic,augann=augment_seg(npic,nann)
        imgpic = Image.fromarray(augpic)
        imgann = Image.fromarray(augann)
        # imgpic.save('/Users/abhinav/Documents/KT/augfootprint/'+str(ct)+'.png')
        # imgann.save('/Users/abhinav/Documents/KT/augannotation/'+str(ct)+'.png')
        imgpic.save('/Users/abhinav/Documents/KT/ims/'+str(ct)+'.png')
        imgann.save('/Users/abhinav/Documents/KT/anns/'+str(ct)+'.png')
>>>>>>> 88001a21c7d7c1b7182307cc051e4c0e25bf900d
