/* identify "see all" */

const seeAllOptionTwitter = document.getElementById('twitter_see_all')
if(elementExistsInDom(seeAllOptionTwitter)){
    seeAllOptionTwitter.addEventListener("click", () => {
        var option = 'twitter';
        console.log(option);
        localStorage.setItem("vLocalStorage", option);
    });
}

const seeAllOptionReddit = document.getElementById('reddit_see_all')
if(elementExistsInDom(seeAllOptionReddit)){
    seeAllOptionReddit.addEventListener("click", () => {
        var option = 'reddit';
        localStorage.setItem("vLocalStorage", option);
    });
}

const seeAllOptionYoutube = document.getElementById('youtube_see_all')
if(elementExistsInDom(seeAllOptionYoutube)){
    seeAllOptionYoutube.addEventListener("click", () => {
        var option = 'youtube';
        localStorage.setItem("vLocalStorage", option);
    });
}

function elementExistsInDom(element){
    if(element == null){
        return false;
    }
    return true;
}
