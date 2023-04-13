import os
import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog

def browse_input_folder():
    """Browse for input folder"""
    input_folder = filedialog.askdirectory()
    input_folder_label.config(text=input_folder)

def browse_output_folder():
    """Browse for output folder"""
    output_folder = filedialog.askdirectory()
    output_folder_label.config(text=output_folder)

def segment_plant(image):
    """Segment plant from background"""
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    

    lower_green = np.array([25, 40, 40])
    upper_green = np.array([95, 255, 255])
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    
    lower_brown = np.array([5, 40, 40])
    upper_brown = np.array([22, 255, 255])
    mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)


    mask = cv2.bitwise_or(mask_green, mask_brown)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    segmented_image = cv2.bitwise_and(image, image, mask=mask)
    return segmented_image

def process_images():
    """Process images in input folder and save to output folder"""
    input_folder = input_folder_label.cget("text")
    output_folder = output_folder_label.cget("text")

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)


            segmented_img = segment_plant(img)

            output_img_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_img_path, segmented_img)

    print("Processing complete.")

app = Tk()
app.title("Plant Image Preprocessing")

browse_input_button = Button(app, text="Browse Input Folder", command=browse_input_folder)
browse_input_button.grid(row=0, column=0)
input_folder_label = Label(app, text="")
input_folder_label.grid(row=0, column=1)

browse_output_button = Button(app, text="Browse Output Folder", command=browse_output_folder)
browse_output_button.grid(row=1, column=0)
output_folder_label = Label(app, text="")
output_folder_label.grid(row=1, column=1)

process_button = Button(app, text="Process Images", command=process_images)
process_button.grid(row=2, columnspan=2)

app.mainloop()
