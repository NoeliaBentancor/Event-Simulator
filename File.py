import os


class File:
    def __init__(self, fileName):
        self.fileName=fileName
    
    async def write(self, content):
        fp = open(self.fileName, 'x')
        fp.write(content)
        fp.close()
    
    async def remove(self):
        os.remove(self.fileName)
        
