import functions
import os


def test_info_about_creator():
    assert isinstance(functions.info_about_creator(), str)


def test_print_files():
    assert functions.print_files() == [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]


def test_print_dirs():
    onlydirs = functions.print_dirs()
    onlyfiles = functions.print_files()
    assert list(set(onlydirs).intersection(onlyfiles)) == []


def test_save_fails_and_dirs():
    onlyfiles = functions.print_files()
    onlydirs = functions.print_dirs()
    functions.save_fails_and_dirs()
    files_and_dirs = []
    with open("listdir.txt", 'r') as f:
        for line in f:
            for word in line.split():
                files_and_dirs.append(word)
    assert set(files_and_dirs).intersection(onlyfiles) == set(onlyfiles)
    assert set(files_and_dirs).intersection(onlydirs) == set(onlydirs)



def test_change_dir():
    old_onlydirs = functions.print_dirs()
    functions.change_dir("C:/Users/Ольга")
    new_onlydirs = functions.print_dirs()
    assert old_onlydirs != new_onlydirs
