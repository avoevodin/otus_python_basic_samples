function deleteItem() {
    const xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            const data = JSON.parse(xhttp.responseText)
            console.log('received data:', data)
            window.location.href = data.url || "/"
        }
    }
    console.log(window.location)
    console.log(xhttp.onreadystatechange)
    xhttp.open("DELETE", window.location, true)
    xhttp.send()
}

window.onload = () => {
    const buttonDelete = document.getElementById('delete-product')
    buttonDelete.addEventListener('click', () => {
        if (confirm('Delete item?')) {
            deleteItem()
        } else {
            console.log("Wasn't deleted.")
        }
    })
}