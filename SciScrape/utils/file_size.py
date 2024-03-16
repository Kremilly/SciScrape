#!/usr/bin/python3

import os, requests

class FileSize:

    @classmethod
    def format(self, bytes, units=[ ' bytes','KB','MB','GB','TB', 'PB', 'EB' ]):
        return str(bytes) + units[0] if bytes < 1024 else self.format(
            bytes >> 10, units[1:]
        )

    @classmethod
    def local_file(self, file):
        file_size = os.stat(file)
        return self.format(file_size.st_size)

    @classmethod
    def remote_file(self, url):
        try:
            req_headers = requests.get(url)
            
            return self.format(
                int(req_headers.headers["Content-Length"])
            )
        except:
            return None
