from flask import Flask
app = Flask(__name__)

@app.route("/")
def mum():
    return "Hello World! :) This is Sylvia and Samantha from your mum"

def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)

@app.route('/ftoc/<ftempString>')
def convertFtoC(ftempString):
    ftemp = 0.0
    try:
        ftemp = float(ftempString)
        ctemp = ftoc(ftemp)
        return "In Farenheit: " + ftempString + " In Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftempString + " to a number"

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


if __name__=="__main__":
    app.run(port=5100)

##+ (a+b)

####add(a, b)
###

    
