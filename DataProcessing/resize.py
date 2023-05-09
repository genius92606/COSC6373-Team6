#resize the enhanced image to it's original size
from PIL import Image
import os

def resize(path,enhanced_path,resized_path):
    if not os.path.exists(os.getcwd() + '/' + resized_path):
    # Create a new directory because it does not exist
        os.makedirs(os.getcwd() + '/' + resized_path)
  
    for img_name in os.listdir(path):
        img_name = img_name[:-4]
        img = Image.open(os.getcwd() + '/' + path + '/' + img_name + '.jpg')
        size = img.size
        enhance_path = os.getcwd() + '/' + enhanced_path + '/' + img_name + '.png'
        enhanced_img = Image.open(enhance_path)
        enhanced_img = enhanced_img.resize(size)
        enhanced_img.save(os.getcwd() + '/' + resized_path + '/' + img_name + '.jpg')

origin_train_path = './train_heavy_blur'
enhanced_train_path = 'train_enhanced/final_results'
resized_train_path = 'train_enhanced/final_resized'
origin_val_path = './val_heavy_blur'
enhanced_val_path = 'val_enhanced/final_results'
resized_val_path = 'val_enhanced/final_resized'

resize(origin_train_path,enhanced_train_path,resized_train_path)
resize(origin_val_path,enhanced_val_path,resized_val_path)