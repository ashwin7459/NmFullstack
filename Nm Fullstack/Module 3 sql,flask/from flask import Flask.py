from flask import Flask

app=Flask(_name_)


@app.route('/') 
def index():
    return ("this is the ashwin application")

@app.route('/about')
def about():
    return ("this is the about page of ashwin")


if _name_ =='_main_':
    app.run(debug = True,port=5000)
