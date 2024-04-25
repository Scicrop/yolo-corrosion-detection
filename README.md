# yolo-corrosion-detection
Basic example of how to train and detect rust corrosion with yolo v7.
This code is nothing more than a group of scripts that automate the training and detection tasks using yolo. Actually the folder *yolov7* is basically the repository of yolo project found here: https://github.com/WongKinYiu/yolov7

Another thing important to mention is that this project uses a dataset of rust corrosion images from Roboflow. The dataset is automatically downloaded in the first run, and located at yolov7/Rust8-2 folder. The original dataset can be found here: https://universe.roboflow.com/trailrun/datasetnew-n7bra

## Dependencies
 - Python >= 3.8
 - Poetry >= 1.8
 - Git

## How to run (It is easy!)

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
