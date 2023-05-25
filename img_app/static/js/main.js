// const modal_cards_1 = document.querySelector('.vacancies__cards-list');
// const toggleButton1 = document.querySelector('.toggleButton1').addEventListener('click', function() {
//   if (modal_cards_1.style === 'display: none;') {
//     modal_cards_1.classList.remove('hidden');
//   } else if (modal_cards_1.style === 'display: flex;') {
//     modal_cards_1.classList.add('hidden');
//   }
// });

const modal_cards_1 = document.querySelector('.new-vacancies');
const modal_cards_2 = document.querySelector('.working-home');
const modal_cards_3 = document.querySelector('.part-time-job');
const modal_cards_4 = document.querySelector('.without-experience');

const toggleButton1 = document.querySelector('.toggleButton1').addEventListener('click', function() {
  modal_cards_1.classList.remove('hidden');
  modal_cards_2.classList.add('hidden');
  modal_cards_3.classList.add('hidden');
  modal_cards_4.classList.add('hidden');
});

const toggleButton2 = document.querySelector('.toggleButton2').addEventListener('click', function() {
  modal_cards_1.classList.add('hidden');
  modal_cards_2.classList.remove('hidden');
  modal_cards_3.classList.add('hidden');
  modal_cards_4.classList.add('hidden');
});

const toggleButton3 = document.querySelector('.toggleButton3').addEventListener('click', function() {
  modal_cards_1.classList.add('hidden');
  modal_cards_2.classList.add('hidden');
  modal_cards_3.classList.remove('hidden');
  modal_cards_4.classList.add('hidden');
});

const toggleButton4 = document.querySelector('.toggleButton4').addEventListener('click', function() {
  modal_cards_1.classList.add('hidden');
  modal_cards_2.classList.add('hidden');
  modal_cards_3.classList.add('hidden');
  modal_cards_4.classList.remove('hidden');
});