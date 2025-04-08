import base64
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ollama import chat

import os
import langchain
#from langchain.chat_models import ChatOpenAI

vorlage = """1. General Description of the Gear
	•	Shape/Form: A round gear with evenly spaced teeth around the outer edge. In the center, there is a larger bore and four smaller bores arranged in a circular pattern around the center.
	•	Color/Material: Metallic appearance (silvery-gray), with no visible discoloration or signs of oxidation.
	•	Surface Structure: The surface appears smooth and reflects light evenly; there are no visible scratches or dents.
	•	Condition of the Teeth: The gear teeth are uniformly shaped with no signs of chipping or unusual indentations.

⸻

2. Categorization with Respect to Possible Defects
	1.	Tooth Clipping
	•	Observation: No broken or chipped gear teeth; all teeth are fully intact.
	•	Assessment: No evidence of clipping.
	2.	Surface Scratches
	•	Observation: The surface appears smooth with no visible lines, grooves, or scratches.
	•	Assessment: No surface scratches detected.
	3.	Wear Out
	•	Observation: The teeth appear uniform; no signs of excessive wear or erosion.
	•	Assessment: No wear observed.
	4.	Rust
	•	Observation: No rust or oxidation visible on the gears surface or in the bores.
	•	Assessment: Rust-free.
	5.	Production Errors
	•	Observation: The holes appear clean and symmetrical, and the overall shape seems precisely fabricated with no visible casting flaws or inaccuracies.
	•	Assessment: No production errors detected.
	6.	Dirt
	•	Observation: No dirt particles, residues, or other contaminants visible.
	•	Assessment: Clean and free of foreign matter.

⸻

3. Summary
	•	Overall Condition: This gear shows no damage, wear, or other anomalies.
	•	Defect Category: None (the component is intact).
	•	Conclusion: Based on the six listed categories (1 through 6), this gear can be clearly classified as defect-free."""

vorlage_1= """You are an inspection system for gears. Please fill out the following template based on the provided image.

Schema:
1. General Description of the Gear
   • Shape/Form: [Description here]
   • Color/Material: [Description here]
   • Surface Structure: [Description here]
   • Condition of the Teeth: [Description here]

2. Categorization with Respect to Possible Defects
   1. Tooth Clipping
      • Observation: [Observation]
      • Localization: [Location where the issue occurs]
      • Assessment: [Evaluation]
   2. Surface Scratches
      • Observation: [Observation]
      • Localization: [Location where the issue occurs]
      • Assessment: [Evaluation]
   3. Wear Out
      • Observation: [Observation]
      • Localization: [Location where the issue occurs]
      • Assessment: [Evaluation]
   4. Rust
      • Observation: [Observation]
      • Localization: [Location where the issue occurs]
      • Assessment: [Evaluation]
   5. Production Errors
      • Observation: [Observation]
      • Localization: [Location where the issue occurs]
      • Assessment: [Evaluation]
   6. Dirt
      • Observation: [Observation]
      • Localization: [Location where the issue occurs]
      • Assessment: [Evaluation]

3. Summary
   • Overall Condition: [Summary]
   • Defect Category: [Category or classification]
   • Conclusion: [Final statement or recommendation]

Use the following image description/text as the basis:

"""



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

full_path = os.path.abspath(f"pic_folder/{image_elements[10][0]}")

print(full_path)

response = chat(
  model='llava',
  messages=[
    {
      'role': 'user',
      'content': f" {vorlage_1}",
      'images': [image_elements[10][1]],
    }
  ],
)
#print(response.message.content)


#print(len(image_elements))

#print(image_elements[21][1])
#print(image_elements[0][1])
#decode_image(image_elements[20][1], "decoded_image.jpg")

#chain_gpt_4_vision = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=1024)

'''def process_image(image_file):
    with Image.open(image_file) as img:
        with BytesIO() as buffer:
            img.save(buffer, format="JPEG")
            image_bytes = buffer.getvalue()
    
    full_response= ""

    for response in generate(model='llava',
                             prompt= "describe the image",
                             images=[image_bytes],
                             stream=True):
        
        # Perform any image processing here
        img.save(buffer)'''
