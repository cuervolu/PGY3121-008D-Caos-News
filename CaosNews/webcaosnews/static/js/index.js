const API_URL1 = 'https://api.gael.cloud/general/public/monedas/USD';
const API_URL2 = 'https://api.gael.cloud/general/public/monedas/UF';

fetch(API_URL1).then(function (response) {
    return response.json();
}).then(function (monedas) {
    document.getElementById("DolarO").innerHTML = 'El valor actual del Dólar es $' + monedas.Valor;
}).catch(function (error) {
    console.log('Requestfailed', error);
});

fetch(API_URL2).then(function (response) {
    return response.json();
}).then(function (monedas) {
    document.getElementById("UTF").innerHTML = 'El valor actual del UF es $' + monedas.Valor;
}).catch(function (error) {
    console.log('Requestfailed', error);
});


