from flask import Flask, render_template

class Views:
    def home(self):
        return render_template("index.html")
    
    def menu(self):
        return render_template("menu.html")