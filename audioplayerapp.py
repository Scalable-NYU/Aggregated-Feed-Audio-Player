from flask import Flask
import sys

print(sys.version)

app = Flask(__name__)

@app.route('/')
def base_func():
  return 'Testing flask app'

@app.route('/<username>')
def return_user_id():
  

if __name__ == '__main__':
  app.run()
