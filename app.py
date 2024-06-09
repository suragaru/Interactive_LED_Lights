from flask import Flask, render_template, request
import serial, time

app = Flask(__name__)


setp='''
<html>
<head>
<title>Led Setup</title>
<style>
body{
    font-family:monospace;
}
</style>
</head>
<body>
<div align='center'>
    <h4>Axca Setup:</h4>
    <form action="/s" method="post">
    <label for="firstname">Com port:</label>
    <input  type="text" id="firstname" name="prt" style='width:30px;' >
    <br><br>
    <button type="submit">connect</button>
<div>
</body>
</html>
'''

setp='''
<html>
<head>
<title>Led Setup</title>
<style>
body{
    font-family:monospace;
}
</style>
</head>
<body>
<div align='center'>
    <h4>Axca Setup:</h4>
    <form action="/s" method="post">
    <label for="firstname">Com port:</label>
    <input  type="text" id="firstname" name="prt" style='width:30px;' >
    <br><br>
    <button type="submit">connect</button>
<div>
</body>
</html>
'''
connection_ok='''
<html>
<head>
<meta http-equiv="Refresh" content="0; URL=/">
</head>
<body>
</body>
</html>
'''


@app.route('/s', methods =["GET", "POST"])
def setup():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       com = request.form.get("prt")
       try:
           setup.ser = serial.Serial(f'COM{com}', 9600)
           print('com port connected..')
           return connection_ok


       except:
           print('com port connection attempt failed..')
    return setp


@app.route("/", methods=['GET', 'POST'])
def index():
     
    if request.method == 'POST':
        if request.form.get('led') == 'off':
            try:
                led_stat='The led is turn off..'
                x='e'
                i=x.strip()
                setup.ser.write(i.encode())
            except:
                print('error serial connection')
                
        elif  request.form.get('led_color0') == 'red':
            try:
                led_stat = 'The led is on and red-lit..'
                x='r'
                i=x.strip()
                setup.ser.write(i.encode())
            except:
                print('error serial connection')

        elif  request.form.get('led_color1') == 'green':
            try:
                led_stat = 'The led is on and green-lit..'
                x='g'
                i=x.strip()
                setup.ser.write(i.encode())
            except:
                print('error serial connection')

        elif  request.form.get('led_color2') == 'blue':
            try:
                led_stat = 'The led is on and blue-lit..'
                x='b'
                i=x.strip()
                setup.ser.write(i.encode())
            except:
                print('error serial connection')
                
        elif  request.form.get('led_color3') == 'white':
            try:
                led_stat = 'The led is on and white-lit..'
                x='w'
                i=x.strip()
                setup.ser.write(i.encode())
            except:
                print('error serial connection')

        elif  request.form.get('led_color4') == 'violet':
            try:
                led_stat = 'The led is on and violet-lit..'
                x='v'
                i=x.strip()
                setup.ser.write(i.encode())
            except:
                print('error serial connection')

        elif  request.form.get('led_color5') == 'yellow':
            try:
                led_stat = 'The led is on and yellow-lit..'
                x='y'
                i=x.strip()
                setup.ser.write(i.encode())
            except:
                print('error serial connection')
                
                
        else:
            print('error in get request')

    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html', led_stat=led_stat)

if __name__ == '__main__':
    app.run(port=80,debug=True)
