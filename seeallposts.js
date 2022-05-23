/* style the content for every category */
var optionFromLocalStorage = localStorage.getItem("vLocalStorage");
var option = optionFromLocalStorage;
identifyThePlatform();

function identifyThePlatform() {
    var twitter = 'twitter';
    if(option === twitter)
        loadTwitterPosts();
    var reddit = 'reddit';
    if(option === reddit)
        loadRedditPosts();
    var youtube = 'youtube';
    if(option === youtube)
        loadYoutubePosts();
}


function loadTwitterPosts() {
    /* add right title */
    document.getElementById("platform_name").innerHTML = 'Twitter';
    var elem;
    elem = document.querySelector(".platform_name");
    elem.classList.toggle('twitter');

    /* add right styled posts */
    var list; var index;
    list = document.querySelectorAll(".platform");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('twitter');
    list = document.querySelectorAll(".platform_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('twitter_post');

}

function loadRedditPosts() {
    document.getElementById("platform_name").innerHTML = 'Reddit';
    var elem;
    elem = document.querySelector(".platform_name");
    elem.classList.toggle('reddit');

    var list; var index;
    list = document.querySelectorAll(".platform");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('reddit');
    list = document.querySelectorAll(".platform_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('reddit_post');

}

function loadYoutubePosts() {
    document.getElementById("platform_name").innerHTML = 'YouTube';
    var elem; 
    elem = document.querySelector(".platform_name");
    elem.classList.toggle('youtube');

    var list; var index;
    list = document.querySelectorAll(".platform");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('youtube');
    list = document.querySelectorAll(".platform_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('youtube_post');
    var a = document.querySelectorAll(".post");
    
    addHTMLElements();

    removeParagraphs();
}

function removeParagraphs() {
    list = document.querySelectorAll(".description");
    for(index = 0; index < list.length; index++)
        list[index].remove();
}

function addHTMLElements() {
    var list = document.getElementsByClassName('post');
    for(index = 0; index < list.length; index++) {
        
        /* build new HTML elements */
        const divElement = document.createElement('div');
        divElement.classList.toggle('for_image');
        const imgElement = document.createElement('img');
        imgElement.classList.toggle('youtube_image');
        //imgElement.src = "images/youtube.jpg";

        /* append img to div */
        divElement.appendChild(imgElement);

        /* append div to a */
        list[index].appendChild(divElement);
    }
}