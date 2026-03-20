import glob
import subprocess

files = glob.glob("*.pbm")

for file in files:
    print(f"Copying {file}")
    subprocess.run(["ampy", "-p", "COM5", "put", file, file])
