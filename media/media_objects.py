import os

class MediaObject:
    """Base class for media objects, representing a generic media file with a filename and duration."""
    
    # Разрешенные расширения файлов для видео и изображений 
    # чтобы на ходу созздавать объекты Video или Image (если бы он был)
    VIDEO_EXTENSIONS = {'.mp4', '.avi', '.mov', '.mkv'}  
    IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp'}

    #Constructor
    def __init__(self, filename, duration = 0):
        # проверка на пустую строку и тип данных
        if not filename or not isinstance(filename, str): 
            raise ValueError("Имя файла не может быть пустым")
        
        # проверка на существование пути к файлу и самого файла
        if not os.path.exists(filename):                  
            raise FileNotFoundError(f"Файл {filename} не существует")
        
        # проверка на отрицательную продолжительность
        if duration < 0:                                  
            raise ValueError("Продолжительность не может быть отрицательной")

        self.filename = filename
        self.duration = duration

    #создание объекта MediaObject из файла, определяя его тип (видео или изображение) на основе расширения
    @classmethod
    def create_from_file(cls, filepath) -> 'MediaObject':
        # Проверка на существование файла
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Файл {filepath} не существует")

        # Выделение расщирения файла и приведение его к нижнему регистру
        _, ext = os.path.splitext(filepath)
        ext = ext.lower()

        if ext in cls.VIDEO_EXTENSIONS:
            # Ленивый импорт, во избежании циклических зависимостей
            from media.video import Video 
            return Video.create_from_file(filepath)
        
        if ext in cls.IMAGE_EXTENSIONS:
            # Если случай Image, то duration = 0 и создаем MediaObject (т.к. Image не реализован)
            return MediaObject(filepath, 0) 

        # В остальных случаях выбрасываем исключение о неподдерживаемом типе файла
        raise ValueError(f"Unsupported file type: {ext}")

    # Метод для получения информации о медиа объекте
    def get_info(self):
        return f"{self.filename}: {self.duration} seconds"

    # Метод для получения имени класса и имени файла
    def __str__(self):
        return f"<{self.__class__.__name__}({self.filename})>"

