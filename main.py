from datetime import datetime;
from pi_camera_automation import make_and_send_picture
from crop_picture import crop_picture

def main():
   
    # Here, access to the Raspberry Pi is established, and the picture is taken.
    # The picture is then saved locally here with the name my_filename

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    number= str(input("[INPUT] Please enter the GW number: "))
    version = str(input("[INPUT] Please enter the version of the GW: "))
    picture_name =f"GW_{number}_{version}_{current_time}.jpg"
    
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