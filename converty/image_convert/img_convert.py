
from PIL import Image

class Img:
    def __init__(self, source, dest=None):
        self.source = source
        self.dest = dest
    
        
    def jpg_to_png(self):
        img = Image.open(self.source)
        if self.dest == None:
            img.save(f"{self.source.strip('.jpg')}.png")
        else:
            img.save(self.dest)
    
    def png_to_jpg(self):
        img = Image.open(self.source)
        if self.dest == None:
            img.save(f"{self.source.strip('.png')}.jpg")
        else:
            img.save(self.dest)