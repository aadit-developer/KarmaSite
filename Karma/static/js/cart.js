updatecart=document.getElementsByClassName('update-cart')

for(var i =0;i<updatecart.length;i++){
    updatecart[i].addEventListener('click',function(){
        var productId=this.dataset.product
        var action=this.dataset.action
        console.log('productId:',productId,'action:',action)
        updateUserOrder(productId,action)
    })
}

function updateUserOrder(productId,action){
    var url='/update_order/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId , 'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data',data)
        location.reload()
    })
}
