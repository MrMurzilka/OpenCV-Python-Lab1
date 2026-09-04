class MediaLibrary:
    def __init__(self):
        self.media_objects = []

    def add(self, media_obj):
        self.media_objects.append(media_obj)

    def get_total_duration(self):
        return sum(obj.duration for obj in self.media_objects)

    def filter_by_type(self, media_type: str):
        return [obj for obj in self.media_objects if isinstance(obj, media_type)]