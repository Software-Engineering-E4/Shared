/* responsive website */
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