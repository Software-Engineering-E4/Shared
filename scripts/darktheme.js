/* change theme */
const change_theme = document.getElementById("checkbox");

change_theme.addEventListener('change',() => {
    
    document.body.classList.toggle('dark-theme');
    
    var index;
    var list;
    /* header content & footer */
    list = document.querySelectorAll(".navig_line, .search_bar, .site_name, .right_container, .latest, .categories, .statistics, .about, .menu_option, .footer");
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
    list = document.querySelectorAll(".see_all");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-grey-overlap');
    /* seeallposts content */
    list = document.querySelectorAll(".platform_name, .platform");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-dark-grey');
    list = document.querySelectorAll(".platform_post .twitter_post, .platform_post .reddit_post, .platform_post .youtube_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-grey');
    /* homepage & seeallposts content */
    list = document.querySelectorAll(".title, .description");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-light-grey');
});
