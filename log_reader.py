
from io import SEEK_END, SEEK_CUR
import re

class LogReader:
    LogFolder = '/var/log/'
    BlockSize = 2048

    def __init__(self, log_name):
        self.log_name = LogReader.LogFolder + log_name

    def _filter_log(self, logs, fter):
        pattern = re.compile(fter)

        match = []

        for item in logs:
            if pattern.search(item):
                match.append(item)

        return match

    def read_log(self, entries, fter):
        out = []

        try:
            handle = open(self.log_name, 'rb')
            handle.seek(0, SEEK_END)
            size = handle.tell()
            buf = ""

            while size > 0 and len(out) < entries:
                shift = LogReader.BlockSize if size > LogReader.BlockSize else size
                handle.seek(-shift, SEEK_CUR)
                read_bytes = handle.read(shift)
                handle.seek(-shift, SEEK_CUR)

                content = read_bytes.decode('utf-8') + buf
                lines = content.splitlines()

                for i in range(len(lines) - 1, 0, -1):
                    out.append(lines[i])

                size -= shift

                if size == 0:
                    out.append(lines[0])
                else:
                    buf = lines[0]

            handle.close()
        except FileNotFoundError as e:
            print("not found")
            raise e
        except PermissionError as e:
            print("no permission")
            raise e
        except IsADirectoryError as e:
            print("specified file is not readable")
            raise e
        except Exception as e:
            print(str(e))
            raise e

        return self._filter_log(out[:entries], fter)
