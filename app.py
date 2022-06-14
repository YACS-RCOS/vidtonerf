from flask import Flask

from dotenv import load_dotenv

load_dotenv('/./flaskenv')

app = Flask(_name_)

if _name_ == '_main_':
  app.run()
