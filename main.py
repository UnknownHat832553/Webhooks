import subprocess
import os
from server import server_on

if __name__ == "__main__":
    bot_files = ['news.py'] # ชื่อไฟล์ (เพิ่มได้) ['ไฟล์ที่1.py', 'ไฟล์ที่2.py']

    processes = []
    for bot_file in bot_files:
        process = subprocess.Popen(['python', bot_file])
        processes.append(process)

    for process in processes:
        process.wait()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
server_on()