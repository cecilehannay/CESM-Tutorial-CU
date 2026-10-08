// Tag exercise/homework pages so custom.css can give them a distinct background.
// Based on the page's filename, which already consistently includes "exercise" or
// "homework" (e.g. 4.3_exercise1.html, 5.4_homework.html) — no per-notebook edits needed.
document.addEventListener("DOMContentLoaded", function () {
  var path = window.location.pathname.toLowerCase();
  if (path.indexOf("exercise") !== -1 || path.indexOf("homework") !== -1) {
    var article = document.querySelector("article.bd-article");
    if (article) {
      article.classList.add("is-exercise-page");
    }
  }
});
