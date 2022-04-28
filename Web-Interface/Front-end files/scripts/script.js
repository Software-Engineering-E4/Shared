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
    
    document.body.classList.toggle('dark-theme');
    
    var index;
    var list;
    /* header content & footer */
    list = document.querySelectorAll(".navig_line, .search_bar, .right_container, .latest, .categories, .about, .menu_option, .footer");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme');
    /* homepage content */
    list = document.querySelectorAll(".titles, .most_reviewed, .Categories");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-dark-grey');
    list = document.querySelectorAll(".twitter, .reddit, .youtube");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-dark-grey-overlap');   
    list = document.querySelectorAll(".most_reviewed_post, .twitter_post, .reddit_post, .youtube_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-grey');
    list = document.querySelectorAll(".title, .description");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-light-grey');
});
