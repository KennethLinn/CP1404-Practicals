import os


def main():

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Changing {} to {}".format(filename, new_name))
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


def get_fixed_filename(filename):
    new_name = ''
    for i, char in enumerate(filename):
        try:
            if filename[i].islower() and filename[i+1].isupper():
                new_name += char + '_'
            elif filename[i].isupper() and filename[i+1].isupper():
                new_name += char + '_'
            elif filename[i-1] == ' ':
                new_name += char.upper()
            else:
                new_name += char
        except IndexError:
            new_name += char
    return new_name.replace(" ", "_").replace(".T_X_T", ".txt")


main()