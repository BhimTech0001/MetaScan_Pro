#!/usr/bin/env python3

from modules.exif import extract_exif_data
from modules.file_scan import scan_file
from modules.hash_utils import compute_file_hashes
from modules.installer import check_and_install_exiftool
from utils.logger import log_error

def banner():
    """Display tool banner."""
    print("=" * 50)
    print("MetaScan_Pro".center(50))
    print("Created by: Bhim Saini".center(50))
    print("=" * 50)

def main():
    """Main entry point."""
    banner()
    check_and_install_exiftool()
    print("Options:")
    print("1. Extract EXIF metadata")
    print("2. Scan for file signatures")
    print("3. Compute file hashes (MD5, SHA-1, SHA-256)")
    print("4. Display EXIF, file signatures, and file hashes")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            file_path = input("Enter the image file path: ")
            exif_data = extract_exif_data(file_path)
            print("\n--- EXIF Metadata ---\n", exif_data)
        elif choice == 2:
            file_path = input("Enter the file path to scan: ")
            results = scan_file(file_path)
            print("\n--- Found File Signatures ---")
            for offset, desc in results:
                print(f"Offset: {offset}, Type: {desc}")
        elif choice == 3:
            file_path = input("Enter the file path to compute hashes: ")
            hashes = compute_file_hashes(file_path)
            print("\n--- File Hashes ---")
            for algo, value in hashes.items():
                print(f"{algo.upper()} Hash: {value}")
        elif choice == 4:
            file_path = input("Enter the file path: ")
            print("\n--- EXIF Metadata ---")
            print(extract_exif_data(file_path))
            print("\n--- File Signatures ---")
            for offset, desc in scan_file(file_path):
                print(f"Offset: {offset}, Type: {desc}")
            print("\n--- File Hashes ---")
            for algo, value in compute_file_hashes(file_path).items():
                print(f"{algo.upper()} Hash: {value}")
        elif choice == 5:
            print("Exiting. Thank you!")
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        log_error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
