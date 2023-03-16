import PuzzleCover from 'components/puzzle/PuzzleCover';
import puzzle from 'assets/img/puzzle.svg';
import styled from 'styled-components';
// import { Button, Box } from '@mui/material';
// import Typography from '@mui/material/Typography';

//style
const Puzzle = styled.div`
  display: flex;
  .puzzle-board {
    background: ${props => props.theme.mainLightColor};
    width: 50%;
    height: 100vh;
  }
  .start-button {
    background: ${props => props.theme.pointLightColor};
  }
`;

const ImgBox = styled.div`
  background-image: url(${puzzle});
  width: 50%;
`;

//onClick
const handleStart = () => {
  console.log('시작 버튼을 클릭');
};

//function
const GamePage = () => {
  return (
    <Puzzle>
      <ImgBox></ImgBox>
      <div className="puzzle-board"></div>
    </Puzzle>
  );
};

export default GamePage;

{
  /* <Box className="puzzle-board" sx={{ display: 'flex', width: '50%' }}>
<Box
  sx={{
    width: '50%',
  }}
>
  <PuzzleCover></PuzzleCover>
</Box>
<Box
  textAlign="center"
  sx={{ margin: '180px', width: '50%', maxWidth: 500 }}
>
  <Typography
    // display="inline"
    align="center"
    color="white"
    fontSize={'100px'}
    // gutterBottom
  >
    PUZZLE
  </Typography>
  <Typography
    // display="inline"
    align="center"
    color="white"
    fontSize={'35px'}
    gutterBottom
  >
    문장의 빈칸을 채워 곰돌이 퍼즐을 완성해요!
  </Typography>
  <Button
    className="start-button"
    variant="contained"
    size="large"
    onClick={handleStart}
    style={{
      margin: '30px',
      width: '13em',
      height: '6em',
    }}
  >
    <Typography color="white" variant="h3" gutterBottom>
      START
    </Typography>
  </Button>
</Box>
</Box> */
}
