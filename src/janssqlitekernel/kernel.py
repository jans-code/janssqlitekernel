#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
from pexpect import replwrap

special_commands = [".archive",".auth",".backup",".bail",".binary",
                    ".cd",".changes",".check",".clone",".connection",".databases",
                    ".dbconfig",".dbinfo",".dump",".echo",".eqp",".excel",
                    ".expert",".explain",".filectrl",".fullschema",".headers",
                    ".help",".import",".imposter",".indexes",".limit",".lint",
                    ".load",".log",".mode",".nonce",".nullvalue",".once",".open",
                    ".output",".parameter",".print",".progress",".prompt",
                    ".read",".recover",".restore",".save",".scanstats",
                    ".schema",".selftest",".separator",".sha3sum",".shell",
                    ".show",".stats",".system",".tables",".testcase",".testctrl",
                    ".timeout",".timer",".trace",".version",".vfsinfo",".vfslist",
                    ".vfsname",".width"]

exit_commands = [".exit", ".quit"]

sqlitewrapper = replwrap.REPLWrapper("sqlite3 -box", "sqlite> ", None)

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
            code = code.strip()
            check_code = code.split(" ")
            if check_code[0] not in special_commands:
                if code[-1] != ";":
                    code = code + ";"
            if check_code[0] in exit_commands:
                solution = check_code[0] + " command is not allowed in SQLite3 Kernel."
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
