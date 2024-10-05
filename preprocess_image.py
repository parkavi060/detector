import cv2
import os

# Function to preprocess images
def preprocess_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through images in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Read the image
        image = cv2.imread(input_path)

        # Check if the image is valid
        if image is None:
            print(f"Error: Unable to read image {input_path}")
            continue

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply any other preprocessing steps as needed
        # For example, you can resize the image, equalize histogram, etc.

        # Write the preprocessed image to the output folder
        cv2.imwrite(output_path, gray_image)
        print(f"Preprocessed image saved: {output_path}")

# Example usage
input_folder = "Harish"
output_folder = "preprocessed_images"
preprocess_images(input_folder, output_folder)
