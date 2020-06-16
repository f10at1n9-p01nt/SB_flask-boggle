function displayResult(result) {
	$('.result').html(result);
}

function scoreWord(validity, word) {
	if (validity !== 'ok') {
		return;
	}
	if (!scoreWord.score) {
		scoreWord.score = {};
	}
}

async function checkGuess() {
	const word_value = $('#guess').val();
	const res = await axios.get('/check-word', { params: { word_value } });
	displayResult(res.data);
	return res.data;
}

$('button').on('click', checkGuess);
