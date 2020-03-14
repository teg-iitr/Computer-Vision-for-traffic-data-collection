# Computer-Vision-for-traffic-data-collection
## part 1. Introduction
Implementation of YOLO v3 object detector in Tensorflow for classified detection of vehicals

YOLO paper is quiet hard to understand, along side that paper. This repo enables you to have a quick understanding of YOLO Algorithmn.


## part 2. Quick start
1. Clone this file
2.  You are supposed  to install some dependencies before getting out hands with these codes.
bashrc
$ cd tensorflow-yolov3
$ pip install -r ./docs/requirements.txt

3. Exporting loaded COCO weights as TF checkpoint(`yolov3_coco.ckpt`)【[BaiduCloud](https://pan.baidu.com/s/11mwiUy8KotjUVQXqkGGPFQ&shfl=sharepset)】
bashrc
$ cd checkpoint
$ https://drive.google.com/file/d/1n3BShKTwnVgEm462YLHDOPWrQvedUUiW/view?usp=sharing 
$ tar all the .zip files
$ cd ..
$ python convert_weight.py
$ python freeze_graph.py

4. Then you will get some `.pb` files in the root path.,  and run the demo script
bashrc
$ python image_demo.py
$ python video_demo.py # if use camera, set video_path = 0


## part 3. Train your own dataset
Two files are required as follows:


xxx/xxx.jpg 18.19,6.32,424.13,421.83,20 323.86,2.65,640.0,421.94,20 
xxx/xxx.jpg 48,240,195,371,11 8,12,352,498,14
image_path x_min, y_min, x_max, y_max, class_id  x_min, y_min ,..., class_id 
make sure that x_max < width and y_max < height

Class names are required as follows:


person
bycycle
twowheeler
truck
car
autorickshaw
bus


### 3.1 Train IDD(Indian Driving Dataset) 
To help you understand my training process, I made this demo of training IDD dataset
#### how to train it ?
Download IDD trainval  and test data
bashrc

$ https://idd.insaan.iiit.ac.in/accounts/login/?next=/dataset/download/

Download IDD Dataset from this link -

##### (1) train from COCO weights(recommend):
Don't try to train from skretch as it will require computational power and will take masside amount of time
bashrc
$ cd checkpoint
$ downloads weights from yolov3_coco.tar.gz
$ tar -xvf yolov3_coco.tar.gz
$ cd ..
$ python convert_weight.py --train_from_coco
$ python train.py


#### how to test and evaluate it ?

$ python evaluate.py
$ cd mAP
$ python main.py -na


### 3.2 Train other dataset
Download COCO trainval  and test data

$ wget http://images.cocodataset.org/zips/train2017.zip
$ wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
$ wget http://images.cocodataset.org/zips/test2017.zip
$ wget http://images.cocodataset.org/annotations/image_info_test2017.zip 
