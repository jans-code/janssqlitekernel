#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
from pexpect import replwrap

sqlitewrapper = replwrap.REPLWrapper("sqlite3", "sqlite> ", None)

class janssqlitekernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.10.0'
    language = 'sqlite3'
    language_version = '3.40.1'
    language_info = {
        'name': 'sqlite3',
        'mimetype': 'application/sql',
        'file_extension': '.sql',
    }
    banner = "SQLite 3\nConnected to a transient in-memory database.\n"\
             "Use .open FILENAME to reopen on a persistent database."

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            if (code[0:5] == ".quit"):
                solution = f'"{code}" is now allowed in the SQLite kernel'
            else:
                code = code.replace("\n"," ")
                solution = sqlitewrapper.run_command(code)
                if solution.strip() == "":
                    solution = "Query OK"
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
