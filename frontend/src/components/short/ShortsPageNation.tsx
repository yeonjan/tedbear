import React, { useState } from 'react';
import styled from 'styled-components';
import { Shorts } from 'utils/api/recommApi';
import VideoLevel from 'assets/img/videoLevel.svg';

const Containter = styled.div`
    width: 100%;
    display: flex;
    .wrapper {
        width: 20%;
        position: relative;
        border-radius: 16px;
        margin-left: 1%;
        margin-right: 1%;
        cursor: pointer;
        
    .main-img {
      border-radius: 16px;
      width: 100%;
      height: 100%;
      cursor: pointer;
      
    }
    .video-level {
      height: 15%;
      width: 15%;
      position: absolute;
      top: 4%;
      left: 4%;
    }
`;

interface Props {
  data: Shorts[];
  requestShorts: (arg0: number) => void;
  nextPage: number;
}

const ShortsPageNation = ({ data, requestShorts, nextPage }: Props) => {
  const [page, setPage] = useState<number>(0);
  console.log(page);

  const handlerRight = () => {
    const nextPage = page + 1;
    setPage(prev => prev + 1);
    requestShorts(nextPage);
  };

  const handlerLeft = () => {
    const nextPage = page - 1;
    setPage(prev => prev - 1);
  };

  return (
    <Containter>
      {data.map((Thumnail, idx) => {
        return (
          <div className="wrapper" key={idx}>
            <img
              className="main-img"
              src={'https://i.ytimg.com/vi/' + Thumnail.watchId + '/hq1.jpg'}
              alt=""
              /* onClick={() => {
                    setOpenModal(true);
                    setShortsId(Thumnail);
                  }} */
            ></img>
            <img
              src={VideoLevel}
              className="video-level"
              style={{
                filter:
                  'invert(45%) sepia(78%) saturate(1707%) hue-rotate(161deg) brightness(93%) contrast(103%)',
              }}
            ></img>
          </div>
        );
      })}
      {page - 1 >= 0 && <button>왼쪽</button>}
      {nextPage >= page + 1 && <button onClick={handlerRight}>오른쪽</button>}
    </Containter>
  );
};

export default ShortsPageNation;
