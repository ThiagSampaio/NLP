$('#termo_busca').on('submit', async (e) => {
    e.preventDefault();

    const termo = $("#term").val();
    const params = new URLSearchParams({termo});
    const resp = await fetch(`/termo?${params}`).then(r => r.json());

    const lista_positiva = resp['positiva'];
    const lista_negativa = resp['negativa'];
    const numero_pesquisas = resp['tracking_searchs']
    var termos = resp['tracking_number_each_search']

    const numPositivos = lista_positiva.length
    const numNegativos = lista_negativa.length
    const numTotal = numPositivos + numNegativos

    console.log(typeof termos)
    //console.log(lista_negativa[3])
    //document.getElementById('output_total_r').innerHTML = numTotal
    //document.getElementById('positivos_r').innerHTML = numPositivos
    //document.getElementById('negativos_r').innerHTML = numNegativos
    document.getElementById('tracking_total').innerHTML = numero_pesquisas

    document.getElementById("positiva_1").innerHTML = lista_positiva[0]
    document.getElementById("negativo_1").innerHTML = lista_negativa[0]
    document.getElementById("positiva_2").innerHTML = lista_positiva[1]
    document.getElementById("negativo_2").innerHTML = lista_negativa[1]
    document.getElementById("positiva_3").innerHTML = lista_positiva[2]
    document.getElementById("negativo_3").innerHTML = lista_negativa[2]
    document.getElementById("positiva_4").innerHTML = lista_positiva[3]
    document.getElementById("negativo_4").innerHTML = lista_negativa[3]
    document.getElementById("negativo_5").innerHTML = lista_negativa[4]
    //$('#resultado').text(data.numero_total);

    let ctx = document.getElementById('myChart').getContext('2d');
    let labels = ['Positvos ', 'Negativos '];
    let colorHex = ['#01937C', '#DA0037'];

    let myChart = new Chart(ctx, {
      type: 'pie',
      data: {
        datasets: [{
          data: [numPositivos, numNegativos],
          backgroundColor: colorHex
        }],
        labels: labels
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          position: 'top'
        },
        plugins: {
          datalabels: {
            color: '#fff',
            anchor: 'end',
            align: 'start',
            offset: -10,
            borderWidth: 2,
            borderColor: '#fff',
            borderRadius: 25,
            backgroundColor: (context) => {
              return context.dataset.backgroundColor;
            },
            font: {
              weight: 'bold',
              size: '400'
            },
            formatter: (value) => {
              return value + ' %';
            }
          }
        }
      }
    })

    // Grafico de barras
    var dps = [];
    for(var element in termos) {
    dps.push({x: element, y: termos[element]});
    }

    let ctxx = document.getElementById('myChart2').getContext('2d');
    let colorHexx = ['#01937C',"#3889FC", "#DB9C3F","#9D66CC"];
    labels_1 = [];

    for(var element in termos) {
    labels_1.push(element);
    }

    var myBarChart = new Chart(ctxx, {
        type: 'bar',
        data:{
            labels: labels_1,
            datasets: [{
             data:dps,
             backgroundColor: ["red", "blue", "green", "blue", "red", "blue", "green"],
            }],
        },
        options:{
            indexAxis: 'y',
            elements:{
                bar:{
                boderWidth:2,
                }
            },
            responsive: true,
        },

    })

});
