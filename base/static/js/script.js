let overlay = document.querySelector(".overlay")
let nextBtn = document.querySelector(".next.btn")
let prevBtn = document.querySelector(".prev.btn")
let carouselContainer = document.querySelector(".carousel-container")
let carouselItems = document.querySelectorAll(".carousel-item")
let hamburger = document.querySelector('.hamburger')
let hamburgerSpan = document.querySelectorAll(".hamburger span")
let navLinks = document.querySelectorAll("nav-links-parent a")
let mobileMenu = document.querySelector(".mobile-menu")
let closeMenu = document.querySelector(".close-menu")
let tabLinks = document.querySelectorAll(".tab-links")
let tabLine = document.querySelector(".tab-line")

let counter = 0
let touchStartX
let touchEndX
let swipeDifference
let threshold = 50

tabLine.style.width = `${tabLinks[0].offsetWidth}px`
tabLine.style.left = `${tabLinks[0].offsetLeft}px`
tabLine.style.opacity = "1"

window.addEventListener("scroll", () => {
    if(scrollY > 0){
        document.querySelector("nav").classList.add("active")
        // hamburgerSpan.forEach(el => el.style.backgroundColor = "black")
       
    }else{
        document.querySelector("nav").classList.remove("active")
        // hamburgerSpan.forEach(el => el.style.backgroundColor = "white")
    }
})

// Script for tab system in product page
let width;
let leftPosition
tabLinks.forEach((link, index) => {
    link.addEventListener("click", () => {
        width = link.offsetWidth
        leftPosition = link.offsetLeft
        tabLine.style.width = `${link.offsetWidth}px`
        tabLine.style.left = `${link.offsetLeft}px`
        // tabLine.style.left = `${(index / tabLinks.length) * 100}%`
        console.log(((index + 1) / tabLinks.length) * 100)
        
    })
}) 

// for(let [index, link] of tabLinks.entries()){
//     console.log(index, link)
// }

/**
 * (index/items.length) * 100%
 */

nextBtn.addEventListener("click", nextImage)
function nextImage(){
    carouselItems[counter].style.animation = "next1 .5s ease forwards"

    if(counter >= carouselItems.length - 1){
        counter = 0
    }else{
        counter++
    }

    console.log(counter)
    carouselItems[counter].style.animation = "next2 .5s ease forwards"
}

prevBtn.addEventListener("click", prevImage)
function prevImage(){
    if(counter == 0)return;

    carouselItems[counter].style.animation = "prev1 .5s ease forwards"

    if(counter <= 0){
        counter = 0
    }else{
        counter--
    }

    carouselItems[counter].style.animation = "prev2 .5s ease forwards"
}

let intervalId

function autoSlide(){
    intervalId = setInterval(nextImage, 3000)
}

// autoSlide()

function touchSlide(){
    carouselContainer.addEventListener("touchstart", (e) => {
        touchStartX = e.touches[0].clientX
    })
    

    carouselContainer.addEventListener("touchmove", (e) => {
        touchEndX = e.touches[0].clientX
        // console.log(touchEndX)

    })

    carouselContainer.addEventListener("touchend", function(e){
        // carouselItems.forEach(el => {
        //     console.log(el.childNodes)
        // })

        //this script is to prevent swipe if we click on any of the children of the carousel items
        if(e.target.closest(".carousel-item > button "))return

        swipeDifference = touchStartX - touchEndX
        if(swipeDifference > threshold){
            console.log("swiped right")
            nextImage()
        }else if(swipeDifference < -threshold){
            console.log("swiped left")
            prevImage()
        }
    })
}

touchSlide()

carouselContainer.addEventListener("mouseenter", ()=>{
    clearInterval(intervalId)
})

carouselContainer.addEventListener("mouseleave", () => {
    // autoSlide()
})

hamburger.addEventListener("click", () => {
    mobileMenu.classList.add("open")
    overlay.style.display = "block"
    // document.body.style.overflowY = "hidden"
})

closeMenu.addEventListener("click", () => {
    mobileMenu.classList.remove("open")
    overlay.style.display = "none"
    // document.body.style.overflowY = "auto"


})