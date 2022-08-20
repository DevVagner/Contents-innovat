from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import bcrypt
from datetime import datetime

app = Flask(__name__)
app.secret_key = "innovat"
client = pymongo.MongoClient("mongodb+srv://innovat:uVF5jfFAntxNOTtn@cluster0.poehq9h.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('innovat')
linksDb = db.links
activesDb = db.actives

@app.route("/", methods=['post', 'get'])
def index():
  return render_template('index.html')


@app.route("/links", methods=['post', 'get'])
def links():
  links = linksDb.find()
  if request.method == "POST":
    link_new = request.form.get('input')
    add = linksDb.insert_one({
      'link': link_new
    })
    return render_template("links.html", links=links)
  else:
    return render_template('links.html', links=links)


@app.route("/tolist", methods=['post', 'get'])
def tolist():
  actives = activesDb.find()
  if request.method == "POST":
    ativ_new = request.form.get('input')
    add_activ = activesDb.insert_one({
      'nome_active': ativ_new,
      'data': '00:00'
    })
    return render_template("tolist.html", ativ_list=actives)
  else:
    return render_template('tolist.html', ativ_list=actives)


@app.route("/deleteLink/<link>", methods=['post', 'get'])
def deleteLink(link):
  try:
    delete = linksDb.delete_one({
      'link': link
    })
    return redirect("/links")
  except:
    print('Erro')


@app.route("/deleteActive/<active>", methods=['post', 'get'])
def deleteActive(active):
  try:
    delete = activesDb.delete_one({
      'nome_active': active
    })
    return redirect("/tolist")
  except:
    print('Erro')


if __name__ == "__main__":
  app.run(debug=True)