/* A list of all european country codes excluding Kosovo because it doesn't appear in django countries list
   and UK since that has a different delivery cost*/
let europeanCountryCodes = [
 'AL', 'AD', 'AM', 'AT', 'AZ', 'BY', 'BE', 'BA', 'BG', 'HR', 'CY', 'CZ', 
 'DK', 'EE', 'FI', 'FR', 'GE', 'DE', 'GR', 'HU', 'IS', 'IE', 'IT', 'KZ', 
 'LV', 'LI', 'LT', 'LU', 'MK', 'MT', 'MD', 'MC', 'ME', 'NL', 'NO', 'PL', 
 'PT', 'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SE', 'CH', 'TR', 'UA', 
 'VA', 
]

var countrySelect = document.getElementById('id_country');
let deliveryCostTag = document.getElementById('delivery_cost')

// Changes displayed delivery cost on checkoutpage
countrySelect.addEventListener('change', function () {

    let countrySelectValue = countrySelect.value
    let isInEurope = Boolean(europeanCountryCodes.find((europeanCountryCode) => europeanCountryCode === countrySelectValue));

    if (countrySelectValue === 'GB'){
        document.getElementById('delivery_label').innerHTML = 'Standard UK Delivery'
    }else if (isInEurope == true){
        deliveryCostTag.innerHTML = '£' + parseFloat(9.95)
        document.getElementById('delivery_label').innerHTML = 'EU Delivery'
    
    } else {
        deliveryCostTag.innerHTML = '£' + parseFloat(25) + '.00'
        document.getElementById('delivery_label').innerHTML = 'Global Delivery'
    }

    deliveryCostTag.classList.add('change-text-color')
    setTimeout(removeChangeTextColor, 1000)

});

// callback function to remove color changing class
function removeChangeTextColor(){
   deliveryCostTag.classList.remove('change-text-color')
}
