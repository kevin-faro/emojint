import os
import urlparse

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

from emojimap import EmojiMap
emojiMap = EmojiMap()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/slackbot', methods = ['GET'])
def slackbot():
  return render_template('slackbot.html')

@app.route('/slackbot', methods = ['POST'])
def bot():
  #todo log form
  app.logger.info(request)
  print(request.form)

  msg = request.form['text']

  response = ''

  if not msg or msg.lower() == ':beginner:':
    response = __help()
  elif msg.lower().startswith(':post_office:'):
    response = __feedback()
  else:
    response = __emojify(msg)

  return jsonify({ 'response_type': response[0], 'text': response[1], 'channel': request.form['channel_name'], 'user': request.form['user_name'] })

def __help():
  return ('ephemeral', ':beginner:\t-\tshow this help\n\:post_office:\t-\tsend feedback\n...\t-\temoji awesomeness!')

def __feedback():
  return ('ephemeral', 'Thanks for the feedback!')

def __emojify(text):
  return ('in_channel', emojiMap.apply(text))

if __name__ == '__main__':
  db.create_all()
  port = int(os.environ.get('PORT',5000))
  app.run(host='0.0.0.0', port=port)
