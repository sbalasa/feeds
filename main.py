import feedparser
from flask import Flask

app = Flask('app')

feeds1 = "https://9gag-rss.com/api/rss/get?code=9GAGNSFWNoGif&format=1"
feeds2 = "https://9gag-rss.com/api/rss/get?code=9GAGAwesomeNoGif&format=1"
feeds3 = "https://9gag-rss.com/api/rss/get?code=9GAGComic&format=1"
feeds4 = "https://9gag-rss.com/api/rss/get?code=9GAGComicNoGif&format=1"

@app.route('/')
def hello_world():
    text = """
    <html>
    Hi, am Santhosh Balasa, <br />
    To view the feeds response, just click the following: <br />
    <a href="https://RSSfeedrender--sbalasa.repl.co/feeds1">feeds1</a>
    <br />
    <a href="https://RSSfeedrender--sbalasa.repl.co/feeds2">feeds2</a>
    <br />
    <a href="https://RSSfeedrender--sbalasa.repl.co/feeds3">feeds3</a>
    <br />
    <a href="https://RSSfeedrender--sbalasa.repl.co/feeds4">feeds4</a>
    <br />
    </html>"""
    return text


@app.route('/feeds1/')
def feeds1():
    feed = feedparser.parse(feeds1)
    title = feed["feed"]["title"]
    return """
    <html>
      <body>
        <h1> {0} </h1>
          <p>{1}</p> <br/>
      </body>
    </html>
    """.format(title, feed)

@app.route('/feeds2/')
def feeds2():
    feed = feedparser.parse(feeds2)
    title = feed["feed"]["title"]
    return """
    <html>
      <body>
        <h1> {0} </h1>
          <p>{1}</p> <br/>
      </body>
    </html>
    """.format(title, feed)

@app.route('/feeds3/')
def feed3():
    feed = feedparser.parse(feeds3)
    title = feed["feed"]["title"]
    return """
    <html>
      <body>
        <h1> {0} </h1>
          <p>{1}</p> <br/>
      </body>
    </html>
    """.format(title, feed)

@app.route('/feeds4/')
def feeds4():
    feed = feedparser.parse(feeds4)
    title = feed["feed"]["title"]
    return """
    <html>
      <body>
        <h1> {0} </h1>
          <p>{1}</p> <br/>
      </body>
    </html>
    """.format(title, feed)

app.run(host='0.0.0.0', port=8080)
