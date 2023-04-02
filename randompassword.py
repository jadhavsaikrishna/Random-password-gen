from flask import Flask,render_template,request

from random import choice,shuffle

letter_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
             "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

number_list=["0","1","2","3","4","5","6","7","8","9"]

symbols_list=["!","#","$","%","&","(",")","*","+"]

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/password",methods=["GET","POST"])
def password():
    if request.method=="POST":
        letters=int(request.form["letter"])
        numbers=int(request.form["number"])
        symbols=int(request.form["sym"])



        password=[]
        for char in range(0,letters):
            password.append(choice(letter_list))
        for num in range(0,numbers):
            password.append(choice(number_list))
        for sym in range(0,symbols):
            password.append(choice(symbols_list))
        shuffle(password)
        randompassword=""
        for char in password:
            randompassword+=char

        return render_template("password.html",RANDOMPASSWORD=randompassword)

if __name__=="__main__":
    app.run()
