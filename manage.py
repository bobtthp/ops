from app import app
from flask_script import Manager
from flask import Flask, render_template, request, redirect
import json
import Tools
manage = Manager(app)

@app.route('/')
def hello():
    return 'hello 8000'
@app.route('/test',methods=['post','get'])
def test():
    if request.method == 'POST':
	d = {}
        data = request.get_data()
	l = data.split('&')
        for i in l:
		L = i.split('=')
                d[L[0]] = L[1]
	print d
	status = Tools.json_to_yml(d)
        return render_template('docker.html') 
    else:
        return render_template('docker.html')

if __name__ == '__main__':
    manage.run()
