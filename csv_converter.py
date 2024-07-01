import os
import pandas as pd

def create_csv(image_dir, output_csv):
    image_files = []
    for root, _, files in os.walk(image_dir):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                image_files.append(os.path.join(root, file))
    
    print(f"Found {len(image_files)} images in {image_dir}")
    
    if len(image_files) == 0:
        print(f"No images found in {image_dir}")
    else:
        df = pd.DataFrame(image_files, columns=["filepath"])
        df.to_csv(output_csv, index=False)
        print(f"CSV file created at {output_csv}")

# Ensure the output CSV paths point to actual files, not directories
positive_dir = "C:/Users/cmmill28/2d-image-classification/dataset/validation/positive"
negative_dir = "C:/Users/cmmill28/2d-image-classification/dataset/validation/negative"
positive_csv = "C:/Users/cmmill28/2d-image-classification/dataset/validation/positive_samples.csv"
negative_csv = "C:/Users/cmmill28/2d-image-classification/dataset/validation/negative_samples.csv"

print("Creating CSV for positive images...")
create_csv(positive_dir, positive_csv)

print("Creating CSV for negative images...")
create_csv(negative_dir, negative_csv)
