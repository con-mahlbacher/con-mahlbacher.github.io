const button = document.getElementById("clickButton")
const data = document.getElementById("info")

const cars = 2

   button.onclick= function(){

    fetch("http://127.0.0.1:5000/receiver",
    {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        },
        body:JSON.stringify(cars)}).then(res=>{
            if(res.ok){
                return res.json()
            } else {
                alert("Something is wrong.")
            }
        }).then(jsonResponse=>{
            data.innerHTML = jsonResponse
        }
        ).catch((err) => console.error(err));
    }
    