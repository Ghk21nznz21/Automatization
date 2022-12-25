''' Holds the wanted destination directions '''
import os
user_name = os.popen('whoami').readline().split("\n")[0]
TEXT = "Text_Folder"
text_extensions = [".txt"]
IMAGES = "Pictures"
images_extensions = [".jpg", ".png", ".jpeg"]
OFFICE = "Office_Folder"
office_extensions = [".odt", ".pdf", ".doc"]
