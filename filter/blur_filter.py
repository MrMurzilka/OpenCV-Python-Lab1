from filter.image_filter import ImageFilter
import cv2
from media.media_objects import MediaObject

class BlurFilter(ImageFilter):
    """BlurFilter class to apply blur effect to media objects."""
    def __init__(self, factor=1):
        self.factor = factor

    def apply(self, media_data: MediaObject):
        # Выделяем имя файла без расширения для будущего сохранения результата
        name = media_data.filename.split("/")[-1].split(".")[0]
        # Проверяем, является ли объект видео или изображением на основе продолжительности 
        # (не лучший вариант, но работает) 
        # возможно переделаю)
        if media_data.duration != 0:
            # Открытие видеофайла с помощью OpenCV
            cap = cv2.VideoCapture(filename = media_data.filename)

            # Проверка на успешное открытие видеофайла
            if not cap.isOpened():
                print(f"Error opening video file: {media_data.filename}")
            else:
                print(f"Successfully opened video file: {media_data.filename}")

            # Настройка параметров для записи нового видеофайла с размытием
            # Так как не всегда, можно сохранить файл в том же формате, что и исходный, то я решил использовать mp4v для всех видеофайлов
            fourcc = cv2.VideoWriter.fourcc(*"mp4v")
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            # Создание объекта VideoWriter для записи нового видеофайла с размытием
            out = cv2.VideoWriter(f"Lab1/source/{name}_Gaussian_blurred.mp4", fourcc, fps, (width, height))

            # Блок try-finally для гарантированного освобождения ресурсов OpenCV
            # Покадровое чтение видео, применение размытия и запись в новый файл
            try:
                # Бесконечный цикл, пока не закончится видеофайл
                while True:
                    # Чтение кадра из вилеофайла в переменную frame, ret - флаг успешного чтения
                    ret, frame = cap.read()

                    # Если видеофайл закончился или произошла ошибка при чтении кадра, выходим из цикла
                    if not ret:
                        break

                    # Применение размытия к кадру с использованием гауссового фильтра
                    # Гауссово размытие было выбрано как основное, так как обечпечивает баланс между
                    # сохранением деталей и естсвтвенностью изображения и производительностью, по сравнению с другими методами размытия
                    # (например, двустороннее размытие (cv2.bilateralFilter) или размытие по среднему (cv2.blur)
                    blurred_frame = cv2.GaussianBlur(frame, (0,0), self.factor)
                    # Запись размытого кадра в новый видеофайл и отображение его в окне
                    out.write(blurred_frame)
                    cv2.imshow("Blurred Video", blurred_frame)

                    # Проверка нажатия клавиши 'q' для выхода из цикла
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            # Гарантированное освобождение ресурсов OpenCV и закрытие всех орон после завершения обработки видео
            finally:
                cap.release()
                out.release()
                cv2.destroyAllWindows()
                
        # Если объект является изображением (duration = 0), то применяем размытие к изображению
        else:
            frame = cv2.imread(media_data.filename)

            if frame is None:
                print(f"Error opening image file: {media_data.filename}")
            else:
                cv2.imwrite(f"Lab1/source/Gaussian_blurred_{name}.jpg", cv2.GaussianBlur(frame, (0,0), self.factor))

