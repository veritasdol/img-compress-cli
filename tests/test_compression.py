import os
import tempfile
from pathlib import Path
from PIL import Image
from img_compress.main import process_file, compress_image
from img_compress.utils import construct_new_file_name


def create_test_image(path: str):
    """Create a simple red JPEG image for testing."""
    image = Image.new("RGB", (100, 100), color="red")
    image.save(path, "JPEG")


def test_compress_image_success():
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.jpg")
        output_path = os.path.join(tmpdir, "output.jpg")

        create_test_image(input_path)
        result = compress_image(input_path, output_path, quality=75)

        assert result is True
        assert os.path.exists(output_path)
        assert os.path.getsize(output_path) > 0


def test_compress_image_file_not_found():
    with tempfile.TemporaryDirectory() as tmpdir:
        missing_path = os.path.join(tmpdir, "missing.jpg")
        output_path = os.path.join(tmpdir, "output.jpg")

        result = compress_image(missing_path, output_path, 80)
        assert result is False


def test_process_file_creates_compressed_image():
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "original.jpg")
        create_test_image(input_path)

        # Act
        process_file(input_path, target_path=tmpdir, quality=70)

        # Assert
        optimized_name = construct_new_file_name("original.jpg")
        output_path = os.path.join(tmpdir, optimized_name)
        assert os.path.exists(output_path)
        assert os.path.getsize(output_path) > 0