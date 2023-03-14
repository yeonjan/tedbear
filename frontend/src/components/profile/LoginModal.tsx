import styled from 'styled-components';
import ModalBg from 'assets/img/ModalMan.png';

const DarkBackground = styled.div`
  background-color: rgba(0, 0, 0, 0.2);
  width: 100vw;
  height: 100vh;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  position: absolute;
`;

const Modal = styled.div`
  border: 1px solid black;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 30vw;
  height: 50vh;
  background-image: url(${ModalBg});
  z-index: 1;
  border-radius: 16px;
  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.04);
`;

interface Props {
  setOpenModal: React.Dispatch<React.SetStateAction<boolean>>;
}

const LoginModal = ({ setOpenModal }: Props) => {
  return (
    <div>
      <DarkBackground onClick={() => setOpenModal(false)} />
      <Modal></Modal>
    </div>
  );
};

export default LoginModal;
