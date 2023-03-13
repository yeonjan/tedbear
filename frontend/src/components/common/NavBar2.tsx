import styled from 'styled-components';
import { Link } from 'react-router-dom';

const Nav = styled.div`
  width: 104px;
  height: 100vh;
  background-color: ${props => props.theme.mainColor};
`;

const NavBar2 = () => {
  return (
    <Nav>
      <ul>
        <li>
          <Link to="/home">Home</Link>
        </li>
        <li>
          <Link to="/game">Game</Link>
        </li>
        <li>
          <Link to="/profile">Profile</Link>
        </li>
        <li>
          <Link to="/yuha">yuha</Link>
        </li>
      </ul>
    </Nav>
  );
};

export default NavBar2;
