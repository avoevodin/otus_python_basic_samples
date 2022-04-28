from pathlib import Path


def demo_cwd():
     cwd = Path.cwd()
     print('cwd:', cwd)
     print('cwd repr', repr(cwd))


def demo_home():
    print('home', Path.home())


def demo_check_existence():
    users = Path('/Users')
    print(users)
    print('Users exists?', users.exists())

    foo = Path('/Foo')
    print(foo)
    print('Foo  exists?', foo.exists())

    foo.unlink(missing_ok=True)


def demo_file_path():
    current_file = Path(__file__)
    print(current_file)
    print(repr(current_file))
    base_dir: Path = current_file.parent
    print(repr(base_dir))
    print(base_dir.parent)
    print('base dir parents:')
    print(list(base_dir.parents))


def demo_build_path():
    current_file = Path(__file__)
    base_dir: Path = current_file.parent

    folder_name = 'pictures'
    file_name = 'cats.jpg'

    cats_pic = base_dir / 'pictures' / 'cats.jpg'
    print(cats_pic)

    cats_pic2 = base_dir.joinpath(folder_name, file_name)
    print(cats_pic2)
    print(cats_pic2 == cats_pic)
    print('suffix', cats_pic.suffix)
    print('suffixes', cats_pic.suffixes)
    print('name', cats_pic.name)
    print('stem', cats_pic.stem)
    print('anchor', cats_pic.anchor)


def demo_files():
    current_file = Path(__file__)
    base_dir: Path = current_file.parent
    filename = 'file.txt'

    file = Path(filename)
    print(file)
    print(file.resolve())
    file.unlink(missing_ok=True)
    file.write_text('Hello\n')
    print(file.read_text())


def demo_folders():
    current_file = Path(__file__)
    base_dir: Path = current_file.parent
    some_folder = base_dir.joinpath('some', 'folder')
    print(some_folder)
    some_folder.mkdir(parents=True, exist_ok=True)
    some_folder.chmod(0o644)
    print(0o644)
    print(0x1A)
    print(0b1111)


def main():
    demo_cwd()
    demo_home()
    demo_check_existence()
    demo_file_path()
    demo_build_path()
    demo_files()
    demo_folders()


if __name__ == '__main__':
    main()
