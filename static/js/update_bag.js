// Update quantity on click
function changeQuantity(formId){
    var form = document.getElementById(formId);
    form.submit();
}

// Remove item and reload on click
function removeItem(itemId, csrfToken){
    var url = `/bag/remove/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
    .done(function() {
        location.reload();
    });
}