class Pycharm :
    def exec(self):
        print("compile")

class VSCode :
    def exec(self):
        print("running")

def code(editor):
    editor.exec()

code(Pycharm())
code(VSCode())