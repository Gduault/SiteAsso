// recupere les élement de la classe modal
var modal = document.getElementById(modal);
// recupere les elements de la classe modalBtn
var modalBtn = document.getElementById(modalBtn);
// recupere les elements de la classe closeBtn
var closeBtn = document.getElementsByClassName('closeBtn')[0];

// utilisation de la methode listen pour ouvrir le modal
modalBtn.addEventListener('click', openModal);
// utilisation de la methode listen pour fermer le modal
closeBtn.addEventListener('click', closeModal);
// utilisation de la methode listen pour fermer le modal en dehors de celui ci
window.addEventListener('click', clickOutside)

// fonction pour ouvrir le modal
function openModal(){
    modal.style.display = 'block';
}

// fonction pour fermer le modal
function closeModal(){
    modal.style.display = 'none';
}

// fonction pour fermer le modal en dehors de celui ci
function clickOutside(e){
    if(e.target == modal){
        modal.style.display = 'block';}
}
