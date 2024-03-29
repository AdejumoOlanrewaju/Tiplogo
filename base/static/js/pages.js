let overlay = document.querySelector(".overlay")
let hamburger = document.querySelector('.hamburger')
let hamburgerSpan = document.querySelectorAll(".hamburger span")
let navLinks = document.querySelectorAll("nav-links-parent a")
let mobileMenu = document.querySelector(".mobile-menu")
let closeMenu = document.querySelector(".close-menu")
let tabLinks = document.querySelectorAll(".tab-links")

window.addEventListener("scroll", () => {
    if(scrollY > 0){
        document.querySelector("nav").classList.add("active")
        // hamburgerSpan.forEach(el => el.style.backgroundColor = "black")
    
    }else{
        document.querySelector("nav").classList.remove("active")
        // hamburgerSpan.forEach(el => el.style.backgroundColor = "white")
    }
})

// hamburger.addEventListener("click", () => {
//     mobileMenu.classList.add("open")
//     overlay.style.display = "block"
//     // document.body.style.overflowY = "hidden"
// })

// closeMenu.addEventListener("click", () => {
//     mobileMenu.classList.remove("open")
//     overlay.style.display = "none"
//     // document.body.style.overflowY = "auto"


// })