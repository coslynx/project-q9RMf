import discord
from datetime import datetime

class LoggingSystem:
    def __init__(self):
        self.log_file = "moderation_log.txt"

    def log_action(self, action, user, reason):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {action} by {user}: {reason}\n"
        
        with open(self.log_file, "a") as file:
            file.write(log_entry)

    def get_logs(self):
        try:
            with open(self.log_file, "r") as file:
                logs = file.readlines()
            return logs
        except FileNotFoundError:
            return []

    def clear_logs(self):
        with open(self.log_file, "w") as file:
            file.write("")