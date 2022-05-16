/* responsive website */
const menuBtn = document.querySelector('.menu-btn')
const divContainer = document.querySelector(".phone.options");
menuBtn.addEventListener('click', () => {
            divContainer.classList.toggle('mobile-menu')
})

const searchBtn = document.querySelector('.search-btn')
const searchlink = document.querySelector('div.search_bar')

searchBtn.addEventListener('click', () => {
            searchlink.classList.toggle('search_menu')
})