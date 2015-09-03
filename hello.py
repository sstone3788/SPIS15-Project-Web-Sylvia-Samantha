
from flask import Flask, url_for, render_template, request, redirect
from songlyrics import *



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
	global questionNum
	questionNum=0
	return render_template('games.html', mumnum=mumnum)



@app.route('/songs/<mumnum>')
def songs(mumnum):
	global questionNum
	questionLyrics=lyrics[questionNum][0]
	return render_template('songs.html', mumnum=mumnum, HQLyrics=questionLyrics)

@app.route('/songs/checkanswersong/<mumnum>', methods=['GET', 'POST'])
def checkAnswerSong(mumnum):
	global questionNum
	inputAnswer=request.form['song']
	if inputAnswer == lyrics[questionNum][1]:
		questionNum=questionNum+1
		if questionNum<len(lyrics):
			return render_template('correct.html', mumnum=mumnum, nextquestion=lyrics[questionNum][0])
		questionNum=0
		return render_template('finished.html', mumnum=mumnum)

	return render_template('incorrect.html', mumnum=mumnum, HQLyrics=lyrics[questionNum][0])






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

def ctof(ctemp):
	return (ctemp*(9.0/5.0))+32.0

@app.route('/ctofanswer/<mumnum>', methods=["POST"])
def ctofanswer(mumnum):
  ctemp = 0.0
  try:
        ctemp = float(request.form["ctempString"])
        ftemp = ctof(ctemp)
        message= "In Celcius: " + request.form["ctempString"] + " In Fahrenheit " + str(ftemp)
        return render_template('ctofanswer.html' , mumnum=mumnum, message=message)
  except ValueError:
	return render_template('ctofanswer.html' , mumnum=mumnum, message="Sorry, Yur Mum could not convert.")


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

@app.route('/mtok/<mumnum>')
def mtok(mumnum):
	return render_template('mtok.html', mumnum=mumnum)

def mtok(miles):
    return (miles*1.609344)

@app.route('/mtokanswer/<mumnum>', methods=["POST"])
def convertMtoK(mumnum):
    miles= 0.0
    try:
        miles =float(request.form["milesString"])
        kilometers = mtok(miles)
	message= "In Miles: " + request.form["milesString"] + " In Kilometers " + str(kilometers) 
	return render_template('mtokanswers.html' , mumnum=mumnum, message=message)
    except ValueError:
	return render_template('mtokanswers.html' , mumnum=mumnum, message="Yur Mum says Or nahh, could not convert.")

@app.route('/ktom/<mumnum>')
def ktom(mumnum):
	return render_template('ktom.html', mumnum=mumnum)

def ktom(kilometers):
    return (kilometers/1.609344)

@app.route('/ktomanswer/<mumnum>', methods=["POST"])
def convertKtoM(mumnum):
    kilometers= 0.0
    try:
        kilometers =float(request.form["kilometerString"])
        miles = ktom(kilometers)
	message= "In Kilometers: " + request.form["kilometerString"] + " In Miles " + str(miles) 
	return render_template('ktomanswer.html' , mumnum=mumnum, message=message)
    except ValueError:
	return render_template('ktomanswer.html' , mumnum=mumnum, message="Yur Mum says Or nahh, could not convert.")


@app.route('/ptok/<mumnum>')
def ptok(mumnum):
	return  render_template('ptok.html', mumnum=mumnum)

def ptok (pounds):
    return (pounds*.45359237)

@app.route('/ptokanswer/<mumnum>',methods=["POST"]) 
def convertptok (mumnum):
    pounds= 0.0
    try:
        pounds = float(request.form["poundString"])
        kilograms = ptok(pounds)
	message= "In Pounds: " + request.form["poundString"] + " In Kilograms " + str(kilograms) 
	return render_template('ptokanswer.html' , mumnum=mumnum, message=message)
    except ValueError:
	return render_template('ptokanswer.html' , mumnum=mumnum, message="Yur Mum says *click* or naw ain't finna convert ")

@app.route('/ktop/<mumnum>')
def ktop(mumnum):
	return  render_template('ktop.html', mumnum=mumnum)

def ktop (kilograms):
    return (kilograms/.45359237)

@app.route('/ktopanswer/<mumnum>',methods=["POST"]) 
def convertktop (mumnum):
    kilograms= 0.0
    try:
        kilograms = float(request.form["kilogramString"])
        pounds = ktop(kilograms)
	message= "In Kilograms: " + request.form["kilogramString"] + " In Pounds " + str(pounds) 
	return render_template('ktopanswer.html' , mumnum=mumnum, message=message)
    except ValueError:
	return render_template('ktopanswer.html' , mumnum=mumnum, message="Yur Mum says *click* or naw ain't finna convert ")

@app.route('/ftom/<mumnum>')
def ftom(mumnum):
	return  render_template('ftom.html', mumnum=mumnum)

def ftom (feet):
    return (feet*0.3048)

@app.route('/ftomanswer/<mumnum>',methods=["POST"]) 
def convertftom (mumnum):
    feet= 0.0
    try:
        feet = float(request.form["feetString"])
        meters = ftom(feet)
	message= "In Feet: " + request.form["feetString"] + " In Meters " + str(meters) 
	return render_template('ftomanswer.html' , mumnum=mumnum, message=message)
    except ValueError:
	return render_template('ftomanswer.html' , mumnum=mumnum, message="Yur Mum says *click* or naw ain't finna convert ")

@app.route('/randommum')
def randommum():
	mumnum= randrange(1, 11)
	return redirect("/main/"+str(randommum))


@app.route('/mtof/<mumnum>')
def mtof(mumnum):
	return  render_template('mtof.html', mumnum=mumnum)

def mtof (meters):
    return (meters/0.3048)

@app.route('/mtofanswer/<mumnum>',methods=["POST"]) 
def convertmtof (mumnum):
    meters= 0.0
    try:
        meters = float(request.form["meterString"])
        feet = mtof(meters)
	message= "In Meters: " + request.form["meterString"] + " In Feet " + str(feet) 
	return render_template('mtofanswer.html' , mumnum=mumnum, message=message)
    except ValueError:
	return render_template('mtofanswer.html' , mumnum=mumnum, message="Yur Mum says *click* or naw ain't finna convert ")








    




if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=54321)





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



def askmum(answer):
    return (answer)

@app.route('/askmum>/<q>')
def momanswers (q):
    return "Yassss" 




##+ (a+b)

####add(a, b)
###

    

