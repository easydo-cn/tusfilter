# -*-coding:utf-8 -*-
import os
import json


class Sessions:
    def __init__(self, session_dir='/var/session'):
        self.tmp = session_dir
        if not os.path.exists(session_dir):
            os.makedirs(session_dir)

    def _os_path(self, upload_session):
        return os.path.join(self.tmp, upload_session)

    def new(self, upload_session, device, key, **kwargs):
        session = {
            'device': device,
            'key': key,
        }
        session.update(kwargs)
        with open(self._os_path(upload_session), 'w') as f:
            json.dump(session, f)

    def load(self, upload_session):
        with open(self._os_path(upload_session)) as f:
            return json.load(f)

    def delete(self, upload_session):
        os.remove(self._os_path(upload_session))
