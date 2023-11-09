from flask import Flask, render_template, request


app = Flask(__name__)

#Make a homepage
@app.route('/')

def homepage():
    return render_template('homepage.html')

@app.route('/hello/<name>')

def hello(name):
    listOfNames = [name, "Seb", "Salmon"]
    return render_template('name.html', Sname=name, nameList=listOfNames)


@app.route('/rank/<movies>')

def rank(movies):
    rankOfMovies = [movies, "Wizard of Oz", "Kink Kong", "Fast and Furious", "The conjuring"]
    return render_template('movies.html', Srank=movies, movieList=rankOfMovies)


@app.route('/form', methods=['GET', 'POST'])

def formDemo(name = None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)



#Add option to run this file directly
if __name__ == "__main__":
    app.run(debug= True)