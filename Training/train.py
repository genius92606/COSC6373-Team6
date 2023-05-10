import torch
from ultralytics import YOLO
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

if __name__ == '__main__':
	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open('data.yaml', 'w') as f:
		f.write('train: ' + dir_path.replace(os.sep, '/') + '/data/train/images/\n')
		f.write('val: ' + dir_path.replace(os.sep, '/') + '/data/val/images/\n')
		f.write('nc: 1\n')
		f.write('names: [\'face\']\n')
	
	model_v8= YOLO("yolov8_TR.yaml").load('yolov8n.pt')  # build a new model from scratch
	model_v8.train(data='data.yaml', epochs=300, imgsz=640,batch=8, amp=False)

