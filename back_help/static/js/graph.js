const renderChart = (data,labels)=>{
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: labels,
        datasets: [
            {
            label: 'Chamados em Andamento',
            data: data,
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 99, 132, 0.2)',                
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'      
              
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',                
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
                       
          
            ],
            borderWidth: 2
        }]
    },
    options: {
    legend:{
        display:true,        
        text:'Status dos Chamados',
        position: 'bottom',
    }
    },
});

};
const getChartData = () =>{
    console.log("fetching");
    fetch('/dash_index_status')
    .then((res) => res.json())
    .then((results) => {
        console.log("results", results);
        const status_data = results.chamado_status_data;
        const [labels,data] = [
            Object.keys(status_data),
            Object.values(status_data),
        ];

        renderChart(data,labels);
    });
};


function start() {
    getChartData();
   
};
window.onload = start;