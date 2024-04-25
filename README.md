# yolo-corrosion-detection
Basic example of how to train and detect rust corrosion with yolo v7.

## Dependencies
 - Python >= 3.8
 - Poetry >= 1.8

## How to run (It is easy!)

The first time you run, it will need to download the dataset and train the model. If you do not have a NVIDIA gpu it will take some hours to train the model. Once the model is trained you will able to run the code again and it will find the weights from the previous training, and then it will run the tests with the 10 images located in `test_images` folder.

```
$ git clone https://github.com/Scicrop/yolo-corrosion-detection
$ cd yolo-corrosion-detection
$ poetry run python app.py
```
