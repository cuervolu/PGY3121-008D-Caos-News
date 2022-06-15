const API_URL1 = 'https://api.gael.cloud/general/public/monedas/USD';
const API_URL2 = 'https://api.gael.cloud/general/public/monedas/UF';

fetch(API_URL1).then(function (response) {
    return response.json();
}).then(function (monedas) {
    moneda = Math.round(parseInt(monedas.Valor))
    document.getElementById("DolarO").innerHTML = 'El valor actual del Dólar es $' + moneda;
}).catch(function (error) {
    console.log('Requestfailed', error);
});

fetch(API_URL2).then(function (response) {
    return response.json();
}).then(function (monedas) {
    moneda = Math.round(parseInt(monedas.Valor))
    document.getElementById("UTF").innerHTML = 'El valor actual del UF es $' + moneda;
}).catch(function (error) {
    console.log('Requestfailed', error);
});


