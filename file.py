from abc import ABC, abstractmethod


class FileHandler(ABC):
    """Abstract base class defining the contract all file handlers must follow."""

    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def read(self):
        """Return the contents of the file."""
        pass

    @abstractmethod
    def write(self, data):
        """Write data to the file."""
        pass

    
    def describe(self):
        return f"{type(self).__name__} handling '{self.filepath}'"


class TextFileHandler(FileHandler):
    """Concrete handler for plain-text files."""

    def read(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return f.read()

    def write(self, data):
        with open(self.filepath, "w", encoding="utf-8") as f:
            f.write(data)


class BinaryFileHandler(FileHandler):
    """Concrete handler for binary files (e.g. images, executables)."""

    def read(self):
        with open(self.filepath, "rb") as f:
            return f.read()          # returns bytes

    def write(self, data):
        if not isinstance(data, (bytes, bytearray)):
            raise TypeError("BinaryFileHandler.write() requires bytes input")
        with open(self.filepath, "wb") as f:
            f.write(data)


# Example
if __name__ == "__main__":
    # Text handler
    text = TextFileHandler("example.txt")
    text.write("Hello from the text handler!")
    print(text.read())                      
    print(text.describe())                   

    # Binary handler
    binary = BinaryFileHandler("example.bin")
    binary.write(b"\x00\x01\x02\x03")
    print(binary.read())                     
    print(binary.describe())               