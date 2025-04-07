from datetime import datetime;
from pi_camera_automation import make_and_send_picture
from crop_picture import crop_picture

def main():
   
    # Here, access to the Raspberry Pi is established, and the picture is taken.
    # The picture is then saved locally here with the name my_filename
    
    
    number= str(input("[INPUT] Please enter the GW number: "))
    scenario = str(input("[INPUT] Please enter the scenario: "))
    test = str(input("[INPUT] Setup correct? (0,075 // 4): "))
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
        picture_name =f"{current_time}__GW_{number}_{scenario}_{version}.jpg"
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


if __name__ == "__main__":
    main()