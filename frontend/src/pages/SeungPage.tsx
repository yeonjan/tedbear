import { useState } from 'react';
import LoginModal from 'components/profile/LoginModal';

const SeungPage = () => {
  const [modalOpen, setModalOpen] = useState<boolean>(false);

  return (
    <div>
      <h1>SeungPage</h1>
      <button onClick={() => setModalOpen(true)}>Start!</button>
      {modalOpen && <LoginModal setOpenModal={setModalOpen} />}
      <div style={{ display: 'flex', marginTop: '10px ' }}>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          <button>안녕</button>
          <button>안녕</button>
          <button>안녕</button>
        </div>
        <div
          style={{
            background: 'black',
            width: '40vw',
            height: '40vh',
            color: 'white',
          }}
        >
          단어장
        </div>
      </div>
    </div>
  );
};

export default SeungPage;
