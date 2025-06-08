import os
import click
from .utils import construct_new_file_name, logger, get_images_paths_from_dir, is_allowed_extension
from PIL import Image, UnidentifiedImageError




def compress_image(img_path: str, target_path: str, quality: int) -> bool:
    try:
        image = Image.open(img_path)
    except FileNotFoundError as error:
        logger.error(f"File not found: {img_path} — {error}")
        return False
    except UnidentifiedImageError as error:
        logger.error(f"Unidentified image format: {img_path} — {error}")
        return False

    try:
        logger.info(f"Saving compressed image")
        image.save(target_path, quality=quality, optimize=True)
        logger.info(f"Optimized image was saved to: {target_path}")
        return True
    except Exception as error:
        logger.error(f"Failed to save image: {target_path} — {error}")
        return False


def process_file(file_path: str, target_path: str, quality: int) -> None:
    file_name = os.path.basename(file_path)
    output_dir = target_path or os.path.dirname(file_path)
    os.makedirs(output_dir, exist_ok=True)

    new_file_name = construct_new_file_name(file_name)
    output_path = os.path.join(output_dir, new_file_name)

    if compress_image(file_path, output_path, quality):
        click.echo(f"✅ Compressed: {file_path} → {output_path}")
    else:
        click.echo(f"❌ Failed to compress: {file_path}")


@click.command(name="img-compress")
@click.option(
    "--file-path", 
    "-f", 
    type=click.Path(exists=True, resolve_path=True, dir_okay=False), 
    help="Path to the image file.")
@click.option(
    "--dir-name", 
    "-d", 
    type=click.Path(exists=True, resolve_path=True, file_okay=False), 
    help="Path to the directory with images. All images with jpg/png extentions will be optimized.")
@click.option(
    "--target-path", 
    "-t", 
    type=click.Path(resolve_path=True, file_okay=False), 
    help="Directory where the compressed image will be saved.")
@click.option(
    "--quality", 
    "-q", 
    type=click.IntRange(1, 100, clamp=True), 
    default=90, 
    help="Compression quality (0-100).")
def main(file_path: str, dir_name: str, target_path: str, quality: int) -> None:
    if not file_path and not dir_name:
        raise click.UsageError(
            "You must provide either --file-path or --dir-name.")
    if file_path and dir_name:
        raise click.UsageError(
            "You must provide only one of --file-path or --dir-name, not both.")

    if dir_name:
        images = get_images_paths_from_dir(dir_name)
        for path in images:
            process_file(path, target_path, quality)
        return
    if is_allowed_extension(file_path):
        process_file(file_path, target_path, quality)
    else:
        logger.error(f"Unsupported extension: {file_path}")

    

