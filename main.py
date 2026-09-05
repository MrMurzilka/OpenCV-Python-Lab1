from media.media_library import MediaLibrary
from media.video import Video
from media.media_objects import MediaObject
from Lab1.filter.blur_filter import BlurFilter

if __name__ == "__main__":
    media_lib = MediaLibrary()

    media_filepaths = [
        "Lab1/source/test_video1.mp4",
        "Lab1/source/test_video2.mp4",
        "Lab1/source/test_video3.mp4",
        "Lab1/source/test_video4.mp4",
        "Lab1/source/test_image.jpg",
    ]

    for path in media_filepaths:
        try:
            media_obj = MediaObject.create_from_file(path)
            media_lib.add(media_obj)
        except Exception as e:
            print(f"Ошибка загрузки {path}: {e}")


    print(media_lib.get_total_duration())

    if media_lib.media_objects:
        filter_obj = BlurFilter(2)
        for media_obj in media_lib.media_objects:
            filter_obj.apply(media_obj)
    