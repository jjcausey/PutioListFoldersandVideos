#   Libraries

import putiopy

############################# User Specific ###########################

# Root Folder
root = 949053319 # INSERT YOUR ROOT FOLDER

# Token
PutioToken = 'Y4BHVXPBH5AV6A4UHLKM' # INSERT YOUR TOKEN

############################# User Specific ###########################

# List Folders in a Specified Folder and the Video Files in those Folders

def PutioMove2Root():
        files1 = client.File.list(root) 
        for file1 in files1:

            if file1.file_type == "FOLDER":
                print "Folder name is: " + file1.name
                files2 = client.File.list(file1.id)
                for file2 in files2:
                    if file2.file_type == "VIDEO":
                        print "     File is: " + file2.name
                        
client = putiopy.Client(PutioToken) # Instanciate Client Object

PutioMove2Root()



