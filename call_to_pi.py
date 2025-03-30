import paramiko

def make_and_send_picture(
    hostname,
    username,
    password,
    my_filename,  
    remote_command_template):
    # This function does the following:
    # 1) Establishes an SSH connection to the Raspberry Pi.
    # 2) Executes the script 'camera_activation.py' with an argument (filename).
    # 3) Downloads the file afterward (if it was created).
    
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        print(f"[INFO] Connect with Raspberry Pi")
        ssh_client.connect(hostname=hostname, username=username, password=password)

        # Befehl zusammensetzen: Wir ersetzen {filename} durch 'my_filename'
        remote_command = remote_command_template.format(filename=my_filename)
        
        print(f"[INFO] Execute code on the Raspberry Pi")
        stdin, stdout, stderr = ssh_client.exec_command(remote_command)

        exit_status = stdout.channel.recv_exit_status()
        
        out = stdout.read().decode('utf-8')
        err = stderr.read().decode('utf-8')

        if exit_status == 0:
            print("[INFO] Skript erfolgreich ausgeführt!")
        else:
            print(f"[WARN] Skript-Fehler (Exit-Code {exit_status}).")

        if out:
            #print("----- STDOUT -----")
            print(out)
        if err:
            print("----- STDERR -----")
            print(err)

        # Nun wird versucht, die Datei herunterzuladen (Pfad = /home/pirag/MAA/<my_filename>)
        remote_file_path = f"/home/pirag/MAA/{my_filename}"
        #print(f"[INFO] Lade Datei vom Raspberry Pi: {remote_file_path}")

        sftp = ssh_client.open_sftp()
        #sftp.get(remote_file_path, my_filename)
        #sftp.get(remote_file_path, f"pic_folder/{my_filename}")
        sftp.get(remote_file_path, f"backup/{my_filename}")
        sftp.close()

        print("[INFO] Picture succesfully locally stored")

    except Exception as e:
        print(f"[ERROR] Fehler beim Verbinden oder Ausführen: {e}")
    finally:
        ssh_client.close()
        print("[INFO] Connection to Raspberry Pi closed.")


