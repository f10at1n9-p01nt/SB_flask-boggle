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


    def test_validate_word(self):
        with app.test_client() as client:
            board = client.get('/')
            res = client.get('/check-word?word_value="hotdogspinachbunsaregross"')
            # res.board = [["H", "O", "T", "T", "T"], 
            #                      ["C", "A", "T", "T", "T"], 
            #                      ["C", "A", "T", "T", "T"], 
            #                      ["C", "A", "T", "T", "T"], 
            #                      ["C", "A", "T", "T", "T"]]
            # with client.session_transaction() as change:
            #     change['board'] =[["H", "O", "T", "T", "T"], 
            #                      ["C", "A", "T", "T", "T"], 
            #                      ["C", "A", "T", "T", "T"], 
            #                      ["C", "A", "T", "T", "T"], 
            #                      ["C", "A", "T", "T", "T"]]
            self.assertIn(b'not-word', res.data)
    

    def test_update_stats(self):
        with app.test_client() as client:
            res = client.get('/stats')
            with client.session_transaction() as change:
                change['games_played'] = 5

            self.assertEqual(res.get_data(as_text=True), 5)


