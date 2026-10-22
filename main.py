from media.media_library import MediaLibrary
from media.video import Video
from media.media_objects import MediaObject
from filter.blur_filter import BlurFilter

if __name__ == "__main__":
    media_lib = MediaLibrary()

    media_filepaths = [
        "source/test_video1.mp4",
        "source/test_video2.mp4",
        "source/test_video3.mp4",
        "source/test_video4.mp4",
        "source/test_image.jpg",
    ]

    #MediaLibrary class test
    for path in media_filepaths:
        try:
            media_obj = MediaObject.create_from_file(path)
            media_lib.add(media_obj)
        except Exception as e:
            print(f"Ошибка загрузки {path}: {e}")

    print(media_lib.filter_by_type(Video))
    print(media_lib.get_total_duration())

    #BlurFilter class test
    if media_lib.media_objects:
        filter_obj = BlurFilter(2)
        for media_obj in media_lib.media_objects:
            filter_obj.apply(media_obj)

    #MediaObject class test
    media_object = media_lib.media_objects[0]
    print(media_object.get_info())
    print(media_object)  # Вывод имени класса и имени файла

    #Video class test
    video_object = media_lib.media_objects[1]
    if isinstance(video_object, Video):
        print(f"Video: {video_object.get_info()}")
        print(f"FPS: {video_object.get_fps()}")
        print(f"Codec: {video_object.get_codec()}")
    