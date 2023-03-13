import styled from 'styled-components';
import { Link } from 'react-router-dom';

const Nav = styled.div`
  width: 104px;
  border: 1px solid black;
`;

const NavBar = () => {
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

export default NavBar;
