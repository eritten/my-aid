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
window.addEventListener("load", ()=>{

    //the about video functionality
  const video = document.querySelector("#dis-vid");
  const playBtn = document.querySelector("#vid-btn");


//   playBtn.addEventListener("click", () => {
//     const hasPlay = playBtn.classList.contains("play");
//     console.log(video)
//     if (hasPlay) {
//       playVid();
//     } else {
//       pauseVid();
//     }
//   });
  
//   function playVid() {
//     video.play();
//     playBtn.innerHTML = `<i class="fas fa-pause"></i>`;
//     playBtn.classList.remove("play");
//   }
//   function pauseVid() {
//     video.pause();
//     playBtn.innerHTML = `<i class="fas fa-play"></i>`;
//     playBtn.classList.add("play");
//   }
})