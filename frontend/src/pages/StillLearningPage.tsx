import Card from 'components/video/Card';
import React, { useEffect, useState } from 'react';
import styled from 'styled-components';

interface card {
  title: string;
  id: string;
}

const Wrapper = styled.div`
  width: 90%;
  max-width: 1200px;
  min-width: 370px;
  background-color: ${props => props.theme.bgColor};
  @media (min-width: 1280px) {
    width: 1040px;
    height: 580px;
  }

  @media (max-width: 1279px) {
    width: 780px;
    height: 870px;
  }

  @media (max-width: 900px) {
    width: 520px;
    height: 1160px;
  }

  @media (max-width: 600px) {
    width: 300px;
    height: 2320px;
  }
`;

const StillLearningPage = () => {
  const [video, setVideo] = useState<card[]>([]);
  useEffect(() => {
    setVideo([
      {
        title:
          'How to Calm Your Anxiety, From a Neuroscientist | The Way We Work, a TED series',
        id: '6Af6b_wyiwI',
      },
      {
        title: 'The skill of self confidence | Dr. Ivan Joseph | TEDxRyersonU',
        id: 'RLESBHduKBs',
      },
      {
        title: 'The skill of self confidence | Dr. Ivan Joseph | TEDxRyersonU',
        id: 'wL8X31XWZW8',
      },
      {
        title:
          'How to motivate yourself to change your behavior | Tali Sharot | TEDxCambridge',
        id: 'BEBKC7Hqfr0',
      },
      {
        title:
          'How to motivate yourself to change your behavior | Tali Sharot | TEDxCambridge',
        id: 'LDVyOnf0t9M',
      },
      {
        title:
          'How to motivate yourself to change your behavior | Tali Sharot | TEDxCambridge',
        id: 'JH_Pa1hOEVc',
      },
      {
        title:
          'How to motivate yourself to change your behavior | Tali Sharot | TEDxCambridge',
        id: '9XGm_uHit5g',
      },
    ]);
  }, []);

  return (
    <Wrapper>
      {video.map((card, idx) => {
        return <Card card={card} key={idx}></Card>;
      })}
    </Wrapper>
  );
};

export default StillLearningPage;
