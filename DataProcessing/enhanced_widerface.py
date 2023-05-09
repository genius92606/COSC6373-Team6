

import shutil
import os

#copy enhanced image to the path.
def func(src_file_path,dst_file_path):
    for img_name in  os.listdir(src_file_path):
        print(img_name)
        src_path = src_file_path + '/' + img_name
        dst = dst_file_path + '/' + img_name
        shutil.copy(src_path,dst)

resized_train_path = './train_enhanced/final_resized'
dst_path = './data/widerface/train/images'

resized_val_path = './val_enhanced/final_resized'
dst_val_path = './data/widerface/val/images'

func(resized_train_path,dst_path)
func(resized_val_path,dst_val_path)
