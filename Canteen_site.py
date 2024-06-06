from flask import Flask 
from Views import Views

class App:
    def __init__(self,import_path):
        self.app = Flask(import_path)
        self.view()
    
    def view(self):
        page = Views()
        self.app.add_url_rule("/",view_func=page.home)
        self.app.add_url_rule("/index.html",view_func=page.home)
        self.app.add_url_rule("/menu.html",view_func=page.menu)
    
    def run(self,**kwargs):
        self.app.run(**kwargs)


Canteen = App(__name__)

Canteen.run(debug=True)