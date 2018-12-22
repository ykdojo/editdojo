// This is the script for the language selection page.

let languageList = ['English', 'Japanese'];

// given learningOrFluent, the new id for the selection element,
// and a new language list, this generates and returns a new HTML snippet
// for language selection.
function generateSelectHTML(learningOrFluent, id, newLanguageList){
  let languageListHTML = '';
  newLanguageList.forEach(language => {
    languageListHTML += `<option>${language}</option>`
  });
  let selectHTML = 
    `<select class="custom-select ed-select" name="${learningOrFluent}${id}">
      <option>Select Additional Language (if any)</option>
      ${languageListHTML}
    </select>`;
  return selectHTML;
}

function attachSelectionListener(learningOrFluent){
  $(`#${learningOrFluent}1`).on('change', function(){
    $(this).nextAll().animate({height:0, padding:0}, 100);
    let animatePromise = $(this).nextAll().promise();

    animatePromise.done(() => {
      // First, remove the faded-out content.
      $(this).nextAll().remove();

      let selectedLanguage = this.value;
      // Then, if the user has selected "Select Langauge (if any)", do nothing.
      if(!languageList.includes(selectedLanguage)){
        return;
      }

      // Otherwise, make a deep copy of languageList
      let newLanguageList = JSON.parse(JSON.stringify(languageList));
      // Then, remove selectedLanguage from the new list
      let i = newLanguageList.indexOf(selectedLanguage);
      newLanguageList.splice(i, 1);

      // Finally, generate select HTML from the new list.
      let selectHTML = generateSelectHTML(learningOrFluent, 2, newLanguageList);

      // Also, add a plus button and add a listner to it.
      $(`#${learningOrFluent}-select`).append(`<img src="/static/icons/plus_sign_icon_rainbow.png" alt="Select More Languages" class="ed-plus-sign" style="display: none;">`);
      $(this).nextAll().fadeIn(100);
      $(this).nextAll().on('click', function(){
        $(this).replaceWith(selectHTML);
      });
    });
  });
};

['learning', 'fluent'].forEach(learningOrFluent => {
  attachSelectionListener(learningOrFluent);
});