from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class BoggleTestCase(TestCase):
    def test_create_board(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Boggle Board</h1>', html)
