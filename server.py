from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return "helloworld"


@app.route('/about')
def about():
    return render_template("About.html")
@app.route('/blog')
def blog():
    return "blog page"
@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return "this is the number " + blog_id
if __name__=="__main__":
    app.run(debug=True)
