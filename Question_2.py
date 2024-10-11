import numpy as np
import cv2 as cv
import glob
import os

scale = 1                                                          # Global variable to store the scaling factor
objpoints = []                                                     # Real world 3D points
imgpoints = []                                                     # Image points

# Function to load and resize the image
def load_resize(img_path, ratio=0.3):
    global scale
    img = cv.imread(img_path)
    h, w = img.shape[:2]
    scale = ratio
    new_h = int(ratio * h)
    new_w = int(ratio * w)
    return cv.resize(img, (new_w, new_h))
    
# Function to scale the K matrix to the original image size
def K_matrix(mtx):
    scale_matrix = np.array([[1/scale, 0, 0], [0, 1/scale, 0], [0, 0, 1]])
    K= np.dot(scale_matrix, mtx)
    return K
    
# Path to the calibration images
CURRENT_DIR = os.path.dirname(__file__)
images_path = os.path.join(CURRENT_DIR,'Calibration_Imgs/*.jpg')

# Parameters for the calibration target
square_size = 21.5
pattern_size = (9, 6)

# Prepare object points for the calibration target
objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2) * square_size

# Getting the paths of Calibration Images
images = glob.glob(images_path)

for image in images:
    # Getting the Resized Image and converting it to grayscale
    img = load_resize(image,0.5)                                    # Change the scaling factor here(default: 0.3)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv.findChessboardCorners(gray, pattern_size, None)

    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)
        
        # Draw the corners on the image and display it
        cv.drawChessboardCorners(img, pattern_size, corners, ret)
        cv.imshow('img', img)
        cv.waitKey(200)

# Performing Camera Calibration
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print(f"\nScale: {scale}\n\n ** The following values are scaled to the original image size **\n")

# Calculating the Reprojection error for each image
for i in range(len(images)):
    rvec, tvec = rvecs[i], tvecs[i]
    projected_points, _ = cv.projectPoints(objpoints[i], rvec, tvec, mtx, dist)
    reprojection_error = cv.norm(imgpoints[i], projected_points, cv.NORM_L2)/len(projected_points)
    reprojection_error = reprojection_error / scale                 # Scaling the error to the original image size
    print(f'Reprojection error for image {i+1}: {reprojection_error}')
    
K = K_matrix(mtx)                                                   # Scaling the K matrix to the original image size
print(f"\nCamera matrix (K):\n {K} \n")
