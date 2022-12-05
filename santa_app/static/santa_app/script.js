window.onload = function(){
    main();
};

window.end_cycle = false;

function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
  }
  

async function remove_present(id){

    try{
    await delay(3500);
    document.getElementById(id).remove();
    }catch{

    }

}



async function main(){

    on_mobile = false;
    if(window.innerWidth / window.innerHeight <= 1){
        on_mobile = true;
    }
    console.log(on_mobile)
count = 0;
element = document.getElementById("presentholder")

while(!window.end_cycle){
    count += 1
    present = document.createElement("img");
    present.src = "/static/santa_app/imgs/present.png";
    present.classList.add("present");
    present.classList.add("present_wobble");
    present.style.height = "auto";
    if(on_mobile){
        present.style.width = String(Math.random() * 15 + 20) + "vw";
    }else{
        present.style.width = String(Math.random() * 5 + 5) + "vw";
    }
    present.onclick = function(){
        present_clicked(this);
    }
    element.appendChild(present);
    present.id = count;
    
    remove_present(count);

    // if(window.end_cycle){
    //     break;
    // }

    await delay(Math.random() * 400 + 300);


}


}


async function present_clicked(el){
    holder = document.getElementById("presentholder");
    all_presents = document.getElementsByClassName("present");

    presents_size = [];
    presents_location = [];

    for(i=0;i<all_presents.length;i++){
        present = all_presents[i]
        width_px = present.offsetWidth;
        width_wv = width_px * 100 / window.innerWidth;
        presents_size.push(width_wv);

        left = parseFloat(window.getComputedStyle(present,null).getPropertyValue("left")) * 100 / window.innerWidth;
        transform = parseFloat(window.getComputedStyle(present,null).getPropertyValue("transform").split(",").slice(-1)[0].slice(1, -1));
        presents_location.push([left, transform]);

    }

    first_present_id = holder.firstChild.id;

    holder.innerHTML = "";


    for(i=0;i<presents_size.length;i++){

        size = presents_size[i];
        loc = presents_location[i];


        present = document.createElement("img");
        present.src = "/static/santa_app/imgs/present.png";
        present.style.width = String(size) + "vw";
        present.style.height = "auto";
        present.style.position = "absolute";
        present.style.left = String(loc[0]) + "vw";
        present.style.transform = "translateY(" + String(loc[1]) + "%)";
        present.id = "clicked_" + (parseInt(first_present_id) + i);

        holder.appendChild(present);
    }

    clicked_present = document.getElementById("clicked_" + el.id);

    clicked_present.style.transform = clicked_present.style.transform + " scale(150%)";
    clicked_present.style.animation = "flyOut";

    paper = document.getElementById("paper");
    paperholder = document.getElementById("backdrop");
    paperholder.style.display = "block";
    paperholder.style.backdropFilter = "blur(3px) brightness(50%)";
    paperholder.style.zIndex = "2";


    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            giftee = xhttp.responseText;
            document.getElementById("giftee").innerHTML = giftee;
        }
    };
    xhttp.open("GET", "/get_giftee", true);
    xhttp.send();


    window.end_cycle = true;
}