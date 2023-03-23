import React from 'react';
import styled from 'styled-components';

interface card {
  title: string;
  id: string;
}

const Wrapper = styled.div`
  width: 250px;
  height: 280px;
  background-color: white;
  margin: 5px;
  float: left;
  @media (max-width: 615px) {
    width: 300px;
  }
  > img {
    width: 250px;
    height: 200px;
    @media (max-width: 615px) {
      width: 400px;
    }
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
      <img
        src={'https://i.ytimg.com/vi/' + card.id + '/maxresdefault.jpg'}
        alt=""
      />
    </Wrapper>
  );
};

export default Card;
