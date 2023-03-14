import PuzzleCover from 'components/puzzle/PuzzleCover';
import styled from 'styled-components';
import { Button, Box } from '@mui/material';
import Typography from '@mui/material/Typography';

//style
const Puzzle = styled.div`
  .puzzle-board {
    background: ${props => props.theme.mainLightColor};
  }
  .start-button {
    background: ${props => props.theme.pointLightColor};
  }
`;

//onClick
const handleStart = () => {
  console.log('시작 버튼을 클릭');
};

//function
const PuzzlePage = () => {
  return (
    <Puzzle>
      <div className="puzzle-board">
        {/* 큰 박스 속 작은 박스 두개  */}
        <Box sx={{ display: 'flex', width: '100%' }}>
          <Box
            sx={{
              width: '50%',
            }}
          >
            <PuzzleCover></PuzzleCover>
          </Box>
          <Box sx={{ width: '50%', maxWidth: 500 }}>
            <Typography color="white" variant="h1" gutterBottom>
              PUZZLE
            </Typography>
            <Typography color="white" variant="h2" gutterBottom>
              문장의 빈칸을 채워 곰돌이 퍼즐을 완성하세요!
            </Typography>
            <Button
              className="start-button"
              variant="contained"
              size="large"
              onClick={handleStart}
              style={{
                width: '16em',
                height: '8em',
              }}
            >
              <Typography color="white" variant="h2" gutterBottom>
                START
              </Typography>
            </Button>
          </Box>
        </Box>
      </div>
    </Puzzle>
  );
};

export default PuzzlePage;
