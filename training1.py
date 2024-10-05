import cv2
import os

def getImageID(path):
    # Function to get the ID and face data from images
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]  # Get all image paths
    faces = []
    IDs = []

    for imagePath in imagePaths:
        # Load the image and convert it to grayscale
        img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

        # Extract ID from file name
        fileName = os.path.basename(imagePath)
        try:
            Id = int(fileName.split('_')[1])  # Extracting the ID from the file name
        except (IndexError, ValueError):
            print(f"Error extracting ID from {fileName}. Skipping this image.")
            continue

        # Add face and ID to the lists
        faces.append(img)
        IDs.append(Id)

    return IDs, faces

# Example usage
path = "preprocessed_images"
IDs, facedata = getImageID(path)
print("IDs:", IDs)

