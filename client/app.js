// 1. Get Selected BHK Value
function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
        if(uiBHK[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid
}

// 2. Get Selected Bathrooms Value
function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
        if(uiBathrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid
}

// 3. Predict Button Click Function
function onEstimatePriceClicked() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    // Flask Backend Endpoint URL
    //var url = "http://127.0.0.1:5000/predict_home_price"; 
    var url="https://bengaluru-house-price-prediction-1-wyvd.onrender.com/predict_home_price"

    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    }, function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
}

// 4. Page Load hote hi Locations load karna
function onPageLoad() {
    console.log("document loaded");
    //var url = "http://127.0.0.1:5000/get_location_names"; 
    var url= "https://bengaluru-house-price-prediction-1-wyvd.onrender.com/get_location_names"
    
    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            $('#uiLocations').append(new Option("Choose a Location", "", true, true));
            // Setting it disabled
            $("#uiLocations option:first").attr('disabled', true);
            
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;