import os
import sys
import shutil
import subprocess
import urllib.request
import tarfile


def log_error(message):
    print(f"ERROR: {message}")


def check_and_install_exiftool():
    """Check if ExifTool is installed. Install it on Linux if missing."""
    try:
        if shutil.which("exiftool"):
            return  # ExifTool is already installed
        if sys.platform.startswith("linux"):
            install_exiftool_on_linux_silent()
        else:
            print("Automatic installation is supported only on Linux.")
            print("Please install ExifTool manually from https://exiftool.org/")
    except Exception as e:
        log_error(f"Error checking/installing ExifTool: {e}")


def check_dependencies():
    """Check for required dependencies (perl, make)."""
    for tool in ["perl", "make"]:
        if not shutil.which(tool):
            raise EnvironmentError(f"{tool} is required but not installed. Please install it first.")


def install_exiftool_on_linux_silent():
    """Install ExifTool on Linux silently."""
    try:
        check_dependencies()
        exiftool_url = "https://exiftool.org/Image-ExifTool-12.64.tar.gz"
        tar_file = "Image-ExifTool.tar.gz"

        # Download and extract
        urllib.request.urlretrieve(exiftool_url, tar_file)
        with tarfile.open(tar_file, "r:gz") as tar:
            tar.extractall()

        extracted_dir = tar.getnames()[0]
        original_dir = os.getcwd()

        try:
            os.chdir(extracted_dir)
            # Install silently
            subprocess.run(["perl", "Makefile.PL"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["make"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["make", "install"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        finally:
            os.chdir(original_dir)

        # Clean up
        os.remove(tar_file)
        shutil.rmtree(extracted_dir)
    except Exception as e:
        log_error(f"Error installing ExifTool on Linux: {e}")
