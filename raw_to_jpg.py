import os
import imageio
import numpy as np
import rawpy

file_list = os.listdir('./')
os.mkdir('./jpgready')
for file in file_list:
    if 'CR2' in file:
        pic_path = os.path.join('./'+file)
        raw = rawpy.imread(pic_path)
        #rgb = raw.postprocess()
        rgb = raw.postprocess(use_camera_wb=True,use_auto_wb=False, half_size=False, no_auto_bright=True,exp_shift=2.55, output_bps=16)
        rgb = np.float32(rgb / 65535.0*255.0)
        rgb = np.asarray(rgb,np.uint8)
        imageio.imsave('./jpgready'+'/'+file[:-4]+'.jpg', rgb)
print('All ready!')
