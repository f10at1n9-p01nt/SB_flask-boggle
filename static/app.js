guessedWords = [];
// const timerInstance = new easytimer.Timer();
const timer = new Timer();

function displayResult(result, displayClass) {
	$(`.${displayClass}`).html(result);
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

async function guessHandler() {
	console.log(guessedWords);
	const word_value = $('#guess').val();
	const res = await axios.get('/check-word', { params: { word_value } });

	displayResult(res.data, 'word-message');
	// Check if word already played
	// Todo: Display message if already played and ok
	if (!guessedWords.includes(word_value) && res.data === 'ok') {
		guessedWords.push(word_value);
		displayResult(scoreWord(res.data, word_value, false), 'score');
	}

	$('form').trigger('reset');
	return res.data;
}

async function storeGameStats() {
	let score;
	$('.score').html() ? (score = $('.score').html()) : (score = 0);
	console.log(score);
	const gamesPlayed = await axios.post('/stats', { game_score: score });
	console.log(gamesPlayed);
}

$('button').on('click', guessHandler);

// Followed easytimer docs
timer.start({ countdown: true, startValues: { seconds: 10 } });
$('.timer').html(timer.getTimeValues().toString());

timer.addEventListener('secondsUpdated', function(e) {
	$('.timer').html(timer.getTimeValues().toString());
});

timer.addEventListener('targetAchieved', function(e) {
	$('form').hide();
	$('.timer').html('Game Over!');
	storeGameStats();
});
