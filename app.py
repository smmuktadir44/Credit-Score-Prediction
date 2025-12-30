
import pandas as pd
import streamlit as st

def user_input():

    # ---------- Numeric Inputs ----------
    Monthly_Inhand_Salary = st.sidebar.number_input('Monthly Inhand Salary', 0, 1_000_000, 10, 150)
    Num_Bank_Accounts = st.sidebar.number_input('Numbers of Bank Account', 0, 20, 1, 2)
    Num_Credit_Card = st.sidebar.number_input('Numbers of Credit Card', 0, 20, 1, 2)
    Interest_Rate = st.sidebar.number_input('Interest Rate', 0, 50, 1, 0)
    Delay_from_due_date = st.sidebar.number_input('Delay From Due Date', 0, 50, 1, 0)
    Num_of_Delayed_Payment = st.sidebar.number_input('Number of Delay Payment', 0, 50, 1, 0)
    Num_Credit_Inquiries = st.sidebar.number_input('Number of Credit Enquiries', 0, 50, 1, 0)
    Credit_Utilization_Ratio = st.sidebar.number_input('Credit Utilization Ratio', 0, 100, 1, 0)
    Total_EMI_per_month = st.sidebar.number_input('Total EMI per Month', 0, 1_000_000, 10)
    Monthly_Balance = st.sidebar.number_input('Monthly Balance', 0, 1_000_000, 10)
    Annual_Income = st.sidebar.number_input('Annual Income', 0, 1_000_000, 10, 1000)
    Num_of_Loan = st.sidebar.number_input('Numbers of Loan', 0, 20, 1, 2)
    Changed_Credit_Limit = st.sidebar.number_input('Changed Credit Limit', 0, 100, 1, 0)
    Outstanding_Debt = st.sidebar.number_input('Outstanding Debt', 0, 10_000, 10, 0)
    Credit_History_Age = st.sidebar.number_input('Credit History Age (Months)', 0, 1000, 1, 10)

    # ---------- Categorical Inputs ----------
    Credit_Mix = st.sidebar.selectbox('Credit Mix', ['Good', 'Standard', 'Bad'])
    Payment_of_Min_Amount = st.sidebar.selectbox('Payment of Minimum Amount', ['Yes', 'No'])

    Type_of_Loan = st.sidebar.multiselect(
        'Types of Loan',
        [
            'Auto Loan', 'Credit-Builder Loan', 'Debt Consolidation Loan',
            'Home Equity Loan', 'Mortgage Loan', 'Not Specified',
            'Payday Loan', 'Personal Loan', 'Student Loan'
        ]
    )

    Payment_Behaviour = st.sidebar.selectbox(
        'Payment Behaviour',
        [
            'Pay_Behav_High_spent_Large_value_payments',
            'Pay_Behav_High_spent_Medium_value_payments',
            'Pay_Behav_High_spent_Small_value_payments',
            'Pay_Behav_Low_spent_Large_value_payments',
            'Pay_Behav_Low_spent_Medium_value_payments',
            'Pay_Behav_Low_spent_Small_value_payments'
        ]
    )

    # ---------- Base Feature Dictionary ----------
    user_data = {
        'Monthly_Inhand_Salary': Monthly_Inhand_Salary,
        'Num_Bank_Accounts': Num_Bank_Accounts,
        'Num_Credit_Card': Num_Credit_Card,
        'Interest_Rate': Interest_Rate,
        'Delay_from_due_date': Delay_from_due_date,
        'Num_of_Delayed_Payment': Num_of_Delayed_Payment,
        'Num_Credit_Inquiries': Num_Credit_Inquiries,
        'Credit_Utilization_Ratio': Credit_Utilization_Ratio,
        'Total_EMI_per_month': Total_EMI_per_month,
        'Monthly_Balance': Monthly_Balance,
        'Annual_Income': Annual_Income,
        'Num_of_Loan': Num_of_Loan,
        'Changed_Credit_Limit': Changed_Credit_Limit,
        'Outstanding_Debt': Outstanding_Debt,
        'Credit_History_Age': Credit_History_Age,
        f'Credit_Mix_{Credit_Mix}': 1,
        f'Payment_of_Min_Amount_{Payment_of_Min_Amount}': 1
    }

    # ---------- One-Hot Encode Loan Types ----------
    loan_types = [
        'Auto Loan', 'Credit-Builder Loan', 'Debt Consolidation Loan',
        'Home Equity Loan', 'Mortgage Loan', 'Not Specified',
        'Payday Loan', 'Personal Loan', 'Student Loan'
    ]

    user_data.update({
        f'Type_of_Loan_{loan}': int(loan in Type_of_Loan)
        for loan in loan_types
    })

    # ---------- One-Hot Encode Payment Behaviour ----------
    payment_behaviours = [
        'Pay_Behav_High_spent_Large_value_payments',
        'Pay_Behav_High_spent_Medium_value_payments',
        'Pay_Behav_High_spent_Small_value_payments',
        'Pay_Behav_Low_spent_Large_value_payments',
        'Pay_Behav_Low_spent_Medium_value_payments',
        'Pay_Behav_Low_spent_Small_value_payments'
    ]

    user_data.update({
        pb: int(pb == Payment_Behaviour)
        for pb in payment_behaviours
    })

    # ---------- Final DataFrame (Aligned with Training) ----------
    input_df = pd.DataFrame([user_data]).reindex(
        columns=X_train.columns,
        fill_value=0
    )

    return input_df
