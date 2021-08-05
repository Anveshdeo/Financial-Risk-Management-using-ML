
from flask import Flask, render_template, request
app = Flask(__name__)
import joblib
trans=joblib.load('Scalar.save')
model = joblib.load('model.save')

@app.route('/')
def helloworld():
    return render_template("base.html")
@app.route('/assesment')
def prediction():
    return render_template("index.html")

@app.route('/risk', methods = ['POST'])
def admin():
    p=request.form["age"]
    q= request.form["gender"]
    if (q == 'f'):
        q1,q2=1,0
    if (q == 'm'):
        q1,q2=0,1
    r= request.form["housing"]
    if (r == 'own'):
        r1,r2,r3=0,1,0
    if (r == 'free'):
        r1,r2,r3=1,0,0
    if (r == 'rent'):
        r1,r2,r3=0,0,1
    s= request.form["job"]
    if (s == 'un'):
        s=0
    if (s == 'ur'):
        s=1
    if (s == 'sk'):
        s=2
    if (s == 'hs'):
        s=3
    t= request.form["saving"]
    if (t == 'l'):
        t1,t2,t3,t4=1,0,0,0
    if (t == 'm'):
        t1,t2,t3,t4=0,1,0,0
    if (t == 'qr'):
        t1,t2,t3,t4=0,0,1,0   
    if (t == 'r'):
        t1,t2,t3,t4=0,0,0,1
    u= request.form["checking"]
    if (u == 'lt'):
        u1,u2,u3=1,0,0
    if (u == 'mo'):
        u1,u2,u3=0,1,0
    if (u == 'ri'):
        u1,u2,u3=0,0,1
    v= request.form["credit"]
    w= request.form["duration"]    
    x= request.form["purpose"]
    if (x == 'bu'):
        x1,x2,x3,x4,x5,x6,x7,x8=1,0,0,0,0,0,0,0
    if (x == 'car'):
        x1,x2,x3,x4,x5,x6,x7,x8=0,1,0,0,0,0,0,0
    if (x == 'da'):
        x1,x2,x3,x4,x5,x6,x7,x8=0,0,1,0,0,0,0,0
    if (x == 'edu'):
        x1,x2,x3,x4,x5,x6,x7,x8=0,0,0,1,0,0,0,0
    if (x == 'fe'):
        x1,x2,x3,x4,x5,x6,x7,x8=0,0,0,0,1,0,0,0
    if (x == 'rtv'):
        x1,x2,x3,x4,x5,x6,x7,x8=0,0,0,0,0,1,0,0
    if (x == 'rep'):
        x1,x2,x3,x4,x5,x6,x7,x8=0,0,0,0,0,0,1,0
    if (x == 'vo'):
        x1,x2,x3,x4,x5,x6,x7,x8=0,0,0,0,0,0,0,1
    y=[[int(x1),int(x2),int(x3),int(x4),int(x5),int(x6),int(x7),int(x8),int(r1),int(r2),int(r3),int(t1),int(t2),int(t3),int(t4),int(u1),int(u2),int(u3),int(q1),int(q2),int(p),int(s),int(v),int(w)]]        
    y=trans.transform(y)
    a = model.predict(y)
    if (a[0] == 0):
        b ="Bad"
        return render_template("predbad.html", z = b)

    else:
        
        b ="Good"
        return render_template("predgood.html", z = b)


if __name__ == '__main__':
    app.run(debug = True)