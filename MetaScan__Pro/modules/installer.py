import os
import shutil
import subprocess
import urllib.request
import tarfile
from MetaScan__Pro import utils

def check_and_install_exiftool():
    """Check if ExifTool is installed. Install it on Linux if missing."""
    try:
        if shutil.which("exiftool"):
            return  # ExifTool is already installed
        if sys.platform.startswith("linux"):
            install_exiftool_on_linux_silent()
        else:
            raise NotImplementedError("Automatic Tool installation is supported only on Linux.")
    except Exception as e:
        log_error(f"Error checking/installing Tool: {e}")


def install_exiftool_on_linux_silent():
    """Install Tool on Linux silently."""
    try:
        exiftool_url = "https://exiftool.org/Image-ExifTool-12.64.tar.gz"
        tar_file = "Image-ExifTool.tar.gz"
        urllib.request.urlretrieve(exiftool_url, tar_file)
        with tarfile.open(tar_file, "r:gz") as tar:
            tar.extractall()
        extracted_dir = tar.getnames()[0]
        os.chdir(extracted_dir)
        subprocess.run(["perl", "Makefile.PL"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["make"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["make", "install"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.chdir("..")
    except Exception as e:
        log_error(f"Error installing MetaScan_Pro on Linux: {e}")
