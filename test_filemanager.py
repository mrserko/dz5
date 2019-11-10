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


def test_change_dir():
    old_onlydirs = functions.print_dirs()
    functions.change_dir("C:/Users/Ольга")
    new_onlydirs = functions.print_dirs()
    assert old_onlydirs != new_onlydirs
