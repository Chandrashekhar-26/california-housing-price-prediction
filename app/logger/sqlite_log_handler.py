import logging
import sqlite3
from datetime import datetime
import os
from config import Config


class SQLiteLogHandler(logging.Handler):

    def __init__(self, log_dir='logs'):
        super().__init__()
        os.makedirs(log_dir, exist_ok=True)
        self.db_path = f'{log_dir}/log.db'
        self.conn = sqlite3.connect(self.db_path)
        self._create_logs_table()

    def _create_logs_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                level TEXT,
                message TEXT,
                module TEXT,
                function TEXT
            )
        ''')
        self.conn.commit()

    def emit(self, record):
        try:
            cursor = self.conn.cursor()
            timestamp = datetime.utcnow().isoformat()
            cursor.execute('''
                INSERT INTO logs (timestamp, level, message, module, function)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                timestamp,
                record.levelname,
                record.getMessage(),
                record.module,
                record.funcName
            ))
            self.conn.commit()
        except Exception:
            self.handleError(record)

    def close(self):
        self.conn.close()
        super().close()


sqlite_log_handler = SQLiteLogHandler(Config.LOG_DIR)
