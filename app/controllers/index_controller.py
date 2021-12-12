"""imports"""
from app.controllers.controller import ControllerBase
from flask import render_template


"""index controller class"""
class IndexController(ControllerBase):
    @staticmethod
    def get():
        return render_template('index.html')


