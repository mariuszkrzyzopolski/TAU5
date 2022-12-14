import unittest

from zad1.main import statement


class StatementTest(unittest.TestCase):
    def test_sample_statement(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                },
                {
                    "playID": "as-like",
                    "audience": 35
                },
                {
                    "playID": "othello",
                    "audience": 40
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }
        sample = """Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n"""
        self.assertEqual(sample, statement(invoice, plays))

    def test_single_comedy_statement(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "as-like",
                    "audience": 35
                }
            ]
        }
        plays = {
            "as-like": {"name": "As You Like It", "type": "comedy"},
        }
        sample = """Statement for BigCo\n As You Like It: $580.00 (35 seats)\nAmount owed is $580.00\nYou earned 12 credits\n"""
        self.assertEqual(sample, statement(invoice, plays))

    def test_single_tragedy_statement(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"}
        }
        sample = """Statement for BigCo\n Hamlet: $650.00 (55 seats)\nAmount owed is $650.00\nYou earned 25 credits\n"""
        self.assertEqual(sample, statement(invoice, plays))

    def test_unknown_type_statement(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                }
            ]
        }
        plays = {
            "hamlet": {"name": "Hamlet", "type": "drama"}
        }
        self.assertRaises(ValueError, statement, invoice, plays)