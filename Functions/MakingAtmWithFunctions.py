#Make a ATM.
#It should have a regular account and a flexible account.
#If there is insufficient money in the regular account, withdraw the money from the flexible account.
#Before withdrawing from the flexible account, ask 'Do you confirm the withdrawal from the flexible account?'.

yusufAcc= {
    'name':'Yusuf Gulumser',
    'accNum': '123453243',
    'balance':3000,
    'flexAcc':2000
}

veliAcc= {
    'name':'Veli Kaya',
    'accNum': '124453343',
    'balance':2000,
    'flexAcc':1000
}

def withdraw(account,amount):
    print(f"Merhaba {account['name']}")

    if (account['balance'] >= amount):
        account['balance']-=amount                   #decrease the withdrawn money from the balance
        print('you can take your money')
    else:
        total= account['balance'] + account['flexAcc']
        if (total>= amount):
            flexAccUsage= input('do you want to use money from your flex account?(y/n)')
            if flexAccUsage=='y':
                flexaccbalancegonnause= amount - account['balance']
                account['balance']=0
                account['flexAcc']-=flexaccbalancegonnause
                print('you can take your money')
            else:
                print(f"you have {account['balance']}$ in account number {account['accNum']} ")

        else:
            print('sorry,insufficient balance')




withdraw(yusufAcc,3000)
withdraw(yusufAcc,2000)