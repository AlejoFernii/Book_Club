// Book Form

function showBookForm(e){
    let formMain = document.createElement('div')

    let formGroup1 = document.createElement('div')


    let labelTitle = document.createElement('label')
        labelTitle.setAttribute('for','title')
        labelTitle.innerHTML = "Book Title:"

    let inputTitle = document.createElement('input')
        inputTitle.setAttribute('type','text')
        inputTitle.setAttribute('name','title')

    formGroup1.append(labelTitle,inputTitle)

    let formGroup2 = document.createElement('div')

    let labelDescription = document.createElement('label')
        labelDescription.setAttribute('for','description')
        labelDescription.innerHTML = "Description:"

    let inputDescription = document.createElement('textarea')
        inputDescription.setAttribute('cols','20')
        inputDescription.setAttribute('rows','4')
        inputDescription.setAttribute('name','description')

    formGroup2.append(labelDescription, inputDescription)

    let sub = document.createElement('input')
        sub.setAttribute('type','submit')
        sub.setAttribute('form','book-form')
        sub.setAttribute('value','Add Book')
        sub.setAttribute('class','btn btn-lg btn-dark btn-outline-success')

    formMain.append(formGroup1, formGroup2, sub)

    e.replaceWith(formMain);

}