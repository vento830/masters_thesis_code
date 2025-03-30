
from datetime import datetime;
from call_to_pi import make_and_send_picture
from bild_verkleinern import crop_picture
def main():
   
    #hier wird der zugriff zum Raspberry Pi erstellt und das Bild aufgenommen. Das bild wird danach hier Lokal mit dem Namen my_filename gespeichert
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    number= str(input("Bitte geben Sie die Nummer des GW ein: "))
    version = str(input("Bitte geben Sie die Version des GW ein: "))
    picture_name =f"GW_{number}_{version}_{current_time}.jpg"
    
    make_and_send_picture(
        hostname="172.22.132.18",
        username="pirag",
        password="Omni123",
        my_filename=picture_name,
        remote_command_template="""
        cd /home/pirag/MAA
        source .venv/bin/activate
        python camera_activation.py {filename}""",
        
    )
    crop_picture(picture_name)





if __name__ == "__main__":
    # Startpunkt - ruf unsere Hauptfunktion auf
    main()