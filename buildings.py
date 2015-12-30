import sys


# rope docs: https://github.com/python-rope/rope/blob/master/docs/library.rst#making-a-project








def remove_screen(building_name):
    s = """

class %(Classname)s(NewsArticle):
    class Meta:
        verbose_name = 'News Article'
        verbose_name_plural = 'Sortable News Articles'
        ordering = ['the_order']


    """ % {'Classname':building_name}
    with open("NewsBlog/models2.py", "r+") as myfile:
        contents = myfile.read()
        print(s)
        print(contents)
        print(contents.find(s))
        if contents.find(s) != -1:
            contents2 = contents.replace(s,"")
            myfile.seek(0)
            myfile.truncate()
            myfile.write(contents2)
            print("Now Type")
            print("python3 manage.py syncdb")
        else:
            print("Building Not Found")

def add_screen(building_name):
    s = """

class %(Classname)s(NewsArticle):
    class Meta:
        verbose_name = 'News Article'
        verbose_name_plural = 'Sortable News Articles'
        ordering = ['the_order']


    """ % {'Classname':building_name}
    with open("NewsBlog/models2.py", "a") as myfile:
        file = myfile.read()
        if file.find(s) != -1:
            myfile.write(s)
            print("Now Type")
            print("python3 manage.py syncdb")
        else:
            print("building exists")
    



if sys.argv[1] == 'add':
    for screen in sys.argv[2:]:
        add_screen(screen)

if sys.argv[1] == 'remove':
    for screen in sys.argv[2:]:
        remove_screen(screen)

if sys.argv == False:
    print('parameters are add and remove')
