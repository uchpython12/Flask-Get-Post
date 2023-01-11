# 1.寫出一個flask 框架  顯示hello world

# 寫出一個get name flask  訪問網址

# 2.
# 訪問 : http://127.0.0.1:5000/data/appInfo/FlaskSE
# 打印 : type(name) : <class 'str'>
# 網頁 : String => FlaskSE


# 3.
# 訪問 : http://127.0.0.1:5000/data/appInfo/id/5
# 打印 : type(id) : <class 'int'>
# 網頁 : int => 5

# 4.
# 訪問 : http://127.0.0.1:5000/data/appInfo/version/1.01
# 打印 : type(version) : <class 'float'>
# 網頁 : float => 1.01

# 網頁模版 - Html 回傳
# 5.網頁顯示 : H1 大標題的 Hello World 元素

# 6.建立 templates 資料夾
# home.html title:My Website Text
# table 三行三列 內容Text

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello world'

@app.route('/data/appInfo/<name>' , methods=['GET'])
def queryDataMessageByName(name):
    print("type(name)=",type(name))
    return name
@app.route('/data/appInfo/id/<int:id>' , methods=['GET'])
def queryDataMessageById(id):
    print("type(id)=",type(id))
    return format(id)
@app.route('/data/appInfo/version/<float:version>' , methods=['GET'])
def queryDataMessageByVersion(version):
    print("type(version)=",type(version))
    return format(version)

@app.route('/text' , methods=['GET'])
def text():
    return "<html><body><h1>Hello World</h1></body></html>"

@app.route('/home' , methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/page/text')
def pageText():
    return render_template('page.html', text="Python Flask !")

@app.route('/page/app')
def pageAppInfo():
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)

@app.route('/page/data')
def pageData():
    data = {  # dict
        '01': 'Text Text Text',
        '02': 'Text Text Text',
        '03': 'Text Text Text',
        '04': 'Text Text Text',
        '05': 'Text Text Text'
    }
    return render_template('page.html', data=data)
@app.route('/static')
def staticPage():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(debug=True)