// aos initialisation
AOS.init({
    offset: 100,
    delay: 100,
    duration: 700,
    easing: 'ease',
    once: false,
    mirror: false,
    anchorPlacement: 'top-bottom'
})
// making the nav links stay highlighted when clicked
const navLinks = document.querySelectorAll(".nav-list a")

navLinks.forEach(link =>{
    link.addEventListener("click", activeLink)
})

function activeLink() {
    navLinks.forEach(link => {
        link.classList.remove("active")
        this.classList.add("active")
        link.addEventListener("click", deactivateMobileNav)
    })
}

// the buttons in the navbar
const searchBtn = document.querySelector(".icons-box .search-btn")
const menuBtn = document.querySelector(".icons-box .menu-btn")
const closeNavBtn = document.querySelector(".nav-list .mobile-menu-close-btn")
const mobileNav = document.querySelector("nav .nav-list")
const searchForm = document.querySelector("nav form")

searchBtn.addEventListener("click", activateSearch)
menuBtn.addEventListener("click", activateMobileNav)
closeNavBtn.addEventListener("click", deactivateMobileNav)

function activateSearch() {
    searchForm.classList.toggle("active")
}
function activateMobileNav() {
    mobileNav.classList.add("active")
}
function deactivateMobileNav() {
    mobileNav.classList.remove("active")
}

// reducing the text length in the editor's pick in home
const postText = document.querySelectorAll(".latest-post-wrapper .post-text")

postText.forEach(text =>{
    const length = 90
    let insideText = text.innerHTML
    let trimmedString = insideText.substring(0, length)
    text.innerHTML = trimmedString + "..."
})
// reducing the text length in the most commented post in home
const commentText = document.querySelectorAll(".most-commented-wrapper .comment-text")

commentText.forEach(text =>{
    const length = 80
    let insideText = text.innerHTML
    let trimmedString = insideText.substring(0, length)
    text.innerHTML = trimmedString + "..."
})

// updating the date in the footer every year
const date = document.getElementById("date")
date.innerHTML = new Date().getFullYear()

// open the comment form in details.html when commenting on a post
const addCommentBtn = document.querySelector(".comments-wrapper .add-comment-btn")
const commentForm = document.querySelector(".comments-wrapper form")

addCommentBtn.addEventListener("click", openCommentForm)

function openCommentForm() {
    commentForm.classList.toggle("active")
    if(commentForm.classList.contains("active")){
        addCommentBtn.innerHTML = "Add a new comment <i class='fas fa-minus add-comment-icon'></i>"
    } else {
        addCommentBtn.innerHTML = "Add a new comment <i class='fas fa-plus add-comment-icon'></i>"
    }
}
// when your comment is added, this message displays
const msgAdded = document.querySelector(".comment-added-msg")

setTimeout(() => {
    msgAdded.style.display = "none"
}, 3000);