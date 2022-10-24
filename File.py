import os


class File:
    def __init__(self, file_name):
        self.file_name = file_name

    async def write(self, content):
        """Writes current file."""
        file = open(self.file_name, "x")
        file.write(content)
        file.close()

    async def remove(self):
        """Removes the file from the current file system."""
        os.remove(self.file_name)
