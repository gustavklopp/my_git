import os

''' modify because html is incorrect... (br not closed)'''
def replace_file(file, old_text, new_text):
    head, filename = os.path.split(file)
    file_copy = head + "/file_copy.html"
    with open(file, 'r', encoding='windows-1252') as f:
        with open(file_copy, 'w', encoding='windows-1252') as f2:
            s = f.read().replace(old_text, new_text)
            f2.write(s)
    os.remove(file)
    os.rename(file_copy, file)


def correct_br(file):
    replace_file(file, "<br clear=ALL>", "<br clear=\"all\"/>")
    replace_file(file, "<br clear=all>", "<br clear=\"all\"/>")