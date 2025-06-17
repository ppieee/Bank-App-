import streamlit as st
from Savings_account import SavingsAccount

st.title('savings Account')

if 'account' not in st.session_state:
    st.session_state.account = SavingsAccount(balance=200000, withdrawal_limit=100)

with st.form ('transaction_form'):
    operation= st.selectbox('Action',('Deposit','Withdrawal'))
    amount=st.number_input('Amount',min_value=0.00,step=1.00)
    submit=st.form_submit_button('Submit')

if submit:
    with st.spinner('Processing...'):
        if operation == 'Deposit':
            if st.session_state.account.deposit(amount):
                st.success(f'Deposited ${amount:.2f}')
            else:
                st.error('Invalid deposit amount')
        if operation == 'Withdraw':
            if st.session_state.account.withdraw(amount):
                st.success(f'Withdrew ${amount:.2f}')
            else:
                st.error('withdrawal failed')
st.write(f'Current Balance : **${st.session_state.account.balance:.2f}')
st.write(f'Withdrawal limit: **${st.session_state.account.withdrawal_limit:.2f}')

