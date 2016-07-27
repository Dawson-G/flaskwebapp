import os
from flask import Flask, request, render_template

app = Flask(__name__)


#  @app.route('/')
#  def index():
#      return "Method used: %s" %(request.method)
#      #return "This is the homepage."
#      
#  @app.route('/about')
#  def about():
#      return '<h2>About</h2>'
#      
#      ba
#  @app.route('/post/<int:post_id>')
#  def post(post_id):
#      return "<h2>Post id: %s" %(post_id)
#  
#  @app.route('/bacon', methods=['GET', 'POST'])
#  def bacon():
#      if request.method == 'POST':
#          return 'You posted!'
#      else:
#          return 'You got me!'
#  
#  @app.route("/profile/<name>")
#  def profile(name):
#      return render_template("profile.html", name=name)
#  
#  @app.route('/')
#  @app.route('/<user>')
#  def index(user=None):
#      return render_template("user.html", user=user)
#
#  @app.route('/shopping')
#  def shopping():
#      food = ["Orange Juice", "food!"]
#      return render_template("shopping.html", food=food)

@app.route('/')
def index():
    return "Homepage"

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
    
