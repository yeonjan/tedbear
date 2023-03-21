import Chart from 'react-apexcharts';
import styled from 'styled-components';

const SemiStyle = styled.div`
  .exp-paper {
    width: 33vw;
    height: 40vh;
    background-color: white;
    border-radius: 20px;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
  }
  .exp-name {
    padding: 10px 0px 0px 230px;
  }
`;

const series = [76];
const options = {
  colors: ['#8F84CE'],
  chart: {
    type: 'radialBar',
    offsetY: -20,
    sparkline: {
      enabled: true,
    },
  },
  plotOptions: {
    radialBar: {
      startAngle: -90,
      endAngle: 90,
      track: {
        background: '#e7e7e7',
        strokeWidth: '97%',
        margin: 5, // margin is in pixels
        dropShadow: {
          enabled: true,
          top: 2,
          left: 0,
          color: '#999',
          opacity: 1,
          blur: 2,
        },
      },
      dataLabels: {
        name: {
          show: true,
          color: '#888',
        },
        value: {
          fontSize: '50px',
          offsetY: -50,
          color: '#6255A4',
        },
      },
    },
  },
  grid: {
    padding: {
      top: -10,
    },
  },
  fill: {
    type: 'gradient',
    gradient: {
      shade: 'light',
      shadeIntensity: 0.4,
      inverseColors: false,
      opacityFrom: 1,
      opacityTo: 1,
      stops: [0, 50, 53, 91],
    },
  },
  labels: ['Average Results'],
};

export default function SemiExp() {
  return (
    <SemiStyle>
      <div className="exp-paper">
        <h1 className="exp-name">Exp</h1>
        <Chart
          options={options}
          series={series}
          type="radialBar"
          height={500}
          width={500}
        />
      </div>
    </SemiStyle>
  );
}
