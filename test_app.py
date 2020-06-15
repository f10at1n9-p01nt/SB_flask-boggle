from unittest import TestCase
from app import app

class BoggleTestCase(TestCase):
    def test_display_board(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Boggle Board</h1>', html)