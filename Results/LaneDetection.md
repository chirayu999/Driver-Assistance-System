# Results

The lane departure algorithms consits a series of preprpcessing steps to a frame

## Input image
![](https://i.imgur.com/6rKHZiV.png)

## After applying the mask over Region Of Interest
![](https://i.imgur.com/ZzFXVlG.png)

## When this image is passed through image threshold, only lane markings will be visible
![](https://i.imgur.com/zDjJEuV.png)

## Canny edge detector is used to find the edge points after image thresholding
![](https://i.imgur.com/jD79C9r.png)

## Finally, Hough transform is used to determine edges in the original image
![](https://i.imgur.com/PPwvPTi.png)






