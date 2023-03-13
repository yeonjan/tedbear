import { Outlet } from 'react-router-dom';
import NavBar2 from 'components/common/NavBar2';
import styled from 'styled-components';
import { useLocation } from 'react-router-dom';

const Wrapper = styled.div`
  display: flex;
  flex-direction: row;
  height: 100vh;
`;

const OutletWrapper = styled.div`
  width: 100%;
  border: 1px solid black;
`;

const LayoutPage = () => {
  const location = useLocation();
  const pathname = location.pathname;

  return (
    <Wrapper>
      {pathname !== '/test' && <NavBar2 />}
      <OutletWrapper>
        <Outlet />
      </OutletWrapper>
    </Wrapper>
  );
};

export default LayoutPage;
