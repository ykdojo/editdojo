/**
 * Text difference module
 * Relevant functions:
 * @method longestCommonSubsequence - used to find common phrases between 2 pieces of text.
 * @method getDifferenceStrings - used to construct a string to disply in HTML highlighting differences.
 */

// Returns difference strings from 2 pieces of text.
function findTextDifference(originalText, changedText) {
  let originalWords = originalText.split(" ");
  let changedWords = changedText.split(" ");

  let commonPhrases = longestCommonSubsequence(originalWords, changedWords);

  return getDifferenceStrings(commonPhrases, originalWords, changedWords);
}

// Dynamic programming longest common subsequence algorithm.
let arr = undefined;

function longestCommonSubsequence(a, b) {
  let m = a.length;
  let n = b.length;
  arr = [...Array(m + 1)].map(e => Array(n + 1));
  return lcs(a, b, m, n);
}

function lcs(a, b, m, n) {
  if (arr[m][n] != undefined) {
    return arr[m][n];
  }

  let result = undefined;
  if (m === 0 || n === 0) {
    result = [];
  } else if (a[m - 1] === b[n - 1]) {
    result = lcs(a, b, m - 1, n - 1).concat(a[m - 1]);
  } else {
    let lcs1 = lcs(a, b, m - 1, n);
    let lcs2 = lcs(a, b, m, n - 1);
    result = lcs1 > lcs2 ? lcs1 : lcs2;
  }

  arr[m][n] = result;
  return result;
}

// Constructs 3 strings that highlight the differences (deletions & additions) between 2 texts.
function getDifferenceStrings(commonPhrases, originalWords, changedWords) {
  let differenceStr = "";
  let deletionsStr = "";
  let additionsStr = "";

  for (let i = 0; i <= commonPhrases.length; i++) {
    let phrase = "";
    let phraseIdxO = originalWords.length;
    let phraseIdxC = changedWords.length;

    if (i !== commonPhrases.length) {
      phrase = commonPhrases[i];
      phraseIdxO = originalWords.indexOf(phrase);
      phraseIdxC = changedWords.indexOf(phrase);
    }

    let deletedStr = substringFromWordlist(originalWords, 0, phraseIdxO);
    let addedStr = substringFromWordlist(changedWords, 0, phraseIdxC);

    differenceStr += `
      <span class="deleted">${deletedStr}</span>
      <span class="added">${addedStr}</span>
      <span class="unchanged">${phrase}</span>
    `;
    deletionsStr += `
      <span class="deleted">${deletedStr}</span>
      <span class="unchanged">${phrase}</span>
    `;
    additionsStr += `
      <span class="added">${addedStr}</span>
      <span class="unchanged">${phrase}</span>
    `;

    originalWords.splice(0, phraseIdxO + 1);
    changedWords.splice(0, phraseIdxC + 1);
  }

  return [differenceStr, deletionsStr, additionsStr];
}

function substringFromWordlist(wordlist, start, end) {
  if (end < start) return "";
  let words = wordlist.slice(start, end);
  return arrToString(words);
}

function arrToString(arr) {
  str = "";
  for (let i = 0; i < arr.length; i++) {
    str += arr[i] + " ";
  }
  return str;
}
