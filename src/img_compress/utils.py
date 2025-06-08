import os
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import List

ALLOWED_EXTENSIONS = (".jpg", ".png", ".jpeg")

log_dir = Path.home() / ".img-compress" / "logs"
log_dir.mkdir(parents=True, exist_ok=True)

log_file = log_dir / "img-compress.log"


handler = TimedRotatingFileHandler(
    filename=str(log_file),
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8",
    utc=True
)

formatter = logging.Formatter(
    "%(asctime)s — %(levelname)s — %(message)s"
)
handler.setFormatter(formatter)

logger = logging.getLogger("img-compress")
logger.setLevel(logging.WARNING)
logger.addHandler(handler)
logger.propagate = False


def construct_new_file_name(old_name: str) -> str:
    name, ext = os.path.splitext(old_name)
    return f"{name}_optimized{ext}"


def is_allowed_extension(file_path: str) -> bool:
    _, ext = os.path.splitext(file_path)
    if ext.lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


def get_images_paths_from_dir(dir_name: str) -> List[str]:
    paths = [os.path.join(dir_name, item) for item in os.listdir(dir_name)]
    return [item for item in paths if os.path.isfile(item) and is_allowed_extension(item)]
