from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.branches = []
        self.branch_opening_times = {}  # key: branch, value: opening time
        self.payroll = None

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)
        self.branch_opening_times[branch] = "9:00"  # default opening time

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        for staff in branch.get_staff():
            self.transfer_staff_member(branch, transfer_branch, staff)
        self.branches.remove(branch)

    def transfer_staff_member(self, from_branch: Branch, to_branch: Branch, staff: Staff):
        from_branch.get_staff().remove(staff)
        to_branch.get_staff().append(staff)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def add_interest(self, account: Account):
        account.add_interest()

    def add_funds(self, account: Account, amount: float):
        account.add_funds(amount)

    def close_account(self, account: Account):
        account.close_account()
        self.accounts.remove(account)

    def add_staff_member(self, branch: Branch, staff: Staff):
        branch.get_staff().append(staff)

    def change_opening_time(self, branch: Branch, time: str):
        self.branch_opening_times[branch] = time

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        self.payroll = payroll
        self.payroll.get_staff_category_pay_schedule(staff_category).set_pay_date(date)
