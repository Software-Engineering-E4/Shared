/* style the content for every category */
var optionFromLocalStorage = localStorage.getItem("vLocalStorage");
var option = optionFromLocalStorage;

if(option === 'twitter') {
    document.getElementById("platform_name").innerHTML = 'Twitter';
    var elem;
    elem = document.querySelector(".platform_name");
    elem.classList.toggle('twitter');

    var list;
    list = document.querySelectorAll(".platform");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('twitter');
    list = document.querySelectorAll(".platform_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('twitter_post');
}

if(option === 'reddit') {
    document.getElementById("platform_name").innerHTML = 'Reddit';
    var elem;
    elem = document.querySelector(".platform_name");
    elem.classList.toggle('reddit');

    var list;
    list = document.querySelectorAll(".platform");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('reddit');
    list = document.querySelectorAll(".platform_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('reddit_post');
}

if(option === 'youtube') {
    document.getElementById("platform_name").innerHTML = 'YouTube';
    var elem;
    elem = document.querySelector(".platform_name");
    elem.classList.toggle('youtube');

    var list;
    list = document.querySelectorAll(".platform");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('youtube');
    list = document.querySelectorAll(".platform_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('youtube_post');
}