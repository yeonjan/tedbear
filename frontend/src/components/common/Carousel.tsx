import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import ArrowBackIosNewIcon from '@mui/icons-material/ArrowBackIosNew';

interface Props {
  url: string;
  id: string;
}

const Wrapper = styled.div`
  overflow: hidden;
  position: relative;
  width: 80vw;
`;

const ContentBox = styled.div<{ transition: string; transform: number }>`
  display: flex;
  transition: ${props => props.transition};
  transform: translateX(-${props => props.transform}%);
  > * {
    width: 31%;
    margin-left: 2%;
    flex-shrink: 0;
    flex-grow: 1;
    border-radius: 10%;
  }
`;

const TitleWithButton = styled.div`
  display: flex;
  justify-content: space-between;
  border: 1px solid black;
  h1 {
    font-size: 4vh;
  }
  .buttom-wrapper {
    width: 100px;
    display: flex;
  }
`;

const LeftButton = styled.button`
  /* position: absolute; */
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: #7b7b7b;
  border: 1px solid black;
`;

const RightButton = styled.button`
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: #7b7b7b;
  border: 1px solid black;
`;

const Carousel = ({ data }: { data: Props[] }) => {
  data = [data[4], data[5], data[6], ...data, data[0], data[1], data[2]];
  const navigate = useNavigate();
  const transition = 'all 0.3s ease-out;';
  const [currentIndex, setCurrentIndex] = useState(3);
  const [length, setLength] = useState(data.length);
  const [transStyle, setTransStyle] = useState(transition);

  const handleClick = (e: React.MouseEventHandler<HTMLDivElement>): void => {
    navigate('/learning', { state: e });
  };

  // useEffect(() => {
  //   console.log('렌더링');
  //   setLength(data.length);
  // }, [data]); >> data가 바뀌지 않는다면 없어도 됨

  const next = () => {
    if (currentIndex < length - 3) {
      setCurrentIndex(prevState => prevState + 1);
    }
    if (currentIndex + 1 === length - 3) {
      setTimeout(() => {
        setCurrentIndex(3);
        setTransStyle('');
      }, 250);
    }
    setTransStyle(transition);
  };

  const prev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(prevState => prevState - 1);
    }
    if (currentIndex - 1 === 0) {
      setTimeout(() => {
        setCurrentIndex(7);
        setTransStyle('');
      }, 250);
    }
    setTransStyle(transition);
  };

  return (
    <Wrapper>
      <TitleWithButton>
        <h1>Recommended Videos</h1>
        <div className="buttom-wrapper">
          <LeftButton onClick={prev}>
            <ArrowBackIosNewIcon />
          </LeftButton>
          <RightButton onClick={next} className="right-arrow">
            <ArrowForwardIosIcon />
          </RightButton>
        </div>
      </TitleWithButton>
      <ContentBox transition={transStyle} transform={currentIndex * 33}>
        {data.map((Thumnail, idx) => {
          return <img key={idx} src={Thumnail.url} alt="" />;
        })}
      </ContentBox>
    </Wrapper>
  );
};

export default Carousel;
