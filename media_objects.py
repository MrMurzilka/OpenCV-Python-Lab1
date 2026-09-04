class MediaObject:
    def __init__(self, filename, duration = 0):
        if filename == None:
            print()
        if duration < 0:
            print()
        self.filename = filename
        self.duration = duration

    def get_info(self):
        return f"{self.filename}: {self.duration} сек"
        
    def __str__(self):
        return f"<{self.__class__.__name__}({self.filename})>"
