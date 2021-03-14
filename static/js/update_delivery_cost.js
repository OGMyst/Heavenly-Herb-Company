/* A list of all european country codes excluding Kosovo because it doesn't appear in django countries list
   and UK since that has a different delivery cost*/
let europeanCountryCodes = [
 'AL', 'AD', 'AM', 'AT', 'AZ', 'BY', 'BE', 'BA', 'BG', 'HR', 'CY', 'CZ', 
 'DK', 'EE', 'FI', 'FR', 'GE', 'DE', 'GR', 'HU', 'IS', 'IE', 'IT', 'KZ', 
 'LV', 'LI', 'LT', 'LU', 'MK', 'MT', 'MD', 'MC', 'ME', 'NL', 'NO', 'PL', 
 'PT', 'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SE', 'CH', 'TR', 'UA', 
 'VA', 
]
const STANDARD_DELIVERY_COST_UK = 4
const STANDARD_DELIVERY_COST_EU = 9.95
const STANDARD_DELIVERY_COST_WORLD = 25
const FREE_DELIVERY_THRESHOLD_UK = 40
const FREE_DELIVERY_THRESHOLD_EU = 50
const FREE_DELIVERY_THRESHOLD_WORLD = 80

let countrySelect = document.getElementById('id_country');
let deliveryLabel = document.getElementById('delivery_label');
let deliveryCostTag = document.getElementById('delivery_cost');
let orderTotalString = document.getElementById('order-total');
let orderTotal = parseFloat(orderTotalString.innerHTML.replace("£", ""));
let grandTotalString = document.getElementById('grand-total');

// Changes displayed delivery cost on checkoutpage
countrySelect.addEventListener('change', function () {

    let countrySelectValue = countrySelect.value
    let isInEurope = Boolean(europeanCountryCodes.find((europeanCountryCode) => europeanCountryCode === countrySelectValue));
    

    if (countrySelectValue === 'GB'){
        deliveryRegionCost = 4;
        deliveryRegionName = 'Standard UK Delivery';
        deliveryThreshold = FREE_DELIVERY_THRESHOLD_UK;

    }else if (isInEurope == true){
        deliveryRegionCost = 9.95;
        deliveryRegionName = 'EU Delivery';
        deliveryThreshold = FREE_DELIVERY_THRESHOLD_EU;
    
    } else {
        deliveryRegionCost = 25;
        deliveryRegionName = 'Global Delivery';
        deliveryThreshold = FREE_DELIVERY_THRESHOLD_WORLD;
    }

    if (orderTotal < deliveryThreshold){
        grandTotalString.innerHTML = "£" + (orderTotal + deliveryRegionCost).toFixed(2);
        deliveryCostTag.innerHTML = '£' + deliveryRegionCost.toFixed(2);
        deliveryLabel.innerHTML = deliveryRegionName;

    }


    deliveryCostTag.classList.add('change-text-color')
    setTimeout(removeChangeTextColor, 1000)

});

// callback function to remove color changing class
function removeChangeTextColor(){
   deliveryCostTag.classList.remove('change-text-color')
}
