/* change theme status */
const button = document.getElementById("change_theme");
const buttonPhone = document.getElementById("phone_change_theme");
/* normal screen */
button.addEventListener('click',() => {

    // 1st time
    if(localStorage.getItem("vDark") === null) {
        localStorage.setItem("vDark", 'true');
        changeColors();
    }
    else {
        checkAndChangeStatus();
        changeColors();
    }
});
/* phone screen */
buttonPhone.addEventListener('click',() => {
    // 1st time
    if(localStorage.getItem("vDark") === null) {
        localStorage.setItem("vDark", 'true');
        changeColors();
    }
    else {
        checkAndChangeStatus();
        changeColors();
    }
});

function checkAndChangeStatus() {
    if(localStorage.getItem("vDark") === 'true')
            localStorage.setItem("vDark", 'false');
        else
            localStorage.setItem("vDark", 'true');
}

function  changeColors() {
    document.body.classList.toggle('dark-theme');
    var index;
    var list;
    /* header content & footer */
    list = document.querySelectorAll(".navig_line, .search_bar, .site_name, .right_container, .home, .categories, .statistics, .about, .menu_option, .footer");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme');
    /* div for theme button */
    button.classList.toggle('dark-theme-btn');
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
    // search content
    list = document.querySelectorAll(".see_more");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-grey-overlap');   
    /* seeallposts content */
    list = document.querySelectorAll(".platform_name, .platform");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-dark-grey');
    list = document.querySelectorAll(".platform_post .twitter_post, .platform_post .reddit_post, .platform_post .youtube_post");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-grey');
    list = document.querySelectorAll(".bseemoreitems");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-grey');
    /* twitter post & reddit post */
    list = document.querySelectorAll(".main, .platform_name .twitter");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-dark-grey');
    list = document.querySelectorAll(".title_and_description, .stats_and_review");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-grey');
    /* homepage's & seeallposts' text content AND post's text*/
    list = document.querySelectorAll(".title, .description");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-light-grey');

    /* for phone */
    list = document.querySelectorAll(".phone.options, .phone.container, .phone_list_element, .phone_list_element.change_theme, .phone.change_theme");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme-phone');

    /* statistics content */
    list = document.querySelector(".intro");
    list.classList.toggle('dark-theme');
    
    /* about us content */
    list = document.querySelectorAll(".about_content");
    for(index = 0; index < list.length; index++)
        list[index].classList.toggle('dark-theme');
    }