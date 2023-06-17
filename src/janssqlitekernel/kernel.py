#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
from pexpect import replwrap
from IPython.display import display, HTML

commands = ['.ARCHIVE', '.AUTH', '.BACKUP', '.BAIL', '.BINARY', '.CD', '.CHANGES', '.CHECK', '.CLONE', '.CONNECTION', '.DATABASES', '.DBCONFIG', '.DBINFO', '.DUMP', '.ECHO', '.EQP', '.EXCEL', '.EXPERT', '.EXPLAIN', '.FILECTRL', '.FULLSCHEMA', '.HEADERS', '.HELP', '.IMPORT', '.IMPOSTER', '.INDEXES', '.LIMIT', '.LINT', '.LOAD', '.LOG', '.MODE', '.NONCE', '.NULLVALUE', '.ONCE', '.OPEN', '.OUTPUT', '.PARAMETER', '.PRINT', '.PROGRESS', '.PROMPT', '.READ', '.RECOVER', '.RESTORE', '.SAVE', '.SCANSTATS', '.SCHEMA', '.SELFTEST', '.SEPARATOR', '.SESSION', '.SHA3SUM', '.SHELL', '.SHOW', '.STATS', '.SYSTEM', '.TABLES', '.TESTCASE', '.TESTCTRL', '.TIMEOUT', '.TIMER', '.TRACE', '.VFSINFO', '.VFSLIST', '.VFSNAME', '.WIDTH', 'ABORT', 'ACTION', 'ADD', 'AFTER', 'ALL', 'ALTER', 'ALWAYS', 'ANALYZE', 'AND', 'AS', 'ASC', 'ATTACH', 'AUTOINCREMENT', 'BEFORE', 'BEGIN', 'BETWEEN', 'BY', 'CASCADE', 'CASE', 'CAST', 'CHECK', 'COLLATE', 'COLUMN', 'COMMIT', 'CONFLICT', 'CONSTRAINT', 'CREATE', 'CROSS', 'CURRENT', 'CURRENT_DATE', 'CURRENT_TIME', 'CURRENT_TIMESTAMP', 'DATABASE', 'DEFAULT', 'DEFERRABLE', 'DEFERRED', 'DELETE', 'DESC', 'DETACH', 'DISTINCT', 'DO', 'DROP', 'EACH', 'ELSE', 'END', 'ESCAPE', 'EXCEPT', 'EXCLUDE', 'EXCLUSIVE', 'EXISTS', 'EXPLAIN', 'FAIL', 'FILTER', 'FIRST', 'FOLLOWING', 'FOR', 'FOREIGN', 'FROM', 'FULL', 'GENERATED', 'GLOB', 'GROUP', 'GROUPS', 'HAVING', 'IF', 'IGNORE', 'IMMEDIATE', 'IN', 'INDEX', 'INDEXED', 'INITIALLY', 'INNER', 'INSERT', 'INSTEAD', 'INTERSECT', 'INTO', 'IS', 'ISNULL', 'JOIN', 'KEY', 'LAST', 'LEFT', 'LIKE', 'LIMIT', 'MATCH', 'MATERIALIZED', 'NATURAL', 'NO', 'NOT', 'NOTHING', 'NOTNULL', 'NULL', 'NULLS', 'OF', 'OFFSET', 'ON', 'OR', 'ORDER', 'OTHERS', 'OUTER', 'OVER', 'PARTITION', 'PLAN', 'PRAGMA', 'PRECEDING', 'PRIMARY', 'QUERY', 'RAISE', 'RANGE', 'RECURSIVE', 'REFERENCES', 'REGEXP', 'REINDEX', 'RELEASE', 'RENAME', 'REPLACE', 'RESTRICT', 'RETURNING', 'RIGHT', 'ROLLBACK', 'ROW', 'ROWS', 'SAVEPOINT', 'SELECT', 'SET', 'TABLE', 'TEMP', 'TEMPORARY', 'THEN', 'TIES', 'TO', 'TRANSACTION', 'TRIGGER', 'UNBOUNDED', 'UNION', 'UNIQUE', 'UPDATE', 'USING', 'VACUUM', 'VALUES', 'VIEW', 'VIRTUAL', 'WHEN', 'WHERE', 'WINDOW', 'WITH', 'WITHOUT'] 

special_commands = ['.ARCHIVE', '.AUTH', '.BACKUP', '.BAIL', '.BINARY', '.CD', '.CHANGES', '.CHECK', '.CLONE', '.CONNECTION', '.DATABASES', '.DBCONFIG', '.DBINFO', '.DUMP', '.ECHO', '.EQP', '.EXCEL', '.EXPERT', '.EXPLAIN', '.FILECTRL', '.FULLSCHEMA', '.HEADERS', '.HELP', '.IMPORT', '.IMPOSTER', '.INDEXES', '.LIMIT', '.LINT', '.LOAD', '.LOG', '.MODE', '.NONCE', '.NULLVALUE', '.ONCE', '.OPEN', '.OUTPUT', '.PARAMETER', '.PRINT', '.PROGRESS', '.PROMPT', '.READ', '.RECOVER', '.RESTORE', '.SAVE', '.SCANSTATS', '.SCHEMA', '.SELFTEST', '.SEPARATOR', '.SESSION', '.SHA3SUM', '.SHELL', '.SHOW', '.STATS', '.SYSTEM', '.TABLES', '.TESTCASE', '.TESTCTRL', '.TIMEOUT', '.TIMER', '.TRACE', '.VFSINFO', '.VFSLIST', '.VFSNAME', '.WIDTH']

exit_commands = [".EXIT", ".QUIT"]

sqlitewrapper = replwrap.REPLWrapper("sqlite3 -html -header", "sqlite> ", None)

class janssqlitekernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.10.0'
    language = 'sqlite3'
    language_version = '3.40.1'
    language_info = {
        'name': 'SQL',
        'mimetype': 'text/plain',
        'file_extension': '.sql',
    }
    banner = "SQLite 3\nConnected to a transient in-memory database.\n"\
             "Use .open FILENAME to reopen on a persistent database."

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            code = code.strip()
            code = code.replace("\n"," ")
            check_code = code.split(" ")
            if check_code[0].upper() not in special_commands:
                if code[-1] != ";":
                    code = code + ";"
            if code == "":
                solution = ""
            elif code[0] == "#":
                solution = ""
            elif check_code[0].upper() in exit_commands:
                solution = check_code[0] + " command is not allowed in SQLite3 Kernel."
            else:
                solution = sqlitewrapper.run_command(code)
                if solution.strip()[:4] == "<TR>":
                    solution = "<TABLE>" + solution + "</TABLE>"
                    stream_content = {'metadata': {}, 'data': {'text/html': solution}}
                    self.send_response(self.iopub_socket, 'display_data', stream_content)
                else:
                    if solution.strip() == "":
                        solution = "Query OK"
                    stream_content = {'name': 'stdout', 'text': solution}
                    self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
    
    def do_complete(self, code, cursor_pos):
        
        if " " in code:
            cursor_pos = code.rfind(" ") + 1
        else:
            cursor_pos = 0
        
        options = []
        for command in commands:
            if command.startswith(code.split(" ")[-1].upper()):
                options.append(command)

        return {
            'matches': options,
            'metadata': {},
            'status': 'ok',
            'cursor_start': cursor_pos,
            'cursor_end': len(code)
        }
