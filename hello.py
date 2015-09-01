
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/welcome/<mumnum>')
def welcome(mumnum):
	return render_template('welcome.html', mumnum=mumnum)

@app.route('/main/<mumnum>')
def main(mumnum):
	return render_template('main.html', mumnum=mumnum)

@app.route('/tools/<mumnum>')
def tools(mumnum):
	return render_template('tools.html', mumnum=mumnum)

@app.route('/ftoc/<mumnum>')
def ftoc(mumnum):
	print "I am in /ftoc/<mumnum>"
	return render_template('ftoc.html', mumnum=mumnum)

@app.route('/ctof/<mumnum>')
def ctof(mumnum):
	return render_template('ctof.html', mumnum=mumnum)

@app.route('/games/<mumnum>')
def games(mumnum):
	return render_template('games.html', mumnum=mumnum)

@app.route('/songs/<mumnum>')
def songs(mumnum):
	return render_template('songs.html', mumnum=mumnum)

@app.route('/movies/<mumnum>')
def movies(mumnum):
	return render_template('movies.html', mumnum=mumnum)

@app.route('/quotes/<mumnum>')
def quotes(mumnum):
	return render_template('quotes.html', mumnum=mumnum)

@app.route('/correct/<mumnum>')
def correct(mumnum):
	return render_template('correct.html', mumnum=mumnum)

@app.route('/incorrect/<mumnum>')
def incorrect(mumnum):
	return render_template('incorrect.html', mumnum=mumnum)


def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)


@app.route('/ftocanswer/<mumnum>', methods=["POST"])
def ftocanswer(mumnum):
    print "I am in /ftocanswer/<mumnum>"
    ftemp = 0.0
    try:
        ftemp = float(request.form["ftempString"])
        ctemp = ftoc(ftemp)
        message= "In Farenheit: " + request.form["ftempString"] + " In Celsius " + str(ctemp) 
	return render_template('ftocanswer.html' , mumnum=mumnum, message=message)
    except ValueError:
        
	return render_template('ftocanswer.html' , mumnum=mumnum, message="Sorry, Yur Mum could not convert.")





   







    




if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=54321)





@app.route("/mum")
def mum():
    return "Hello World! :) This is Sylvia and Samantha from your mum!"





@app.route('/urmum')
def urmum():
    return "It's ur mum"

def add(a,b):
    return (a+b)        

@app.route('/addnumbers/<aString>+<bString>')
def addnumbers(a, b):
##    (a,b) = 0.0
    try:
        a = float(aString)
        b = float(bString)
        return (aString + bString)
##        a= float(a)
##        b = float(b)
##        print "test"
##        return "a+b="+ (a + b)
    except ValueError:
        return "Sorry.  Could not add " + (a,b) + str
    
##        (a,b) = float(a)
####        (a,b) = add(b)


def mtok(miles):
    return (miles*1.609344)

@app.route('/mtok/<milesString>')
def convertMtoK(milesString):
    miles= 0.0
    try:
        miles =float(milesString)
        kilometers = mtok(miles)
        return " In Miles : " + milesString + " In Kilometers : " + str(kilometers)
    except ValueError:
        return " ur mum says naaah shorty " + milesString + " ain't gon convert to kilometers ya woe"

    

def ptok (pounds):
    return (pounds*.45359237)

@app.route('/ptok/<poundsString>') 
def convertptok (poundsString):
    pounds= 0.0
    try:
        pounds = float(poundsString)
        kilograms = ptok(pounds)
        return "In pounds : " + poundsString + " In Kilograms : " + str (kilograms)
    except ValueError:
        return " ur mum says *click* or naw ain't finna convert " + poundsString

def askmum(answer):
    return (answer)

@app.route('/askmum>/<q>')
def momanswers (q):
    return "Yassss" 




##+ (a+b)

####add(a, b)
###

    

