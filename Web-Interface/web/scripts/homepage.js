/* identify "see all" */
const seeAllOptionTwitter = document.getElementById('twitter_see_all')
seeAllOptionTwitter.addEventListener("click", () => {
    var option = 'twitter';
    localStorage.setItem("vLocalStorage", option);
});
const seeAllOptionReddit = document.getElementById('reddit_see_all')
seeAllOptionReddit.addEventListener("click", () => {
    var option = 'reddit';
    localStorage.setItem("vLocalStorage", option);
});
const seeAllOptionYoutube = document.getElementById('youtube_see_all')
seeAllOptionYoutube.addEventListener("click", () => {
    var option = 'youtube';
    localStorage.setItem("vLocalStorage", option);
});