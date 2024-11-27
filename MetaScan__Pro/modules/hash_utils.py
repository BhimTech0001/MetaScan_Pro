import hashlib

def compute_file_hashes(file_path):
    """Compute MD5, SHA-1, and SHA-256 hashes."""
    hashes = {"md5": hashlib.md5(), "sha1": hashlib.sha1(), "sha256": hashlib.sha256()}
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                for hash_func in hashes.values():
                    hash_func.update(chunk)
        return {name: func.hexdigest() for name, func in hashes.items()}
    except FileNotFoundError:
        return {"error": f"File '{file_path}' not found."}
