import os
import shutil


def main():
    extensions = []

    os.chdir('FilesToSort')
    files = os.listdir('.')

    for file in files:
        extension = file.split('.')[-1]
        if extension not in extensions:
            os.mkdir(extension)
            extensions.append(extension)
        shutil.move(file, extension)


if __name__ == '__main__':
    main()