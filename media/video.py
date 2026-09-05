from media.media_objects import MediaObject
import cv2

class Video(MediaObject):
    """Video class representing a video file with metadata, inheriting from MediaObject."""
    def __init__(self, filename, duration, resolution, codec, fps=0):
        super().__init__(filename, duration)
        self.resolution = resolution
        self.codec = codec
        self.fps = fps

    # Метод для создания объекта Video из файла, извлекая информацию о видео с помощью OpenCV
    @classmethod
    def create_from_file(cls, filepath):
        # Используем OpenCV для открытия видеофайла
        cap = cv2.VideoCapture(filepath)

        # Проверка на успешное открытие видеофайла
        if not cap.isOpened():
            raise ValueError(f"Error opening video file: {filepath}") 

        # Блок try-finally для гарантированного освобождения ресурсов OpenCV
        try:

            # Получаем информацию о видеофайле
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            fps = cap.get(cv2.CAP_PROP_FPS)
            fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

            # Т.к. fourcc - int, побитово сдвигаем и извлекаем младщий байт, чтобы преобразовать его в char и собрать строку кодека
            codec = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)]) 
            resolution = f"{width}x{height}"
            # Вычисляем продолжительность видео в секундах, если fps > 0, иначе устанавливаем duration = 0
            duration = frame_count/fps if fps > 0 else 0 
            return cls(filepath, duration, resolution, codec, fps)

        # Освобождение ресурсов OpenCV
        finally:
            cap.release() 

    # Метод для получения кадров в секунду (fps) видео
    def get_fps(self):
        return self.fps

    # Метод для получения кодека видео
    def get_codec(self):
        return self.codec