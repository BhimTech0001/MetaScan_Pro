MAGIC_SIGNATURES = [
    (b'\x89PNG\r\n\x1a\n', 'PNG Image'),
    (b'\xff\xd8\xff', 'JPEG Image'),
    (b'GIF87a', 'GIF Image'),
    (b'GIF89a', 'GIF Image'),
    (b'PK\x03\x04', 'ZIP Archive'),
    (b'7z\xBC\xAF\x27\x1C', '7z Archive'),
    (b'Rar!\x1A\x07\x00', 'RAR Archive'),
    (b'\x1f\x8b\x08', 'GZIP Archive'),
    (b'\x42\x5A\x68', 'BZIP2 Archive'),
    (b'ELF', 'ELF Executable'),
    (b'%PDF-', 'PDF Document'),
    (b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1', 'Microsoft Office Document'),
    (b'\x50\x4B\x03\x04', 'Office Open XML (e.g., DOCX, XLSX)'),
    (b'\xFF\xFE\x3C\x00', 'XML Document'),
    (b'{\\rtf1', 'RTF Document'),
    (b'ID3', 'MP3 Audio'),
    (b'\x00\x00\x00\x18ftypmp4', 'MP4 Video'),
    (b'\x00\x00\x01\xBA', 'MPEG Video'),
    (b'OggS', 'OGG Audio'),
    (b'RIFF', 'WAV Audio'),
    (b'\x0A\x50', 'Copyright String'),
    # Add more signatures as needed
]

def scan_file(file_path):
    """Scan for known file signatures."""
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            results = [(data.find(sig), desc) for sig, desc in MAGIC_SIGNATURES if sig in data]
        return results
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
