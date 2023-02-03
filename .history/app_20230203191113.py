import sqlite3
from flask import Flask, render_template, request, flash
from werkzeug.exceptions import abort
import pandas
import csv
import random

result = pandas.read_csv('temperature.csv')

print(result)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Q#qwe121dvj)sndh'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    with open('temperature.csv') as f:
      reader = csv.reader(f)
      chosen_row = random.choice(list(reader))
      print(chosen_row)
    return render_template('index.html', randomDate=chosen_row)

def save_user_guess(guessed_temp, actual_temp, dt):
  conn = get_db_connection()
  conn.execute('INSERT INTO user_guesses (guessed_temp, actual_temp, dt) VALUES (?, ?, ?)',
              (guessed_temp, actual_temp, dt))
  conn.commit()
  conn.close()

@app.route('/result', methods=('GET', 'POST'))
def compareTemperatures():  
  with open('temperature.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    foundRowInCsv = [row for row in reader if row['dt'] == request.form['date']]

    # print("foundRowInCsv", foundRowInCsv)

    foundRowInCsvAsArray = [foundRowInCsv[0]['dt'], foundRowInCsv[0]['dt_iso'], foundRowInCsv[0]['temp'] ]

    save_user_guess(request.form['guess-temperature'], foundRowInCsvAsArray[2], foundRowInCsv[0]['dt'])

    guessedTemp = float(request.form['guess-temperature'])
    actualTemp = float(foundRowInCsvAsArray[2])

    # print("guessedTemp", guessedTemp, "actualTemp:", actualTemp)

    if guessedTemp == actualTemp:
      flash('You guessed it correctly, Congratulations. You won!')
    elif guessedTemp < actualTemp:
      # print("Found that guessedTemp is LOWER than actualTemp")
      flash('You guessed lower value, increase value')
    else:
      # print("Found that guessedTemp is HGIHER than actualTemp")
      flash('You guessed higher value, decrease value')

  return render_template('index.html', randomDate=foundRowInCsvAsArray)
