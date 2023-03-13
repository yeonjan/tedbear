import { useState } from 'react';
import styled from 'styled-components';

const DarkBackground = styled.div`
  background-color: rgba(0, 0, 0, 0.2);
  width: 100vw;
  height: 100vh;
  z-index: 0;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
`;

const LoginModal = (
  setOpenModal: React.Dispatch<React.SetStateAction<boolean>>,
) => {
  return (
    <div>
      <DarkBackground onClick={() => setOpenModal(false)}></DarkBackground>
      <div>Hi</div>)
    </div>
  );
};

export default LoginModal;
