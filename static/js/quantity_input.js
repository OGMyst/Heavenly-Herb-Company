// Ensure proper enabling/disabling of all inputs on page load
$(document).ready(function(){
    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
    }
    handleEnableDisable(itemId)
});

// Disable +/- buttons outside 1-99 range
function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Increment quantity
    function incrementQty(buttonId){
        incrementButton = document.getElementById(buttonId);
       
        var closestInput = $(incrementButton).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1);
        var itemId = $(closestInput).data('item_id');
        handleEnableDisable(itemId);
    };

    // Decrement quantity
    function decrementQty(buttonId){
        decrementButton = document.getElementById(buttonId);
       
        var closestInput = $(decrementButton).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1);
        var itemId = $(closestInput).data('item_id');
        handleEnableDisable(itemId);
    };