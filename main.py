import platform
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth



scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.appdata']

device_id = platform.node()

def get_access():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return create_folder_and_sheet(drive)
 

def create_folder_and_sheet(drive):
    folder_name = 'Учет абонементов'
    folder = drive.CreateFile({'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'})
    folder.Upload()

    folder_id = folder.get('id')
    sheet_create = drive.CreateFile({'parents': [{'id': folder_id}], 'title': device_id,
                                     'mimeType': 'application/vnd.google-apps.spreadsheet'})

    sheet_create.Upload()
    return sheet_create