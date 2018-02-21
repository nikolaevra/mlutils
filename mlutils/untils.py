def format_file_names(rel_path='', name_style="img_{}"):
    """
      Rename all files in the folder under rel_path.
      Keyword arguments:
      rel_path -- relative path to the folder (default 0.0)
      name_style -- file naming convention with incrementing integer (default "img_{}")
    """
    import os
    from os import listdir
    from os.path import isfile, join

    dir_path = os.path.abspath(os.getcwd())
    full_path = os.path.join(dir_path, rel_path)

    onlyfiles = [f for f in listdir(full_path) if isfile(join(full_path, f))]
    i = 1

    for file in onlyfiles:
        infile = os.path.join(full_path, file)
        outfile = name_style.format(i) + ".jpg"

        if infile != outfile:
            os.rename(infile, os.path.join(full_path, outfile))
            i = i + 1
        else:
            print('Could not rename matching names {} and {}'.format(infile, outfile))


def get_methods(obj):
    """
      Get all methods of a class
    """
    import inspect

    return inspect.getmembers(obj, predicate=inspect.ismethod)
