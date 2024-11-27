#!/usr/bin/env python3

from modules.exif import extract_exif_data
from modules.file_scan import scan_file
from modules.hash_utils import compute_file_hashes
from modules.installer import check_and_install_exiftool
from utils.logger import log_error

import shutil

def banner():
    """Display tool banner with dynamic width based on terminal size."""
    # Get the current terminal width
    terminal_width = shutil.get_terminal_size().columns
    
    # Ensure a minimum width for the banner
    banner_width = max(terminal_width, 50)  # Use at least 50 as the minimum width

    print("=" * banner_width)
    print("MetaScan_Pro".center(banner_width))
    print("Created by: Bhim Saini".center(banner_width))
    print("=" * banner_width)

def main():
    """Main entry point."""
    banner()
    copyright_notice()  # Display copyright notice
    check_and_install_exiftool()
    while True:  # Keep running indefinitely
        print("\nOptions:")
        print("1. Extract EXIF metadata")
        print("2. Scan for file signatures")
        print("3. Compute file hashes (MD5, SHA-1, SHA-256)")
        print("4. Display EXIF, file signatures, and file hashes")
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
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting MetaScan_Pro. Thank you for using the tool!")
            break  # Exit gracefully when Ctrl+C is pressed
        except Exception as e:
            log_error(f"Unexpected error: {e}")
            print(f"An error occurred: {e}. Returning to the main menu...")

if __name__ == "__main__":
    main()
