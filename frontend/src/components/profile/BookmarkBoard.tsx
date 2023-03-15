import { Stack, Paper, Button, Box } from '@mui/material';
import styled from 'styled-components';
import Typography from '@mui/material/Typography';

//style
const Bookmark = styled.div`
  .unclicked-button {
    background: ${props => props.theme.mainLightColor};
  }
  .clicked-button {
    background: ${props => props.theme.mainColor};
  }
`;

//onClick
const handleVideoBookmark = () => {
  console.log('영상 북마크 열기');
};
const handleSentenceBookmark = () => {
  console.log('문장 북마크 열기');
};
const handleWordBookmark = () => {
  console.log('단어 북마크 열기');
};

const BookmarkBoard = () => {
  return (
    <div>
      <Bookmark>
        <Stack>
          <Button
            className="unclicked-button"
            variant="contained"
            size="large"
            onClick={handleVideoBookmark}
            style={{
              margin: '0px 0px 0px 50px',
              borderRadius: '30px 0px 0px 30px',
              width: '4em',
              height: '8em',
            }}
          >
            {' '}
            <Typography align="center" color="white" fontSize={'30px'}>
              영상
            </Typography>
          </Button>
          <Button
            className="clicked-button"
            variant="contained"
            size="large"
            onClick={handleSentenceBookmark}
            style={{
              margin: '0px 0px 0px 50px',
              borderRadius: '30px 0px 0px 30px',
              width: '4em',
              height: '8em',
            }}
          >
            <Typography align="center" color="white" fontSize={'30px'}>
              문장
            </Typography>
          </Button>
          <Button
            className="unclicked-button"
            variant="contained"
            size="large"
            onClick={handleWordBookmark}
            style={{
              margin: '0px 0px 0px 50px',
              borderRadius: '30px 0px 0px 30px',
              width: '4em',
              height: '8em',
            }}
          >
            {' '}
            <Typography align="center" color="white" fontSize={'30px'}>
              단어
            </Typography>
          </Button>
        </Stack>
        <Paper
          elevation={3}
          style={{
            width: '1500x',
            height: '400px',
            padding: 100,
            margin: '0px 100px 50px 150px', //책갈피 50px
          }}
        ></Paper>
      </Bookmark>
    </div>
  );
};

export default BookmarkBoard;
