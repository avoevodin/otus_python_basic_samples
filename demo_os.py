import os

BASE_DIR = os.path.dirname(__file__)
IS_WINDOWS = 'nt' in os.name


def demo_paths():
    print('file:', __file__)
    print('base dir:',  BASE_DIR)
    print('os name:', os.name)
    print('is windows?', IS_WINDOWS)
    print('os path sep:', os.sep)

    folder_name = 'pictures'
    file_name = 'cat.jpg'
    print('test file path:',  os.path.join(BASE_DIR,  folder_name, file_name))


def demo_cwd():
    # current working directory
    cwd = os.getcwd()
    print('cwd:', cwd)


def main():
    demo_paths()
    demo_cwd()


if __name__ == '__main__':
    main()

