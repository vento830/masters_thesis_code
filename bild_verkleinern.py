import cv2
import os
def crop_picture(image_path):
    
    print(f"Öffne Bild: {image_path}")
    # Bild einlesen
    image = cv2.imread(f"backup/{image_path}")
    # Falls das Bild nicht eingelesen werden konnte, Programm beenden
    if image is None:
        print("Bild konnte nicht eingelesen werden. Überprüfe den Dateipfad.")
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

    #print(f"Neues Bild wird gespeichert unter: {image_path}")
    print(f"Breite: {width}, Höhe: {height}")
    cv2.imwrite(f"pic_folder/{new_image_path}", cropped_image)
