from datetime import datetime;
from pi_camera_automation import make_and_send_picture
#from crop_picture import crop_picture
import cv2
import os

def main():
   
    # Here, access to the Raspberry Pi is established, and the picture is taken.
    # The picture is then saved locally here with the name my_filename
    
    
    number= str(input("[INPUT] Please enter the GW number: "))
    scenario = str(input("[INPUT] Please enter the scenario: "))
    test = str(input("[INPUT] Setup correct? (0,125 // 4): "))
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    while( True ):
        #stopping = str(input("[INPUT] Do you want to stop the program? (yes/no): "))
        #if stopping =="y":
         #       break
         #v1: normal picture (oben 0,075 // unten 4)
         #v2: normal picture + rotation
         #v3: angled gear wheel
         #v4: gear wheel in hand
         #v5: no light
         #v6: no light + correct optical lightning (oben 0,075  // unten 2,4)
         #v7: blurred (oben 0,225  // unten 4)
         
        version = str(input("[INPUT] Please enter the version of the GW: "))
        picture_name =f"GW_{number}_{scenario}_{version}__{current_time}.jpg"
        make_and_send_picture(
            
            hostname="172.22.132.18",
            username="pirag",
            password="Omni123",
            my_filename=picture_name,
            remote_command_template="""
            cd /home/pirag/MAA
            source .venv/bin/activate
            python camera_activation.py {filename}""")
        
        crop_picture(picture_name)

def crop_picture(image_path):
    
    print("[INFO] Cropping image...")
    # Bild einlesen
    image = cv2.imread(f"backup/{image_path}")
    # Falls das Bild nicht eingelesen werden konnte, Programm beenden
    if image is None:
        print("Image could not be imported. Check the file path.")
        exit()
    # Höhe und Breite des Bildes auslesen
    height, width = image.shape[:2]
    # Beispielwerte für Abschneiden links und rechts (in Pixel)
    # oben + unten = 1648

    # links recht = 3824
    #werte für Abschneiden wheel only'
    #crop_top = 1230
    #crop_bottom = 2548- crop_top
    #crop_left = 2209
    #crop_right = 4372 -crop_left


    crop_top = 1230
    crop_bottom = 2548- crop_top
    crop_left = 2209
    crop_right = 4372 -crop_left
    cropped_image = image[crop_top:height - crop_bottom,
                        crop_left:width - crop_right]
    height, width = cropped_image.shape[:2]
    #print(f"Breite: {width}, Höhe: {height}")
    base, ext = os.path.splitext(image_path)
    new_image_path = f"{base}_cropped{ext}"

    cv2.imwrite(f"pic_folder/{new_image_path}", cropped_image)
    print("[INFO] Successfully cropped image!")

if __name__ == "__main__":
    main()