import Carousel from 'components/common/Carousel';
import styled from 'styled-components';

const Main = styled.div`
  display: flex;
  justify-content: center;
`;

const HomePage = () => {
  const data: Array<{ url: string }> = [
    {
      url: 'https://img.youtube.com/vi/6Af6b_wyiwI/0.jpg',
    },
    {
      url: 'https://img.youtube.com/vi/RLESBHduKBs/0.jpg',
    },
    {
      url: 'https://img.youtube.com/vi/wL8X31XWZW8/0.jpg',
    },
    {
      url: 'https://img.youtube.com/vi/BEBKC7Hqfr0/0.jpg',
    },
    {
      url: 'https://img.youtube.com/vi/LDVyOnf0t9M/0.jpg',
    },
    {
      url: 'https://img.youtube.com/vi/JH_Pa1hOEVc/0.jpg',
    },
    {
      url: 'https://img.youtube.com/vi/9XGm_uHit5g/0.jpg',
    },
  ];
  return (
    <Main>
      <div>
        <h1>Your Recommended Videos</h1>
        <Carousel data={data}></Carousel>
      </div>
    </Main>
  );
};

export default HomePage;
