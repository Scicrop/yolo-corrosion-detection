# yolo-corrosion-detection
Basic example of how to train and detect rust corrosion with yolo v7.
This code is nothing more than a group of scripts that automate the training and detection tasks using yolo. Actually the folder *yolov7* is basically the repository of yolo project found here: https://github.com/WongKinYiu/yolov7

Another thing important to mention is that this project uses a dataset of rust corrosion images from Roboflow. The dataset is automatically downloaded in the first run, and located at yolov7/Rust8-2 folder. The original dataset can be found here: https://universe.roboflow.com/trailrun/datasetnew-n7bra

**This content is part of SCICROP-ACADEMY learning series.**

## Dependencies
 - Python >= 3.8
 - Poetry >= 1.8
 - Git

## How to run: Training + Detection (It is easy!)

The first time you run, it will need to download the dataset and train the model. If you do not have a NVIDIA gpu it will take some hours to train the model. Once the model is trained you will able to run the code again and it will find the weights from the previous training, and then it will run the tests with the 10 images located in `test_images` folder.

```
git clone https://github.com/Scicrop/yolo-corrosion-detection
```
```
cd yolo-corrosion-detection
```
```
poetry run python app.py
```

## Detecting with Yolo
```
poetry run python yolov7/detect.py --weights runs/train/yolov7-corrosion2/weights/best.pt --source /tmp/rust3.mp4 --view-img
```
Make sure to pass the correct `best.pt` in **--weights** parameter, as well as the correct **--source** parameter path. The source can be images, videos or even urls of live video cameras.


## Results


https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/7af79f84-4642-4d7b-8d67-ac4b6dbc55a3


![rust0 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/3ae1b900-777e-41a2-b14f-ea1d91f621d2)
![rust1 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/d7054208-596a-4d9e-b36f-0bf1ae44100c)
![rust2 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/951ea20d-cf9c-4cae-860b-6a61bc75bdc2)
![rust3 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/9d0a0f3d-496c-4010-b090-a385df091c2c)
![rust4 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/f79952a6-e8a8-4687-96db-11d65f364c8d)
![rust5 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/7aa159fc-1db1-4235-9ade-0a6c301b7efd)
![rust6 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/79846bca-937f-4e27-bf47-5411e1320762)
![rust7 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/6df7fba0-5041-49ed-a542-374ec917f019)
![rust8 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/8b26fbb6-94cc-4b03-bcb3-331f7830e593)
![rust9 png_screenshot_26 04 2024](https://github.com/Scicrop/yolo-corrosion-detection/assets/692043/7cd366c4-0a5e-42b7-8992-c6879f3a7ef8)



