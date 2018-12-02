# SpottedPoster
# This file is part of the spottedPoster distribution (https://github.com/horstmannmat/spottedPoster).
# Copyright (C) 2018 Matheus Horstmann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Shows basic usage of the Drive v3 API.

Creates a Drive v3 API service and prints the names and ids of the last 10 files
the user has access to.
"""
from __future__ import print_function
import os
import io
from apiclient.http import MediaIoBaseDownload
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import csv

f = open('sensitive_spreadSheet_data.txt', 'r')
file_id= f.readline().rstrip()
f.close()

#Create file if not exist
if os.path.exists("spottedOld.tsv"):
    pass
else:
    open("spottedOld.tsv","w").close()

# Setup the Drive v3 API
store = file.Storage('credentials.json')
SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
drive_service = build('drive', 'v3', http=creds.authorize(Http()))

# Download spreadSheet from google
request = drive_service.files().export_media(fileId=file_id,mimeType='text/csv')
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()

print("Finished download")

#write the new file
with open("spottedOld.csv","w") as f:
    wrapper = str(fh.getvalue().decode("utf-8"))
    csv_file = csv.reader(io.StringIO(wrapper))
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csv_file:
        if (row[1] !=  '' ):
            w.writerow(row)

    # f.write('\n'.encode('utf-8',errors='strict'))


open("spottedDiff.csv", "w").close()
open("spottedNew.csv", "w").close()
