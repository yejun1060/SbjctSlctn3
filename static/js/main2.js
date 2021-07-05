




function checkOnlyOne2(element) {

  const checkboxes
      = document.getElementsByName("H[]");

  checkboxes.forEach((cb) => {
    cb.checked = false;
  })

  element.checked = true;
}

function checkOnlyOne3(element) {

  const checkboxes
      = document.getElementsByName("C[]");

  checkboxes.forEach((cb) => {
    cb.checked = false;
  })

  element.checked = true;
}

function checkOnlyOne5(element) {

  const checkboxes
      = document.getElementsByName("D[]");

  checkboxes.forEach((cb) => {
    cb.checked = false;
  })

  element.checked = true;
}


