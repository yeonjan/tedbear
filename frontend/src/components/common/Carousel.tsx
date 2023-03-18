import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';

interface Props {
  data: any;
}

interface Thumnail {
  url: string;
  id: number;
}

const Wrapper = styled.div`
  overflow: hidden;
  position: relative;
  .left-arrow,
  .right-arrow {
    width: 48px;
    height: 48px;
    border-radius: 24px;
    background-color: yellow;
    border: 1px solid black;
  }

  .left-arrow {
    left: 24px;
    background-color: yellow;
  }

  .right-arrow {
    right: 24px;
    background-color: yellow;
  }
`;

const ContentBox = styled.div`
  display: flex;
  transition: all 0.3s ease-out;
  > * {
    width: 32.3%;
    flex-shrink: 0;
    flex-grow: 1;
    border-radius: 5%;
    margin-left: 1%;
  }
`;

const Carousel = ({ data }: Props) => {
  const navigate = useNavigate();
  const [currentIndex, setCurrentIndex] = useState(0);
  const [length, setLength] = useState(data.length);

  const handleClick = (e: React.MouseEventHandler<HTMLDivElement>): void => {
    navigate('/learning', { state: e });
  };

  useEffect(() => {
    console.log('렌더링');
    setLength(data.length);
  }, [data]);

  const next = () => {
    if (currentIndex < length - 3) {
      setCurrentIndex(prevState => prevState + 1);
    }
  };

  const prev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(prevState => prevState - 1);
    }
  };

  return (
    <Wrapper>
      {currentIndex > 0 && (
        <button onClick={prev} className="left-arrow">
          Left
        </button>
      )}
      <ContentBox style={{ transform: `translateX(-${currentIndex * 33.3}%)` }}>
        {data.map((Thumnail: Thumnail, idx: number) => {
          return <img key={idx} src={Thumnail.url} alt="" />;
        })}
      </ContentBox>
      {currentIndex < length - 3 && (
        <button onClick={next} className="right-arrow">
          Right
        </button>
      )}
    </Wrapper>
  );
};

export default Carousel;
