import docutils.parsers.rst

txt = '''
+--------------------------------+-------------------------------+
|Lorem ipsum lorem ipsum         |Second Column                  |
|Lorem ipsum lorem ipsum Lorem   |                               | 
+--------------------------------+-------------------------------+
|Lorem ipsum lorem ipsum         |Lorem ipsum lorem ipsum Lorem  | 
|Lorem ipsum lore                |Lorem ipsum lorem ipsum        | 
|                                |Lorem i                        |
|                                |                               |
+--------------------------------+-------------------------------+
|Lorem ipsum lorem ipsum         |Lorem ipsum lorem ipsum Lorem  | 
|Lorem ipsum lore                |                               | 
|                                |Lorem i                        |
|                                |                               |
+--------------------------------+-------------------------------+
'''

def rst2tree(txt):
    parser = docutils.parsers.rst.Parser()
    document = docutils.utils.new_document("test")
    document.settings.tab_width = 4
    document.settings.pep_references = 1
    document.settings.rfc_references = 1
    parser.parse(txt, document)
    return document

doc = rst2tree(txt)
print(doc)