

function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for(var i in uiBHK) {
    if(uiBHK[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate rent button clicked");
  var sqft       = document.getElementById("uiSqft");
  var bhk        = getBHKValue();
  var bathrooms  = getBathValue();
  var furnish = document.getElementById("uiFurnishing");
  var localities = document.getElementById("uiLocations");
  var Tenants    = document.getElementById("uiTenants");
  var estPrice   = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_rent_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_rent_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      area: parseFloat(sqft.value),
      bhk: bhk,
      bathrooms: bathrooms,
      furnish: furnish.value,
      Tenants: Tenants.value,
      localities: localities.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Rupees</h2>";
      console.log(status);
  });
}


function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
   // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url, function (data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var locations = data.localities;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_furnish_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_furnish_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url, function (data, status) {
        console.log("got response for get_furnish_names request");
        if (data) {
            var furnishs = data.furnish;
            var uiFurnishing = document.getElementById("uiFurnishing");
            $('uiFurnishing').empty();
            for (var i in furnishs) {
                var opt = new Option(furnishs[i]);
                $('#uiFurnishing').append(opt);
            }
        }
    });
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_tenants_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_tenants_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url, function (data, status) {
        console.log("got response for get_tenants_names request");
        if (data) {
            var tenants = data.Tenants;
            var uiTenants = document.getElementById("uiTenants");
            $('uiTenants').empty();
            for (var i in tenants) {
                var opt = new Option(tenants[i]);
                $('#uiTenants').append(opt);
            }
        }
    });

}          


window.onload = onPageLoad;