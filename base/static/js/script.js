console.log("hi there")

let nextBtn = document.querySelector(".next.btn")
let prevBtn = document.querySelector(".prev.btn")
let carouselContainer = document.querySelector(".carousel-container")
let carouselItems = document.querySelectorAll(".carousel-item")
let hamburger = document.querySelector('.hamburger')
let mobileMenu = document.querySelector(".mobile-menu")
let closeMenu = document.querySelector(".close-menu")

let counter = 0
let touchStartX
let touchEndX
let swipeDifference
let threshold = 50

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
    intervalId = setInterval(nextImage, 5000)
}

// autoSlide()

function touchSlide(){
    carouselContainer.addEventListener("touchstart", (e) => {
        touchStartX = e.client[0].touches
    })
    

    carouselContainer.addEventListener("touchmove", () => {
        touchEndX = e.client[0].touches
    })

    carouselContainer.addEventListener("touchend", () => {
        swipeDifference = touchStartX - touchEndX
        console.log(swipeDifference)

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
})

closeMenu.addEventListener("click", () => {
    mobileMenu.classList.remove("open")
})