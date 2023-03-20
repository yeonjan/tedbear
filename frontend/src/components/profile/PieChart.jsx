import Chart from 'react-apexcharts';

const series = [15, 5, 20, 5, 5, 10, 10, 10, 10, 10];

const options = {
  // chart type
  chart: {
    type: 'polarArea',
  },
  // label custom
  labels: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
  // color custom
  colors: [
    '#df3333',
    '#ff6600',
    '#ffff00',
    '#80ff00',
    '#00eaff',
    '#0011ff',
    '#f700ff',
    '#8e0089',
    '#482000',
    '#505050',
  ],
  // filling color opacity custom
  fill: {
    opacity: 0.8,
  },
  // responsive custom
  responsive: [
    {
      breakpoint: 480,
      options: {
        chart: {
          width: 200,
        },
        legend: {
          position: 'bottom',
        },
      },
    },
  ],
};

export default function PieChart() {
  return (
    <div>
      <Chart options={options} series={series} type="polarArea" height={300} />
    </div>
  );
}
