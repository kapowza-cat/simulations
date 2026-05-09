import subprocess
import os

def create_exe(script_name, icon_path=None):
    if not os.path.exists(script_name):
        print(f"Error: {script_name} not found.")
        return

    # --onefile: Bundle everything into a single .exe
    # --noconsole: Hide the terminal window when the exe runs
    command = ["python", "-m", "PyInstaller", "--noconsole", "--onefile", "--clean", script_name]

    if icon_path and os.path.exists(icon_path):
        command.extend(["--icon", icon_path])

    try:
        print(f"Starting build for {script_name}...")
        subprocess.run(command, check=True)
        print("\nBuild successful!")
        print("Your executable is located in the 'dist' folder.")
    except subprocess.CalledProcessError as e:
        print(f"\nAn error occurred during the build: {e}")

create_exe("crash.py")