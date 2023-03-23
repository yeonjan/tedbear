import Card from 'components/video/Card';
import React, { useEffect, useState } from 'react';
import styled from 'styled-components';

interface card {
  title: string;
  id: string;
}

const Wrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  border: 3px solid red;
  gap: 2%;
  background-color: ${props => props.theme.bgColor};
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
