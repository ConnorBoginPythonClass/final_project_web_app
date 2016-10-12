from flask import Flask, render_template, request
import giphypop
import os
g = giphypop.Giphy()
app = Flask(__name__)

def get_gif(responses):
    # g = giphypop.giphy()
    responses = g.search('cats') # returns a list of objects
    for response in responses:
    	print(response.media_url)
    	print(response.url)

# http://media0.giphy.com/media/26uf9IAZN7JvvYbwA/giphy.gif # Media (image) Url
# http://giphy.com/gifs/love-cat-cats-26uf9IAZN7JvvYbwA # GIF Url
# http://media1.giphy.com/media/26uf5hiFbD0DdZdGo/giphy.gif
# http://giphy.com/gifs/cat-judgemental-judgey-26uf5hiFbD0DdZdGo

@app.route('/')
def index():
    name = request.values.get('name', 'Nobody')
    greeting = "Hello {}".format(name)
    return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    gif = request.values.get('term')
    responses = get_gif(gif)
    return render_template('results.html', responses=responses)

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)