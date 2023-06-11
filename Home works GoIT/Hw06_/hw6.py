import shutil
import sys
import uuid
from normalize import normalize
from pathlib import Path

CATEGORIES = {"Pictures": ['.JPEG', '.PNG', '.JPG', '.SVG'],
              "Video": ['.AVI', '.MP4', '.MOV', '.MKV'],
              "Documents": ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX', '.RTF'],
              "Audio": ['.MP3', '.OGG', '.WAV', '.AMR'],
              "Archives": ['.ZIP', '.GZ', '.TAR'],
              "Torrent": ['.TORRENT']}


def unpack_archives(file: Path, root_dir: Path, category: str) -> None:
    path_to_unpack = root_dir.joinpath(f"{category}\\{normalize(file.stem)}")
    shutil.unpack_archive(file, path_to_unpack)
    file.unlink()


def move_file(file: Path, root_dir: Path, category: str) -> None:
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    new_name = target_dir.joinpath(f"{normalize(file.stem)}{file.suffix}")
    if new_name.exists():
        new_name = new_name.with_name(
            f"{new_name.stem}-{uuid.uuid4()}{file.suffix}")
    file.rename(new_name)


def get_categories(file: Path) -> str:
    ext = file.suffix.upper()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


def sort_folder(path: Path) -> None:
    for item in path.glob("**/*"):
        if item.is_file():
            cat = get_categories(item)
            if cat == "Archives":
                unpack_archives(item, path, cat)
            else:
                move_file(item, path, cat)


def delete_folders(path: Path) -> None:
    for item in path.iterdir():
        if item.is_dir():
            delete_folders(item)
        try:
            item.rmdir()
        except:
            continue


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"

    if not path.exists():
        return f'Folder path {path} do not exists.'

    sort_folder(path)

    delete_folders(path)

    return "All OK"


if __name__ == "__main__":
    print(main())
