import PuzzleCover from 'components/puzzle/PuzzleCover';
import styled from 'styled-components';

//style
const Puzzle = styled.div`
  .puzzle-board {
    background: ${props => props.theme.mainLightColor};
  }
`;

//function
const PuzzlePage = () => {
  return (
    <Puzzle>
      <div className="puzzle-board">
        <PuzzleCover></PuzzleCover>
      </div>
    </Puzzle>
  );
};

export default PuzzlePage;
