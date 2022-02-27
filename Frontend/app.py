from flask import Flask, render_template, url_for,request

app = Flask(__name__)
@app.route('/')
@app.route('/index/')
def index():
    description = """
    """
    return render_template('index.html',
                            user_name='',
                            user_image=url_for('static', filename='img/profile.png'),
                            description=description,
                            blur=True)

@app.route('/result/',methods = ['POST'])
def result():
    result = request.form
    sentences = result['sentences']
    #value = jsonTransform(model.predict(sentences)) ### JSON 
    #toxicity_text = toxicity + severe_toxicity + obscene + threat + insult + idd_attack

    return render_template('result.html',
                            user_name=sentences,
                            user_image=url_for('static', filename='tmp/happy.jpg'),
                            description='Hi my friend')
