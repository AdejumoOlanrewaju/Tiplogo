let home = document.querySelector(".home")
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
let productBoxes = document.querySelectorAll(".product-box")
let serviceBox = document.querySelectorAll(".service-box")
let testimonialScrollSection = document.querySelector(".testimonial-scroll-section")
let testimonialScrollBtn = document.querySelectorAll(".testimonial-btn-container button")
let testimonial = document.querySelectorAll(".testimonial")
let overlay = document.querySelector(".overlay")

let counter = 0
let touchStartX
let touchEndX
let swipeDifference
let threshold = 50

if(carouselContainer){
    console.log("hello")
    tabLine.style.width = `${tabLinks[0].offsetWidth}px`
    tabLine.style.left = `${tabLinks[0].offsetLeft}px`
    tabLine.style.opacity = 1

    let width;
    let leftPosition
    tabLinks.forEach((link, index) => {
        link.addEventListener("click", (e) => {
            animateTabline(e, link)
            categorizeProducts(link)
        }) 

    })

    // Script for tab system in product page
    function animateTabline(e, link){
        e.preventDefault()
        width = link.offsetWidth
        leftPosition = link.offsetLeft
        tabLine.style.width = `${width}px`
        tabLine.style.left = `${leftPosition}px`   
    }

    let removeMisEl = document.querySelectorAll(".remove_mis") 
    function categorizeProducts(link){
        if(link.dataset.category == "all"){
            productBoxes.forEach(el => {
                el.classList.remove("hide")
                setTimeout(() => {
                    el.style.display = "block" 
                    el.style.width = '300px'
                    el.style.maxHeight = '450px'
                    el.classList.add("show") 
                    removeMisEl.forEach((el) => {
                        el.classList.add("hide")
                        el.classList.remove("show")
                        el.style.width = '0px'
                        el.style.maxHeight = '0px'
                        el.style.display = "none" 
                    })
                }, 500)
            })

        }else{
            productBoxes.forEach(el => {
                el.classList.remove("show")
                el.classList.add("hide")
                setTimeout(() => {
                    el.style.width = 0
                    el.style.maxHeight = 0
                    el.style.display = "none"
                }, 50)
            })

            document.querySelectorAll(`#${link.dataset.category}`).forEach(el => {
                setTimeout(() => {
                    el.style.display = "block"
                    el.classList.remove("hide")
                    el.style.width = '300px'
                    el.style.maxHeight = '450px'
                    el.classList.add("show") 
                }, 500)
            })

        }
    }

    nextBtn.addEventListener("click", (e) => {
        clearInterval(intervalId)
        setTimeout(() => {
            autoSlide()
        }, 2000)
        nextImage()
    })

    function nextImage(){
        carouselItems[counter].style.animation = "next1 .5s ease forwards"

        if(counter >= carouselItems.length - 1){
            counter = 0
        }else{
            counter++
        }

        // console.log(counter)
        carouselItems[counter].style.animation = "next2 .5s ease forwards"
    }

    prevBtn.addEventListener("click", () => {
        clearInterval(intervalId)
        setTimeout(() => {
            autoSlide()
        }, 2000)
        prevImage()
    })
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

    //  autoSlide()

    function touchSlide(){
        carouselContainer.addEventListener("touchstart", (e) => {
            touchStartX = e.touches[0].clientX
        })
        

        carouselContainer.addEventListener("touchmove", (e) => {
            touchEndX = e.touches[0].clientX
            // console.log(touchEndX)

        })

        carouselContainer.addEventListener("touchend", function(e){
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



    // Script for handling responsive navigation

    let tesCount = 0
    testimonialScrollBtn.forEach(btn => btn.addEventListener("click", ChangeTesMove))

    let moveX = 0
    function ChangeTesMove(){
        let tesWidth;
        testimonial.forEach(el =>  {
            tesWidth = el.clientWidth
        })

        moveX = Math.ceil(testimonialScrollSection.scrollLeft)
        this.className == "next-btn" ? moveX += tesWidth : moveX -= tesWidth
        if(moveX < 0){
            moveX = 0
        }
        testimonialScrollSection.scrollLeft = moveX
        console.log(moveX)
        this.className == "next-btn" ? disableNextBtn(this) : disablePrevBtn(this)
    }

    function disableNextBtn(el){
        document.querySelector(".testimonial-btn-container .prev-btn").disabled = false
        tesCount = (testimonialScrollSection.scrollWidth - testimonialScrollSection.clientWidth)
        if(moveX >= tesCount){
            el.disabled = true
        }else{
            el.disabled = false
        }
    }

    function disablePrevBtn(el){
        document.querySelector(".testimonial-btn-container .next-btn").disabled = false
        if(moveX <= 15){
            el.disabled = true
        }else{
            el.disabled = false
        }
    }
}
    function handleAnim(elem){
        let options = {
            root : null,
            rootMargin : '0px',
            threshold : 0.7
            
        }

        function observerCallback(entries, observer){
            entries.forEach(entry => {
                if(entry.isIntersecting){
                    console.log(entry.target + "is seen")
                    entry.target.classList.add("addAnim")
                }
            })
        }

        let observer = new IntersectionObserver(observerCallback, options)
        elem.forEach(el => {
            observer.observe(el)

        })
    }

    handleAnim(testimonial)
    handleAnim(serviceBox)
    handleAnim(productBoxes)

// if(tabLine.style.left == tabLinks[0].offsetLeft){
// }

window.addEventListener("scroll", () => {
    if(scrollY > 0){
        document.querySelector("nav").classList.add("active")
    
    }else{
        document.querySelector("nav").classList.remove("active")
    }
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


// for(let [index, link] of tabLinks.entries()){
//     console.log(index, link)
// }

/**
 * if(this.dataset.category == "all"){
 *      categories.forEach(el => el.classList.remove("close"))
 * }else{
 *    categories.forEach(el => el.classList.add("close"))
 *     document.querySelector(`#${this.dataset.category}`).classList.remove("close")
 * }
 */

/**
 * (index/items.length) * 100%
 */

// carouselItems.forEach(el => {
//     console.log(el.childNodes)
// })


// carouselContainer.addEventListener("mousemove", (e)=>{
//     // console.log(e.target.closest(".carousel .btn"))
//     // clearInterval(intervalId)
//     // autoSlide()
//     // if(e.target.closest(".carousel > btn")){
//     //     console.log("hi there")
//     // }
//     console.log("hi")
// })

// carouselContainer.addEventListener("mousemove", (e) => {
//     //  autoSlide()
//     console.log(e.target.className == "btn")
// })