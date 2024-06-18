






let selcdgfh = document.querySelector('.selcdgfh')
let mavideopre = document.querySelector('.mavideopre')
let fermer = document.querySelector('#fermer')
let ouvrir = document.querySelector('#ouvrir')
let dhjkfkr = document.querySelector('#dhjkfkr')
selcdgfh.addEventListener('click',()=>{
    mavideopre.classList.add("active")
    fermer.classList.add("active")
    ouvrir.classList.add("active")

    
});
fermer.addEventListener('click',()=>{
    mavideopre.classList.remove("active")
    fermer.classList.remove("active")
    ouvrir.classList.remove("active")


    
});
dhjkfkr.addEventListener('click',()=>{
    mavideopre.classList.remove("active")
    fermer.classList.remove("active")
    ouvrir.classList.remove("active")


    
});
// cdghd.addEventListener('click',()=>{
//     menhoa.classList.remove("active")

    
// });

let logoMenu = document.querySelector('.logoMenu')
let menhoa = document.querySelector('.menhoa')
let cdghd = document.querySelector('#cdghd')

logoMenu.addEventListener('click',()=>{
    menhoa.classList.add("active")

    
});
cdghd.addEventListener('click',()=>{
    menhoa.classList.remove("active")

    
});



let accee = document.querySelector('.mebhhd11')
let aprop = document.querySelector('#aprop')
let pord = document.querySelector('#pord')
let cone = document.querySelector('#cone')

accee.addEventListener('click',()=>{
    accee.classList.add("active")

    cone.classList.remove("active")
    pord.classList.remove("active")
    aprop.classList.remove("active")

    
});



aprop.addEventListener('click',()=>{
    
    aprop.classList.add("active")

    cone.classList.remove("active")
    pord.classList.remove("active")
    accee.classList.remove("active")

    
});



pord.addEventListener('click',()=>{
    
    pord.classList.add("active")

    cone.classList.remove("active")
    aprop.classList.remove("active")
    accee.classList.remove("active")

    
});



cone.addEventListener('click',()=>{
    
    cone.classList.add("active")

    pord.classList.remove("active")
    aprop.classList.remove("active")
    accee.classList.remove("active")

    
})

