from flask import Flask, render_template

# create a new flask app
app = Flask(__name__)

# show index.html at site.com/
@app.route('/')
def index():
  return render_template('index.html')

# show portfolio.html at site.com/portfolio/
@app.route('/portfolio/')
def portfolio():
  return render_template('portfolio.html')

# run the app locally
if __name__ == '__main__':
  app.run(host='127.0.0.1', debug=True)
