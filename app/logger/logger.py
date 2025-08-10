import logging
import os
from .sqlite_log_handler import sqlite_log_handler
from config import Config
import sqlite3


class Logger:

    def __init__(self, log_dir='logs'):
        os.makedirs(log_dir, exist_ok=True)
        self.log_dir = log_dir

        # Create file handler
        file_handler = logging.FileHandler(f"./{log_dir}/log.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        ))

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # add sqlite log handler and file handler if not already exists
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(sqlite_log_handler)


    def log_info(self, log_msg):
        self.logger.info(log_msg)

    def log_error(self, log_msg):
        self.logger.error(log_msg)

    def log_debug(self, log_msg):
        self.logger.debug(log_msg)

    def log(self, level, log_msg):
        self.logger.log(level, log_msg)

    def fetch_logs(self):
        conn = None
        query = "SELECT id, timestamp, level, message, module, function FROM logs ORDER BY timestamp DESC"
        result = []

        try:
            conn = sqlite3.connect(f"./{self.log_dir}/log.db")
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            result = rows
        except sqlite3.Error as e:
            error = f"Error fetching logs: {e}"
            print(error)
            return error

        finally:
            if conn is not None:
                conn.close()

        return result


logger = Logger(Config.LOG_DIR)
