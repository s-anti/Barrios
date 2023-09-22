import subprocess
import os


servidorWeb = subprocess.Popen(
    ["python", "-m", "http.server", "8080"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    cwd=os.getcwd(),
)

servidorBackend = subprocess.Popen(
    ["python", "app.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    cwd=os.getcwd(),
)

servidorWeb.wait()
servidorBackend.wait()
