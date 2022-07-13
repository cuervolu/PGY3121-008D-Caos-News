const API_URL1 = 'https://api.gael.cloud/general/public/monedas/USD';
const API_URL2 = 'https://api.gael.cloud/general/public/monedas/UF';

fetch(API_URL1).then(function (response) {
    return response.json();
}).then(function (monedas) {
    moneda = (monedas.Valor).toLocaleString('es-CL', { minimumFractionDigits: 2, style: 'currency', currency: 'CLP' });
    document.getElementById("DolarO").innerHTML = 'El valor actual del Dólar es $' + moneda;
}).catch(function (error) {
    console.log('Requestfailed', error);
});

fetch(API_URL2).then(function (response) {
    return response.json();
}).then(function (monedas) {
    moneda = (monedas.Valor).toLocaleString('es-CL', { minimumFractionDigits: 2, style: 'currency', currency: 'CLP' });
    document.getElementById("UTF").innerHTML = 'El valor actual del UF es $' + moneda;
}).catch(function (error) {
    console.log('Requestfailed', error);
});


