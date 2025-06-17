import streamlit as st
from current_account import CurrentAccount
st.title('Current Account')

if 'account' not in st.session_state:
    st.session_state.account = CurrentAccount(balance=200000)

with st.form('transaction_form'):
    operation=st.selectbox('Action',('Deposit','Withdraw'))
    amount=st.number_input('Amount',min_value=0.01,step=1.00)
    submit=st.form_submit_button('Submit')

if submit:
    with st.spinner('Processing...'):
        if operation == 'Deposit':
            if st.session_state.account.deposit(amount):
                st.success('Deposited ${amount:.2f}')
            else:
               print ('Invalid deposit amount')
        else:
            if st.session_state.account.withdraw(amount):
                st.success(f'Withdrew ${amount:.2f}')
            else:
                st.error('withdrawal failed')

st.write(f'Current Balance : **${st.session_state.account.balance:.2f}')


