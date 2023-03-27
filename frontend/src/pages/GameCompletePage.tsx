import { Button } from '@mui/material';
import { Stack } from '@mui/system';
import { ReactComponent as Complete } from 'assets/img/complete.svg';
import styled from 'styled-components';

const StyledComplete = styled.div`
  .whole {
    position: relative;
  }
  .complete-bg {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
  }
  .buttons {
  }
  .button-1 {
  }
  .button-2 {
  }
`;

const GameCompletePage = () => {
  return (
    <StyledComplete>
      <div className="whole">
        <Complete className="complete-bg">
          <Stack
            className="
        buttons"
          >
            <Button className="button-1"></Button>
            <Button className="button-2"></Button>
          </Stack>
        </Complete>
      </div>
    </StyledComplete>
  );
};

export default GameCompletePage;
