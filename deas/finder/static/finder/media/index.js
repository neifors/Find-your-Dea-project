
window.navigator.geolocation.getCurrentPosition((position) =>{
    
    lat = position.coords.latitude
    long = position.coords.longitude
    console.log(lat)

    const inputLat = document.querySelector("#lat")
    const inputLong = document.querySelector("#long")

    inputLat.value = lat
    inputLong.value = long
})