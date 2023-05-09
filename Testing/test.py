#test with pretrained model
from ultralytics import YOLO
import argparse
import torchvision.datasets as datasets
from torchvision.transforms import ToTensor
import os
import time

#weights: model weights
#img_size:inference size
#conf_thres: object confidence threshold
#iou_thres: IOU threshold
#device
def test_wilderface(model,dataset_folder,save_folder,img_size=640,conf_thres=0.01,iou_thres=0.5,augment=False,device='cpu'):
    # testing dataset
    testset_folder = dataset_folder
    testset_list = dataset_folder[:-7] + "wider_val.txt"
    with open(testset_list, 'r') as fr:
        test_dataset = fr.read().split()
        num_images = len(test_dataset)
    for img_name in test_dataset:
        #print(testset_folder)
        image_path = testset_folder + img_name
        #print(image_path)
        results = model.predict(source=image_path, imgsz=img_size, conf=conf_thres, iou=iou_thres, augment=augment, device=device)

        save_name = save_folder + img_name[:-4] + ".txt"
        dirname = os.path.dirname(save_name)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        with open(save_name, "w") as fd:
            result = results[0].cpu().numpy()
            file_name = os.path.basename(save_name)[:-4] + "\n"
            bboxs_num = str(result.boxes.shape[0]) + '\n'
            fd.write(file_name)
            fd.write(bboxs_num)
            for box in result.boxes:
                conf = box.conf[0]
                cls  = box.cls[0]
                xyxy = box.xyxy[0]
                x1 = int(xyxy[0] + 0.5)
                y1 = int(xyxy[1] + 0.5)
                x2 = int(xyxy[2] + 0.5)
                y2 = int(xyxy[3] + 0.5)
                fd.write('%d %d %d %d %.03f' % (x1, y1, x2-x1, y2-y1, conf if conf <= 1 else 1) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-model', '--model', default="./yolov8_30.pt")
    parser.add_argument('-input',  '--input',default='./')
    parser.add_argument('-output', '--output', default='./output/')

    args = parser.parse_args()
    # Load a model
    model = YOLO(args.model)  # load the best model
    
    val_path = args.input

    #if not assign input download the widerface
    if args.input == './':
        val_data = datasets.WIDERFace(
        root = 'data', 
        split = 'val', 
        transform = ToTensor(),
        download = True
        )
        val_path = './data/widerface/WIDER_val/images/'
    

    #prepare wider_val.txt for testing
    rootdir = val_path
    with open(val_path[:-7] + '/wider_val.txt', 'w') as f:
        for file in os.listdir(rootdir):
            if(file[0] == '.'):
                continue
            #print(file)
            d = os.path.join(rootdir, file)
            for img in os.listdir(d):
                f.write(file+'/'+img + os.linesep)

    start = time.time()
    test_wilderface(model,val_path,args.output)
    end = time.time()
    print(str(args.model) + " test time:" + str(end-start))