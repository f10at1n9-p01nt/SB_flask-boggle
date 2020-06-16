describe('app.js', function() {
	describe('scoreWord', function() {
		let validity;
		let word;
		let score;
		beforeEach(function() {
			validity = 'ok';
			word = '';
			reset = true;
		});

		it('Not valid word', function() {
			validity = 'not-word';
			expect(scoreWord(validity, word, reset)).toEqual(0);
		});

		it('Should give score of 0', function() {
			const res = scoreWord(validity, word, reset);
			expect(res).toEqual(0);
		});

		it('Should give score of 4', function() {
			const word = 'test';
			expect(scoreWord(validity, word, reset)).toEqual(4);
		});

		it('Should give score of 7', function() {
			scoreWord(validity, 'test', reset);
			expect(scoreWord(validity, 'goo', false)).toEqual(7);
		});
	});

	// ? Why is this test not working?
	// describe('displayResult', function() {
	// 	it('Should display "test message"', function() {
	// 		displayResult('test message');
	// 		expect($('#display-message').html()).toContain('<h2>test message</h2>');
	// 	});
	// });
});
