from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)
events = []

@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/add', methods=['POST'])
def add_event():
    title = request.form['title']
    date = request.form['date']
    desc = request.form['desc']

    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        events.append({'title': title, 'date': date, 'desc': desc})
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    
