function show_paper(){
    paper = document.getElementById("paper");
    paperholder = document.getElementById("backdrop");
    paperholder.style.display = "block";
    paperholder.style.backdropFilter = "blur(3px) brightness(50%)";
    paperholder.style.zIndex = "2";
}