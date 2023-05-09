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
1. Data preprocessing: 
    1. We construct the data structure to fulfill the YOLO requirement 
    2. We enhanced the wider face dataset by using super resolution
2. Training:
    1. We finetuned Yolov8 model for face detection.
    2. Train with enhanced images
    3. Train with transformer
    4. Train with both enchanced images and transformer
3.  Testing and Evaluation:
    1. Predicting results using all the models (4 models)
    2. Evaluate all the models.


<details open>
<summary>Data Processing</summary>

```bash
python
yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
```

</details>

<details open>
<summary>Training</summary>

```bash
python
yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
```

</details>

</details>

<details open>
<summary>Testing and Evaluation</summary>

```bash
python
yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
```

</details>
