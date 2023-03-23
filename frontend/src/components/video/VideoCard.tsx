import React from 'react';
import styled from 'styled-components';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

interface card {
  title: string;
  id: string;
}

const Wrapper = styled.div`
  > img {
    width: 22vw;
    @media (max-width: 1200px) {
      width: 30vw;
    }

    @media (max-width: 900px) {
      width: 40vw;
    }
    @media (max-width: 600px) {
      width: 80vw;
    }
  }
`;

// box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
// transition: 0.4s;
// &:hover {
//   scale: 1.04;
//   box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.2);
//   transition: 0.4s;

const VideoCard = ({ card }: { card: card }) => {
  return (
    // <Wrapper>
    //   <img
    //     src={'https://i.ytimg.com/vi/' + card.id + '/maxresdefault.jpg'}
    //     alt=""
    //   />
    // </Wrapper>
    <Card sx={{ maxWidth: 345 }}>
      <CardActionArea>
        <CardMedia
          component="img"
          image={'https://i.ytimg.com/vi/' + card.id + '/maxresdefault.jpg'}
          alt=""
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Lizard 안녕하세요 ㅋㅋㅋㅋ
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
};

export default VideoCard;
