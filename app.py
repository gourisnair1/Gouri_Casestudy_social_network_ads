from flask import Flask,render_template, request
import pickle
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        print(gender)
        age = request.form['age']
        print(age)
        salary = request.form['salary']
        print(salary)
        # female = request.form['female']
        # print(female)
        # male = request.form['male']
        # print(male)
        model = pickle.load(open('ad_model.pkl','rb'))
        purchased = model.predict([[float(gender),float(age),float(salary)]])
        print(purchased[0])

    return render_template('prediction.html', purchased = (purchased[0]))

if __name__ =='__main__':
    app.run()