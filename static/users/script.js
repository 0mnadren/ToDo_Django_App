// Hidden and Visible
const editButton = document.querySelector('#edit-profile');
const closeEdit = document.querySelector('#close-edit');

editButton.addEventListener('click', () => {
    document.getElementById('edit-profile').style.display = 'none';
    document.getElementById('close-edit').style.display = 'block';
    document.getElementById('profile-info-div').style.display = 'block';
})

closeEdit.addEventListener('click', () => {
    document.getElementById('edit-profile').style.display = 'block';
    document.getElementById('close-edit').style.display = 'none';
    document.getElementById('profile-info-div').style.display = 'none';
})




// Checkboxes and LocalStorage
const checkBoxes = document.querySelectorAll('input[type=checkbox]');
for (let i=0; i < checkBoxes.length; i ++) {
    checkBoxes[i].addEventListener('click', () => {
    const checkBoxes = document.querySelectorAll('input[type=checkbox]');
    let checkedIds = [];
    for (let checkbox of checkBoxes) {
        if (checkbox.checked == true) {
            let id = checkbox.id;
            checkedIds.push(id);
        }
    }
    saveCheckBoxes(checkedIds)
    })
}

// Load Data from Local Storage
window.addEventListener('DOMContentLoaded', function () {
    if (localStorage.getItem('checkedBoxes') != null) {
        checkedBoxesArray = JSON.parse(localStorage.getItem('checkedBoxes'));

        let checkedBoxesUnpack = checkedBoxesArray[0]['checked'];

        for (let i=0; i < checkedBoxesUnpack.length; i++) {
            document.getElementById(checkedBoxesUnpack[i]).checked = true;
        }
    }      
});

// Save data to Local Storage
function saveCheckBoxes(checkedIds) {
    checkedBoxesArray = [
        {
            checked: checkedIds
        }
    ]
    window.localStorage.setItem('checkedBoxes', JSON.stringify(checkedBoxesArray));
}
