import torch
from ultralytics import YOLO
import argparse
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-option', '--option')
	args = parser.parse_args()
	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open('data.yaml', 'w') as f:
		f.write('train: ' + dir_path.replace(os.sep, '/') + '/data/train/images/\n')
		f.write('val: ' + dir_path.replace(os.sep, '/') + '/data/val/images/\n')
		f.write('nc: 1\n')
		f.write('names: [\'face\']\n')
	with open('data_enhanced.yaml', 'w') as f:
		f.write('train: ' + dir_path.replace(os.sep, '/') + '/data_enhanced/train/images/\n')
		f.write('val: ' + dir_path.replace(os.sep, '/') + '/data_enhanced/val/images/\n')
		f.write('nc: 1\n')
		f.write('names: [\'face\']\n')
	if args.option == 'yolov8_30':
		model = YOLO('yolov8n.pt')
		model.train(data='data.yaml', epochs=30, imgsz=640,batch=8, amp=False)
	elif args.option == 'yolov8_30_enhanced':
		model = YOLO('yolov8n.pt')
		model.train(data='data_enhanced.yaml', epochs=30, imgsz=640,batch=8, amp=False)
	elif args.option == 'yolov8_30_transformer':
		model= YOLO("yolov8_TR.yaml").load('yolov8n.pt')  # build a new model from scratch
		model.train(data='data.yaml', epochs=30, imgsz=640,batch=8, amp=False)
	elif args.option == 'yolov8_30_transformer_enhanced':
		model= YOLO("yolov8_TR.yaml").load('yolov8n.pt')  # build a new model from scratch
		model.train(data='data_enhanced.yaml', epochs=30, imgsz=640,batch=8, amp=False)
	elif args.option == 'yolov8_100_transformer':
		model= YOLO("yolov8_TR.yaml").load('yolov8n.pt')  # build a new model from scratch
		model.train(data='data.yaml', epochs=100, imgsz=640,batch=8, amp=False)
	elif args.option == 'yolov8_300_transformer':
		model= YOLO("yolov8_TR.yaml").load('yolov8n.pt')  # build a new model from scratch
		model.train(data='data.yaml', epochs=300, imgsz=640,batch=8, amp=False)
	
