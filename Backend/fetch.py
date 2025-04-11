from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# === CONFIGURATION ===

SERVICE_ACCOUNT_FILE = 'D:\\Projects\\telecaller\\backend\\avid-influence-451503-v3-b0c64ccab032.json'
FILE_NAME = 'response.txt'
FOLDER_ID = '1mYtpp5m_RDrD7CLk8BbWLXAX0WIjcYRa'
LOCAL_DOWNLOAD_PATH = 'downloaded_response.txt'

# === AUTHENTICATION ===

SCOPES = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
drive_service = build('drive', 'v3', credentials=credentials)

# === SEARCH FOR FILE ===

query = f"'{FOLDER_ID}' in parents and name='{FILE_NAME}' and trashed = false"
results = drive_service.files().list(q=query, fields="files(id, name)").execute()
files = results.get('files', [])

if not files:
    print("❌ File not found in the specified folder.")
else:
    file_id = files[0]['id']
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(LOCAL_DOWNLOAD_PATH, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"⬇ Download progress: {int(status.progress() * 100)}%")

    print(f"✅ File downloaded as: {LOCAL_DOWNLOAD_PATH}")