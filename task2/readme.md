### Task 2 consists:

     1. Input:
          - input_dir (default='cat') : directory where input data are stored
          - csv_file_name (default='data_labels.csv') : path of the data_labels
          - output_dir (default='output') : directory where output will be stored

     2. Process:
    	    - Read all the images
    	    - Read the csv file and get the image label names and coordinates
    	    - Draw bounding boxes for every image, using the corresponding image's coordinates
    	    - Add labels for every image
    	    - Create another folder and save all the images

    3. Output:
    	    - Images with a bounding box and a label
    	    - New folder where all the new images are stored

### Modules used:

    1. opencv
    2. os
    3. pandas
    4. argparse

### Output:

    1. Images with a bounding box and a label

![SS1](https://user-images.githubusercontent.com/63935255/155831110-8a547749-5fde-4afb-9eff-a1f2caa8b78d.png)
![SS2](https://user-images.githubusercontent.com/63935255/155831122-fbf65af4-0a2e-4959-9550-e50bc073af9a.png)
![SS3](https://user-images.githubusercontent.com/63935255/155831130-4c3548cd-acc8-4e3d-b42f-055598774d3d.png)

    2. Generates a new folder named "outputs" where all the output images are stored
