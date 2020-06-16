function displayResult(result) {
	$('.result').html(result);
}
// score = 0;

// function scoreWord(validity, word) {
// 	if (validity === 'ok') {
// 		return (score += word.length);
// 	}
// 	return score;
// }
// Testing memoization. Not a great idea if running multiple games.
function scoreWord(validity, word, reset) {
	if (!scoreWord.score || reset === true) {
		scoreWord.score = 0;
	}

	if (validity !== 'ok') {
		return scoreWord.score;
	}

	scoreWord.score += word.length;
	return scoreWord.score;
}

async function checkGuess() {
	const word_value = $('#guess').val();
	const res = await axios.get('/check-word', { params: { word_value } });
	displayResult(res.data);
	return res.data;
}

$('button').on('click', checkGuess);
