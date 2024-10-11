# Project 3: Camera Calibration and Perception

## ENPM673: Perception for Autonomous Robots

### Contents of the Project

1. `Question_1.py`: Code to solve the first question (Camera calibration or other image processing tasks).
2. `Question_2.py`: Code to solve the second question.
3. `Terminal_Output_1.png`: Screenshot of the terminal output for Question 1.
4. `Terminal_Output_2.png`: Screenshot of the terminal output for Question 2.
5. `README.md`: This README file.
6. `Calibration_Imgs` (folder): Contains the images used for camera calibration or other tasks.
7. `report.pdf`: This report provides a detailed explanation of the methodologies, experiments, and results obtained in Project 3: Camera Calibration and Perception.

---

## Prerequisites

- **Python**: Version 3.11.1
- **Editor**: Visual Studio Code or another IDE of your choice

### Python Libraries
Ensure you have the following libraries installed:

```python
import numpy as np
import cv2 as cv
import glob
import os
```

To install them, run:

```bash
pip install numpy opencv-python
```

---

## How to Run the Code

Follow these steps to execute the code:

1. Download and extract the project zip file.
2. Ensure the `Calibration_Imgs` folder is located in the same directory as the `.py` files.
3. Install Python 3.11.1 and the necessary libraries.
4. Open the project folder in your IDE (e.g., Visual Studio Code).
5. Run the scripts for each question:
   - For Question 1:
     ```bash
     python3 Question_1.py
     ```
   - For Question 2:
     ```bash
     python3 Question_2.py
     ```

---

## Results

### Question 1: Camera Calibration / Image Processing Task

Below is the terminal output and an image showing the results of running `Question_1.py`:

- **Terminal Output**:
  ![Terminal Output for Question 1](Terminal%20Output_1.png)

- **Sample Image**:
  If applicable, add a relevant image for Question 1's output here.

### Question 2: Another Image Processing Task

Below is the terminal output and an image showing the results of running `Question_2.py`:

- **Terminal Output**:
  ![Terminal Output for Question 2](Terminal%20Output_2.png)

- **Sample Image**:
  If applicable, add a relevant image for Question 2's output here.

---

## Notes

- Ensure that the `Calibration_Imgs` folder is not moved or altered, as the scripts depend on it to function correctly.
- If you encounter any issues with the `glob` or `os` libraries not locating files, ensure that the path to the images is correct and relative to the current working directory.

---

## Conclusion

This project demonstrates camera calibration and other image processing tasks using Python and OpenCV. By following the steps outlined above, you can run the scripts and see the outputs for each question. The report for the project can be viewed here. [![Project Report](https://img.icons8.com/ios-filled/30/ff2c2c/pdf.png)](report.pdf)