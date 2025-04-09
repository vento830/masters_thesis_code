import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")





from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash-exp-image-generation",#models/gemini-2.0-flash-exp-image-generation   #gemini-2.0-flash-001
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)  


messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
ai_msg
#print(ai_msg)

import base64
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

pic2=encode_image("/Users/marv/MAA/masters_thesis_code/masters_thesis_code/pic_folder/2025-04-07_14-31-03__GW_2_TC3_v1_cropped.jpg")





smart_template_prompt = """


For each detected defect, provide the following information:
1. Observation – What is visible?
2. Localization – Precise location of the defect using:
   - Angle: measured from the center (like a clock dial, in degrees from 0° to 360°, where 0° is "up")
   - Radius: distance from the center to the defect (in pixels or millimeters)
3. Assessment – Evaluation of severity and potential impact

Output Format:

Detected Defects:
- [Defect Category Name]
  • Observation: [Short description]
  • Localization:
     - Angle: [e.g., 135°]
     - Radius: [e.g., 48 px]
  • Assessment: [Severity or action required]

Use the following definitions of defect categories to guide your interpretation:

Defect Categories:
1. **Tooth Clipping** – Partial or complete loss of gear teeth, often due to mechanical overload or wear. Typically results in noticeable gaps or breaks in the gear's outer profile.
2. **Surface Scratches** – Superficial lines or marks on the gear surface, possibly caused by handling or foreign particles. Generally cosmetic, but may indicate larger issues.
3. **Wear Out** – Progressive material loss due to friction and operation over time. Visible as smoothing or rounding of teeth and changes in contact pattern.
4. **Rust** – Oxidation due to moisture or poor storage. Appears as reddish or brown patches on the gear surface, can lead to structural weakening if untreated.
5. **Production Errors** – Manufacturing flaws such as casting bubbles, incorrect machining, or off-center holes. Usually identifiable by unusual shapes or asymmetries.
6. **Dirt** – Foreign material (dust, grease, particles) attached to the gear surface. May obscure real defects or affect the operation temporarily.



Your task: Use the definitions above to identify and describe only the relevant defect(s) using the format.
"""

prompt = f'''You are a gear wheel inspection system specialized in detecting and describing common gear defects. 
        Based on the second image, identify which defect categories are relevant in the first (target) image. Only describe those categories where a defect is actually detected. Ignore all other categories.
        Use the following template:
        {smart_template_prompt}'''
#print(prompt)
message = {
    "role": "user",
    "content": [
        {
            "type": "text",
            "text": f"{prompt}",
        },
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/png;base64,{pic2}"},
        },
    ],
}

response = llm.invoke(
    [message],
    generation_config=dict(response_modalities=["TEXT", "IMAGE"]),
)
print(response.content)