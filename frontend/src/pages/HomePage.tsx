import Carousel from 'components/common/Carousel';
import ShortsCarousel from 'components/common/ShortsCarousel';
import styled from 'styled-components';

interface Props {
  url: string;
  id: string;
}

const HomePage = () => {
  const data: Props[] = [
    {
      url: 'https://i.ytimg.com/vi/7tSP1M052Sg/maxresdefault.jpg',
      id: '6Af6b_wyiwI',
    },
    {
      url: 'https://i.ytimg.com/vi/tB5J9qgM2zI/maxresdefault.jpg',
      id: 'RLESBHduKBs',
    },
    {
      url: 'https://i.ytimg.com/vi/oITW0XsZd3o/maxresdefault.jpg',
      id: 'wL8X31XWZW8',
    },
    {
      url: 'https://i.ytimg.com/vi/YY6LCOJbve8/maxresdefault.jpg',
      id: 'BEBKC7Hqfr0',
    },
    {
      url: 'https://i.ytimg.com/vi/-k0p-DYYZKU/maxresdefault.jpg',
      id: 'LDVyOnf0t9M',
    },
    {
      url: 'https://i.ytimg.com/vi/IStsehNAOL8/maxresdefault.jpg',
      id: 'JH_Pa1hOEVc',
    },
    {
      url: 'https://i.ytimg.com/vi/UGdLvGbpehQ/maxresdefault.jpg',
      id: '9XGm_uHit5g',
    },
  ];
  return (
    <div>
      <Carousel data={data}></Carousel>
      <ShortsCarousel data={data}></ShortsCarousel>
    </div>
  );
};

export default HomePage;
