var node_list = document.querySelectorAll("img");
var btn_afficher = document.querySelector("#afficher");
var btn_inter_coupé = document.querySelector("#inter");
var btn_aléatoire = document.querySelector("#aléatoire");
var btn_réinitialiser = document.querySelector("#réinitialiser");
var index_list
function initial(){
    index_list = []
    for(var i = 0; i < node_list.length; i++){
        index_list.push(i);
    }
}
initial()
function cacher(){
    for(let i = 0; i < node_list.length; i++){
        node_list[i].src="dos.ico";
    }
}
btn_afficher.addEventListener('click' ,function(){
    for(let i = 0; i < node_list.length; i++){
        node_list[i].src="pic_cartes/"+index_list[i]+".jpg";
    }
})
btn_inter_coupé.addEventListener('click',function(){
    cacher();
    let nouvelle_index_list = [];
    let sub_index_list1 = index_list.slice(0, (index_list.length)/2); 
    let sub_index_list2 = index_list.slice((index_list.length)/2);
    for(let i = 0; i < node_list.length/2; i++){
    nouvelle_index_list.push(sub_index_list1[i]);
    nouvelle_index_list.push(sub_index_list2[i]);
    }
    index_list = nouvelle_index_list;   
})
btn_aléatoire.addEventListener('click',function(){
    cacher();
    let index_list_temp = index_list;
    let i = 0;
    var nouvelle_index_list = [];
    const longueur = index_list.length;
    while (i < longueur){
        let random_index = Math.floor(Math.random() * index_list_temp.length);
        nouvelle_index_list.push(index_list_temp[random_index]);
        index_list_temp.splice(random_index, 1);
        i++;
    }
    index_list = nouvelle_index_list;
})
btn_réinitialiser.addEventListener('click',function(){
    cacher()
    initial()
    })