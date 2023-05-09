# COSC6373-Team6
This is the final project of Team 6 in Computer Vision

First, we have to create an anaconda environment installed with required libraries for our porject.

<details open>
<summary>Install</summary>
  
```
conda create -n team6 -c notebook nb_conda_kernels
conda activate team6
pip install requirements.txt
```

</details>

Our project have several steps, so we separate all the code to three folders: DataProcessing, Training, Testing
(We suggest not running data processing and training cuase it would take a long time)
1. Data Processing: 
    1. Construct the data structure to fulfill the YOLO requirement 
    2. Enhance the heavy blur images in wider face dataset by using super resolution
2. Training:
    1. We finetuned Yolov8 model for face detection.
    2. Train with enhanced images
    3. Train with transformer
    4. Train with both enchanced images and transformer
    5. Train with transformer using 100 epochs
    6. Train with transformer using 300 epochs
3.  Testing and Evaluation:
    1. Predicting results using all the models (6 models)
    2. Evaluate all the models.

## <div align="center"></div>

<details close>
<summary>Data Processing</summary>

clone the this repository
```bash
cd DataProcessing
git clone https://github.com/sczhou/CodeFormer
cd CodeFormer
```
Then install more libraries
 ```bash
pip3 install -r requirements.txt
python basicsr/setup.py develop
conda install -c conda-forge dlib (only for face detection or cropping with dlib)
```

1. Preparing data:
Find all the heavy blur images in train and val dataset, and put them in a new folder. Which will run the process file through terminal, to download WilderFace data and prepare the data for enhancement. It takes time.
 ```bash
python ../widerface.py
```
2. Run Super Resolution (It will take forever.)
 ```bash
python inference_codeformer.py -w 0.7 --input_path ./train_heavy_blur --bg_upsampler realesrgan --face_upsample --output_path ./train_enhanced
python inference_codeformer.py -w 0.7 --input_path ./val_heavy_blur --bg_upsampler realesrgan --face_upsample --output_path ./val_enhanced
```
3. Resize the enhanced image to their original size
 ```bash
python ../resize.py
```
4. Prepare YOLO style files
 ```bash
python ../yolov7_train_face_data_preparation.py
```
This will generate folders "train" "val" in the data/widerface and the widerface.yaml
compress "train","val" folder as well as widerface.yaml to a zip file, this will be used for training.
5. Prepare YOLO style enhanced files for training
```bash
python ../enhanced_widerface.py
```
this will copy the enhanced images to the train,val images files, compress them like the previous step, this will be used for training.

6. Prepare WiderFace style WIDER_val/images with enhanced file
```bash
  python ../wilderface_val_enhance.py 
```
this will copy the enhanced val images to the WIDER_val/images, compress it for testing.
  
</details>

## <div align="center"></div>

<details close>
<summary>Training</summary>

```bash
python
yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
```

</details>

## <div align="center"></div>

<details open>
<summary>Testing and Evaluation</summary>

```bash
# Go to Testing folder
cd Testing
``` 
We have two validation sets in this folder for evaluation:

| Data sets| Description | 
| ---------------------- | --------------------- |
| WIDER_val | the original validation data of Wider Face |
|WIDER_val_enhanced | the enhanced validation data of Wider Face |
  
As mentioned, we have several model weights in this folder:
  
| Model weights| Description | 
| ---------------------- | --------------------- |
| yolov8_30.pt | model trained on original train data for 30 epochs |
| yolov8_30_enhanced.pt | model trained on enhanced train data for 30 epochs |
| yolov8_30_transformer.pt | |
| yolov8_30_transformer_enhanced.pt | |
| yolov8_100_transformer.pt | |
| yolov8_300_transformer.pt | |

Therefore, we have 6 result folders

| Result folder | Description | 
| ---------------------- | --------------------- |
| yolov8_30_output | model trained on original train data for 30 epochs |
| yolov8_30_enhanced_output | model trained on enhanced train data for 30 epochs |
| yolov8_30_transformer_output | |
| yolov8_30_transformer_enhanced_output | |
| yolov8_100_transformer_output | |
| yolov8_300_transformer_output | |

## To test the result from pre-trained model
1. Run the test.py to get output
Format: python test.py -model 'path for the weight' -input 'path for input images' -output 'output path'

```bash
#example1: testing on the yolov8_30.pt with original validation data and output to yolov8_30_output
python test.py -model yolov8_30.pt -input WIDER_val/images/ -output yolov8_30_output/

#example2: testing on the yolov8_30_enhanced with enhanced validation data and output to yolov8_30_enhanced_output/
python test.py -model yolov8_30_enhanced.pt -input WIDER_val_enhanced/images/ -output yolov8_30_enhanced_output/
```
  
2.  Show one result, note that it takes about 30ms for one image, exit by press any key.
Format: python test_single_img.py -model 'weight path' -img 'image path'
```bash
#example: 
python test_single_img.py -model yolov8_30.pt -img WIDER_val/images/0--Parade/0_Parade_marchingband_1_20.jpg

```
  
## To evaluate the predicted result on widerface
  
We will use the code from https://github.com/derronqi/yolov7-face/tree/main/widerface_evaluate
  
```bash
#step1. Get in the widerface_evaluate folder
cd widerface_evaluate

#step2. Build the code
python setup.py build_ext --inplace

#step3. run the evaluation
# format: python3 evaluation.py -p 'predict result path' -g 'ground_truth path'

python evaluation.py -p ../widerface_result_txt -g ground_truth
```


</details>
