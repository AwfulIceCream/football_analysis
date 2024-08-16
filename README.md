# Football Analysis Project
This project aims to detect and track players, referees, and footballs in a video using YOLO, a leading AI object detection model. We will train the model to enhance its performance further. Additionally, we will employ K-means clustering for pixel segmentation to assign players to teams based on their jersey colors. This segmentation will allow us to calculate each team's ball acquisition percentage during a match.
To measure player movement accurately, we will use optical flow to account for camera movement between frames. By implementing perspective transformation, we can adjust for scene depth and perspective, enabling us to measure player movements in meters instead of pixels. Finally, we will calculate each player's speed and the distance covered. This comprehensive project addresses real-world challenges and is suitable for both beginners and experienced machine learning engineers.
## The input video looks like this:
![Alt Text](https://github.com/AwfulIceCream/football_analysis/blob/main/results_pics/input_video%20-%20frame%20at%200m0s.jpg)
## And then, after processing, the output looks like this:
![Alt Text](https://github.com/AwfulIceCream/football_analysis/blob/main/results_pics/output_video%20-%20frame%20at%200m0s.jpg)
## Features

- Object detection and tracking using YOLO
- Player team assignment using K-means clustering
- Ball acquisition percentage calculation
- Optical flow for camera movement compensation
- Perspective transformation for accurate distance measurement
- Calculation of player speed and distance covered

### Used technologies

- Python 3.x
- PyTorch
- OpenCV
- NumPy
- Scikit-learn

## Contact

For questions or feedback, feel free to reach out to:

- Andrii - [Your Email](mailto:andrii.myrosh.shi.2022@lpnu.ua)
- Project Link: [GitHub Repository](https://github.com/AwfulIceCream/football_analysis)

---
