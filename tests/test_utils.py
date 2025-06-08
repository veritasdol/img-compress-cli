import os
import tempfile
from img_compress.utils import construct_new_file_name, is_allowed_extension, get_images_paths_from_dir


def test_construct_new_file_name():
    assert construct_new_file_name("photo.jpg") == "photo_optimized.jpg"
    assert construct_new_file_name("archive.tar.gz") == "archive.tar_optimized.gz"

def test_is_allowed_extension():
    assert is_allowed_extension("image.jpg")
    assert is_allowed_extension("photo.PNG")
    assert is_allowed_extension("photo.pdf.jpeg")
    assert not is_allowed_extension("photo.PNG.pdf")
    assert not is_allowed_extension("document.pdf")

def test_get_images_paths_from_dir(tmp_path):
    # Create temp files
    (tmp_path / "img1.jpg").write_text("dummy")
    (tmp_path / "img2.png").write_text("dummy")
    (tmp_path / "file.txt").write_text("not image")

    result = get_images_paths_from_dir(str(tmp_path))
    assert len(result) == 2
    assert any("img1.jpg" in path for path in result)
    assert all(path.endswith(('.jpg', '.png')) for path in result)