from flask import Flask, render_template, request, redirect, url_for, flash
from client import Client
from bank import Bank

app = Flask(__name__)
app.secret_key = 'some_secret'

bank = Bank()

@app.route('/')
def home():
    return render_template('home.html', bank_name=bank.name)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        name = request.form['name']
        deposit = int(request.form['deposit'])
        client = Client(name, deposit)
        bank.update_db(client)
        flash(f'Account created successfully! Your account number is {client.account["account_number"]}')
        return redirect(url_for('home'))
    return render_template('create_account.html')

@app.route('/access_account', methods=['GET', 'POST'])
def access_account():
    if request.method == 'POST':
        name = request.form['name']
        account_number = int(request.form['account_number'])
        current_client = bank.authentication(name, account_number)
        if current_client:
            return redirect(url_for('account_actions', name=name, account_number=account_number))
        else:
            flash('Authentication failed! Reason: Account not found.')
            return redirect(url_for('home'))
    return render_template('access_account.html')

@app.route('/account_actions/<name>/<int:account_number>', methods=['GET', 'POST'])
def account_actions(name, account_number):
    current_client = bank.authentication(name, account_number)
    if request.method == 'POST':
        action = request.form['action']
        amount = int(request.form['amount'])
        if action == 'withdraw':
            current_client.withdraw(amount)
        elif action == 'deposit':
            current_client.deposit(amount)
        flash(f'Action {action} completed!')
        return redirect(url_for('account_actions', name=name, account_number=account_number))
    return render_template('account_actions.html', client=current_client)

if __name__ == '__main__':
    app.run(debug=True)
