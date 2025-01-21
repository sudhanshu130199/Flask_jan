from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Sudhanshu!</p>"

@app.route("/ping", methods=['GET'])
def ping():
    return "<p>Hey man! why are pinging me</p>"

@app.route("/aboutus", methods=['GET'])
def aboutus():
    return "<p>We are Mlops learners</p>"

model_pickle = open("classifier.pkl", "rb")
# In the terminal we should be at that path where .pkl file is present then we can pass classifier.pkl as above otherwise we've to give full path
# In terminal we can use "cd path" to go to specific path
clf = pickle.load(model_pickle)

# defining the endpoint which will make the prediction
@app.route("/prediction", methods=['POST'])
def prediction():
    """ Returns loan application status using ML model
    """
    loan_req = request.get_json()
    print(loan_req)
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status": pred}


# flask --app Flask_jan/app.py run
# to run flask application on terminal