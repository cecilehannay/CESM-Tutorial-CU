// Tag exercise/homework pages so custom.css can give them a distinct background.
// A page counts as an exercise if its filename contains "exercise" or "homework"
// (e.g. 4.3_exercise1.html, 5.4_homework.html) OR its title starts with
// "Exercise" / "Homework" (e.g. "Exercise: Download CESM").
document.addEventListener("DOMContentLoaded", function () {
  var path = window.location.pathname.toLowerCase();
  var byPath = path.indexOf("exercise") !== -1 || path.indexOf("homework") !== -1;
  var h1 = document.querySelector("article.bd-article h1");
  var title = h1 ? h1.textContent.trim().toLowerCase() : "";
  var byTitle = title.indexOf("exercise") === 0 || title.indexOf("homework") === 0;
  if (byPath || byTitle) {
    var article = document.querySelector("article.bd-article");
    if (article) {
      article.classList.add("is-exercise-page");
    }
  }
});
