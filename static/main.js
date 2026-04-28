function addBook() {
    let addAuthor = document.getElementById('add_author').value
    let addName = document.getElementById('add_name').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'author': addAuthor || 'Unknown', 
                            'name': addName ||'Unknown'})
        }
    ) 
}


function deleteBook(el) {
    id = el.value
    fetch('/delete/' + id, {
        method: 'delete',
        headers: {'Content-Type': 'application/json'}
        }
    )
}

