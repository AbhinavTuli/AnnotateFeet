#augmenting the dataset of footprints before feeding it to the network for segmentation

import imgaug as ia
import imgaug.augmenters as iaa
import os
import numpy as np
from PIL import Image

seq = iaa.Sequential([
    iaa.Crop(px=(0, 100)), # crop images from each side by 0 to 100px (randomly chosen)
    iaa.Fliplr(0.5), # horizontally flip 50% of the images
    iaa.GaussianBlur(sigma=(0, 3.0)), # blur images with a sigma of 0 to 3.0
    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        #translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
        rotate=(-25, 25),
        shear=(-8, 8),
        mode='edge',
    ),
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    iaa.LinearContrast((0.5, 1.75)),
    #iaa.Flipud(0.5)
],random_order=True)

def augment_seg( img , seg  ):
	
	aug_det = seq.to_deterministic() 
	image_aug = aug_det.augment_image( img )

	segmap = ia.SegmentationMapsOnImage( seg, shape=img.shape )
	segmap_aug = aug_det.augment_segmentation_maps( segmap )
	segmap_aug = segmap_aug.get_arr()

	return image_aug , segmap_aug

pics = os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/Dataset/")
anns = os.listdir("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/Annotations/")

ct=0
for i in range(2):
    for pic,ann in zip(pics,anns):
        try:
            ct+=1
            ipic = Image.open("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/Dataset/"+pic)
            iann = Image.open("/Users/abhinav/Documents/Foot Data and Manipulations/Testing/Annotations/"+ann)
            npic=np.asarray(ipic)
            nann=np.asarray(iann)
            # print(type(npic))
            # print(type(nann))
            augpic,augann=augment_seg(npic,nann)
            imgpic = Image.fromarray(augpic)
            imgann = Image.fromarray(augann)
            # imgpic.save('/Users/abhinav/Documents/KT/augfootprint/'+str(ct)+'.png')
            # imgann.save('/Users/abhinav/Documents/KT/augannotation/'+str(ct)+'.png')
            imgpic.save('/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedDataset/'+str(ct)+'.png')
            imgann.save('/Users/abhinav/Documents/Foot Data and Manipulations/Testing/AugmentedAnnotations/'+str(ct)+'.png')
        except Exception as e:
            print("Error!",e)

