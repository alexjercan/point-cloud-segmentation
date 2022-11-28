# Point Cloud Segmentation

## TODO

- [x] exploratory data analysis
    - [x] try to import challenge src
    - [x] distribution of the classes for train set, test not available
    - [x] try to plot some of the points, maybe using knn to sample objects
    - [x] how was the lidar sensor used and which positions are used for train and test set
    - [x] Compute the overlapping of the train and test points (output train labels for the overlapping ones)
        - I guess the test files were choosen so that there is no overlapping between train and test

- [ ] implementations
    - [x] PyTorch Dataset
    - [x] PointNet++
    - [ ] Point Cloud Transformer
    - [ ] Compare the two implementations
