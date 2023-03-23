import React from 'react';
import styled from 'styled-components';

interface card {
  title: string;
  id: string;
}

const Wrapper = styled.div`
  border: 3px black solid;
  display: flex;
  /* width: 24%; */
  > img {
    width: 20vw;
    /* margin-left: 2%;
    margin-right: 2%;
    margin-top: 2%;
    margin-bottom: 2%; */
    /* @media (max-width: 900px) {
      width: 27vw;
    }
    @media (max-width: 500px) {
      width: 30vw;
    }
    @media (max-width: 300px) {
      width: 40vw;
    }
    @media (max-width: 200px) {
      width: 100vw;
    } */
  }
`;

const Card = ({ card }: { card: card }) => {
  return (
    <Wrapper>
      <img src={'https://i.ytimg.com/vi/' + card.id + '/hq1.jpg'} alt="" />
    </Wrapper>
  );
};

export default Card;
