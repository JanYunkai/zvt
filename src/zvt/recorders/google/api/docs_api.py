# -*- coding: utf-8 -*-

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import httplib2


SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
DOCUMENT_ID = ""

class GoogleDocs:

    def __init__(self, apikey, documentId, proxy_ip=None, proxy_port=None):
        self.apikey = apikey

        p = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP, proxy_ip, proxy_port, 
            proxy_user=None, proxy_pass=None)
        http = httplib2.Http(proxy_info = p)
        self.documentId = documentId
        self.service = build("docs", "v1", http = http, developerKey=apikey)

    def get(self):
        doc = self.service.documents().get(documentId=self.documentId).execute()
        print(doc)