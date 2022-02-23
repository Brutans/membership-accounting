import platform
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.appdata']

def get_id():
    return get_access(platform.node())

def get_access(device_id):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive, device_id

