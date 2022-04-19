/* scripts for responsive website */
const menuBtn = document.querySelector('.menu-btn')
const navlinks = document.querySelector('ul.right_container')
menuBtn.addEventListener('click', () => {
            navlinks.classList.toggle('mobile-menu')
})

const searchBtn = document.querySelector('.search-btn')
const searchlink = document.querySelector('div.search_bar')
searchBtn.addEventListener('click', () => {
            searchlink.classList.toggle('search_menu')
})


/* change theme */
const change_theme = document.getElementById("change_theme");

change_theme.addEventListener('change',() => {
    document.body.classList.toggle('dark');
    var list = document.querySelectorAll(".titles, .most_reviewed, .twitter, .reddit, .youtube, .categories, .twitter");
    var index;
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-gray');
    var list = document.querySelectorAll(".most_reviewed_post, .twitter_post, .reddit_post, .youtube_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('light-gray');
    });


    /*
    var h2 = document.getElementById('titles');
    h2.classList.toggle('dark');
    var h2 = document.getElementById('Categories');
    h2.classList.toggle('dark');
    document.que
    */
