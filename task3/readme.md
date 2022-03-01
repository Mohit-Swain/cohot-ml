### Task 3 consists:

    Aim: To create a neural network model of the highest accuracy, with the least number of parameters


    process:
             -Load the dataset from a given folder
             -Create all the image pre-processing steps
             -Create a Neural network model using Keras and train the model on the training dataset
             -Test the model on the test dataset



### Library used:

    1. Keras
    2. Tensorboard
    3. Numpy
    4. OpenCv
    5. Pandas
    4. Matplotlib
    5. Os

### Output:

    1. Trained the model with:

        - 2 Hidden Dense Layers
        - 2 Dropout Layers
        - 1 Output layer


!![ann-cat-dog](https://user-images.githubusercontent.com/43781668/156106012-21e328aa-7825-4455-8a73-b62cacae8153.png)

    With Total 133,281 parameters and 100 epochs :

        - Accuracy = 58.8%
        - Val_Accuracy = 61.19%




    1. Trained same model with:
       - 4 Convolution layers
       - 2 Maxpooling layers
       - 1 Flatten layer
       - 1 Dense layer
       - 1 Output layer

![cnn-cat-dog](https://user-images.githubusercontent.com/43781668/156106791-64abbcb7-17dd-4532-a5fc-1817f239e6d8.png)

    With Total 1,132,577 parameters and 25 epochs :

        - Accuracy = 78.31%
        - Val_Accuracy = 77.1%

## Summary

    a. The ANN Model that trained with 133,281 parameters achieved 58.8% Accuracy

    b. The CNN Model trained with 125,314 parameters achieved 78.31% Accuracy





