import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        
        allFiles = os.walk(file_from)
        for root, directories, files in allFiles:
            for fil in files:
                start = file_from
                filePath = os.path.join(root, fil)
                f = open(filePath, "rb")
                relative_path = os.path.relpath(filePath, start)
                file_path_upload = os.path.join(file_to, relative_path)
                file_path_upload = file_path_upload.replace("\\", "/")
                dbx.files_upload(f.read(), file_path_upload)
                print(fil, " Uploaded Successfully")

def main():
    access_token = "xRWyVvEDPp8AAAAAAAAAAQcX6c39_jGvHWkV1phFEDcVvqVG1Vj1te0cyVDzn9ic"

    transferdata = TransferData(access_token)

    file_from = input("Enter the folder path upload files: ")
    file_to = input("Enter the name of the path and give / before name, to upload files: ")

    if(os.path.exists(file_from)):
        if(file_to == ""):
            print("File name for the dropbox is empty")
        else:
            transferdata.upload_files(file_from, file_to)
    else:
        print("File Not Found")
        

main()