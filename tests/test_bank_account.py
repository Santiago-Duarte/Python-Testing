import unittest
from src.bank_account import *
import os
from unittest.mock import patch
from src.exeptions import WithdrowalTimeRestrictionError

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists("transaction_log.txt"):
            os.remove("transaction_log.txt")

    def count_lines(self, filenames):
        with open(filenames, 'r') as f:
            return len(f.readlines())

    def test_deposit_when_valid_amount_is_provided_should_increase_balance(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    def test_withdraw_when_valid_amount_is_provided_should_decrease_balance(self):
        new_balance = self.account.withdraw(300)
        self.assertEqual(new_balance, 700, "El balance no es igual")

    def test_get_balance_when_account_is_initialized_should_return_current_balance(self):
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es igual")

    def test_transfer_when_enough_funds_are_available_should_move_balance_between_accounts(self):
        cuenta1 = BankAccount(1000)
        cuenta2 = BankAccount(500)
        cuenta1.transfer(200, cuenta2)
        self.assertEqual(cuenta1.get_balance(), 800, "El balance no es igual")
        self.assertEqual(cuenta2.get_balance(), 700, "El balance no es igual")

    def test_transfer_when_insufficient_funds_are_available_should_not_change_balances(self):
        cuenta1 = BankAccount(100)
        cuenta2 = BankAccount(500)
        cuenta1.transfer(200, cuenta2)
        self.assertEqual(cuenta1.get_balance(), 100, "El balance no es igual")  # Balance should remain unchanged
        self.assertEqual(cuenta2.get_balance(), 500, "El balance no es igual")  # Balance should remain unchanged

    def test_deposit_when_transaction_is_made_should_create_transaction_log_file(self):
        self.account.deposit(200)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transaction_when_multiple_transactions_are_added_should_return_number_of_lines(self):
        self.assertEqual(self.count_lines(self.account.log_file), 1)
        self.account.deposit(200)
        self.assertEqual(self.count_lines(self.account.log_file), 2)

    def test_transfer_when_funds_are_insufficient_should_log_error_message(self):
        cuenta1 = BankAccount(100, log_file="transaction_log.txt")
        cuenta2 = BankAccount(500, log_file="transaction_log.txt")
        cuenta1.transfer(200, cuenta2)
        with open("transaction_log.txt", 'r') as f:
            assert "Error during transfer" in f.read()

    @patch('src.bank_account.datetime')
    def test_withdrawal_during_bussine_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        mock_datetime.now.return_value.weekday.return_value = 4

        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800)

    @patch('src.bank_account.datetime')
    def test_withdrawal_disawoll_before_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrowalTimeRestrictionError):
            self.account.withdraw(200)

    @patch('src.bank_account.datetime')
    def test_withdrawal_disawoll_after_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrowalTimeRestrictionError):
            self.account.withdraw(200)

    @patch('src.bank_account.datetime')
    def test_withdrawal_allow(self, mock_datetime):
        # Configuramos una hora válida (ej. las 10 AM)
        mock_datetime.now.return_value.hour = 10
        # Configuramos que el método weekday() devuelva 4 (Viernes)
        mock_datetime.now.return_value.weekday.return_value = 4  
        
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800)

    @patch('src.bank_account.datetime')
    def test_withdrawal_disawoll_on_weekends(self, mock_datetime):
        # Configuramos una hora válida (ej. las 10 AM)
        mock_datetime.now.return_value.hour = 10
        # Configuramos que el método weekday() devuelva 5 (Sábado)
        mock_datetime.now.return_value.weekday.return_value = 5  
        
        with self.assertRaises(WithdrowalTimeRestrictionError):
            self.account.withdraw(200)

    
    def test_deposit_varios_amounts(self):
        test_cases = [
            {"amount": 100, "expected_balance": 1100},
            {"amount": 3000, "expected_balance": 4000},
            {"amount": 3500, "expected_balance": 4500}
        ]
        
        
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transaction_log.txt")  # Reset account for each subtest
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(
                    new_balance, case["expected_balance"], 
                    f"El balance no es igual para el depósito de {case['amount']}"
                )