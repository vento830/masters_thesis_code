import base64
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import langchain
#from langchain.chat_models import ChatOpenAI
#from langchain.schema.messages import HumanMessage, AIMessagee
def encode_image(image_path):
    """
    Encodes an image to base64 string.
    
    Args:
        image_path (str): Path to the image file.
        
    Returns:
        str: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def decode_image(encoded_string, output_path):
    """
    Decodes a base64 string to an image file.
    
    Args:
        encoded_string (str): Base64 encoded string of the image.
        output_path (str): Path to save the decoded image.
    """
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(encoded_string))
        print(f"[INFO] Decoded image saved to {output_path}")

#print(encode_image("pic_folder/2025-04-07_14-31-03__GW_2_TC3_v6_cropped.jpg"))



image_elements = []
for image_file in os.listdir("pic_folder"):
    if image_file.endswith(".jpg"):
        # Encode the image
        encoded_image = encode_image(f"pic_folder/{image_file}")
        # Append a tuple with the filename and the encoded image
        image_elements.append((image_file, encoded_image))
#print(len(image_elements))

#print(image_elements[21][1])
#print(image_elements[0][1])
#decode_image(image_elements[20][1], "decoded_image.jpg")

