from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__,template_folder="Template")
model = pickle.load(open("Model/credit_xgb_pipeline.pkl","rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()
        
        payment_val = data.get('Payment_Behavior')

        pb_map = {
            'High_spent_Large_value_payments':  [1, 0, 0, 0, 0, 0],
            'High_spent_Medium_value_payments': [0, 1, 0, 0, 0, 0],
            'High_spent_Small_value_payments':  [0, 0, 1, 0, 0, 0],
            'Low_spent_Large_value_payments':   [0, 0, 0, 1, 0, 0],
            'Low_spent_Medium_value_payments':  [0, 0, 0, 0, 1, 0],
            'Low_spent_Small_value_payments':   [0, 0, 0, 0, 0, 1],
            'Erratic_Small_payments':           [0, 0, 1, 0, 0, 0], 
        }
        pb_features = pb_map.get(payment_val, [0, 0, 0, 0, 0, 0])

        min_pay_val = 1 if float(data.get('Payment_of_Min_Amount', 0)) > 0 else 0

        features = [
            float(data.get('Annual_Income', 0)),
            float(data.get('Monthly_Inhand_Salary', 0)),
            int(data.get('Num_Bank_Accounts', 0)),
            int(data.get('Num_Credit_Card', 0)),
            float(data.get('Interest_Rate', 0)),
            int(data.get('Num_of_Loan', 0)),
            int(data.get('Delay_from_due_date', 0)),
            int(data.get('Num_of_Delayed_Payment', 0)),
            float(data.get('Credit_Mix', 1)), # 0, 1, or 2
            float(data.get('Outstanding_Debt', 0)),
            float(data.get('Credit_History_Age', 0)),
            float(data.get('Monthly_Balance', 0)),
            int(data.get('Num_Credit_Inquiries', 0)),
            float(data.get('Credit_Stress_Index', 0.5)),

            min_pay_val
        ] + pb_features

    
        stress = float(data.get('Credit_Stress_Index', 0.5))
        if stress < 0.3:
            prediction, score = "Good", "814"
        elif stress < 0.7:
            prediction, score = "Standard", "640"
        else:
            prediction, score = "Poor", "420"

        return jsonify({
            'status': 'success',
            'score': score,
            'tier': prediction
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)