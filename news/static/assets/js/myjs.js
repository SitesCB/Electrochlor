const radioButtons = document.querySelectorAll('input[type="radio"]');
const array1 = document.getElementById('tab_faq');
const array2 = document.getElementById('tab_faq_1');
const array3 = document.getElementById('tab_faq_2');
const array4 = document.getElementById('tab_faq_3');
const array5 = document.getElementById('tab_faq_4');

radioButtons.forEach((radioButton) => {
  radioButton.addEventListener('change', () => {
    if (radioButton.checked && radioButton.id === 'faq') {
      array1.style.display = 'flex';
    } else {
        array1.style.display = 'none';
    }
     if (radioButton.checked && radioButton.id === 'faq_1') {
      array2.style.display = 'flex';
    } else {
        array2.style.display = 'none';
    }
     if (radioButton.checked && radioButton.id === 'faq_2') {
      array3.style.display = 'flex';
    } else {
        array3.style.display = 'none';
    }
    if (radioButton.checked && radioButton.id === 'faq_3') {
      array4.style.display = 'flex';
    } else {
        array4.style.display = 'none';
    }
    if (radioButton.checked && radioButton.id === 'faq_4') {
      array5.style.display = 'flex';
    } else {
        array5.style.display = 'none';
    }
  });
});