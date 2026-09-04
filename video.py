from media_objects import MediaObject

class Video(MediaObject):
    def __init__(self, filename, duration, resolution, codec, fps=0):
        super().__init__(filename, duration)
        self.resolution = resolution
        self.codec = codec
        self.fps = fps

    def get_fps(self):
        return self.fps

    def get_codec(self):
        return self.codec