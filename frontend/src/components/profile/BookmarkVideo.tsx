import styled from 'styled-components';
import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getVideoBookmark } from 'utils/api/bookmarkApi';
import VideoLevel from 'assets/img/videoLevel.svg';
import BookmarkFull from 'assets/img/bookmarkFull.svg';
import BookmarkEmpty from 'assets/img/bookmarkEmpty.svg';

interface IBookmarkVideo {
  thumbnailUrl: string;
  title: string;
  watchId: string;
  score: number;
  bookMarked: boolean;
}

const BookIn = styled.div`
  position: absolute;
  max-height: 800px;
  overflow: auto;
  margin: 20px;
`;

const BookmarkVideo = () => {
  const navigate = useNavigate();
  const [videoBookmark, setVideoBookmark] = useState<IBookmarkVideo[]>([]);

  const handleClick = (watchId: string): void => {
    navigate(`/learning/${watchId}`);
  };

  useEffect(() => {
    const fetchData = async () => {
      const data: IBookmarkVideo[] = await getVideoBookmark();
      setVideoBookmark(data);
      console.log(data);
    };
    fetchData();
  }, []);

  return (
    <BookIn>
      <div>
        <h2>Bookmarked Video</h2>
        {/* {videoBookmark} */}
        <div>
          {videoBookmark.map((Thumnail, idx) => {
            return (
              <div className="wrapper" key={idx}>
                <img
                  className="main-img"
                  src={Thumnail.thumbnailUrl}
                  onClick={() => handleClick(Thumnail.watchId)}
                  alt=""
                />
                <img
                  src={VideoLevel}
                  className="video-level"
                  style={{
                    filter:
                      'invert(45%) sepia(78%) saturate(1707%) hue-rotate(161deg) brightness(93%) contrast(103%)',
                  }}
                ></img>
                <img
                  src={Thumnail.bookMarked ? BookmarkFull : BookmarkEmpty}
                  className="book-mark"
                ></img>
                <div className="title">{Thumnail.title}</div>
              </div>
            );
          })}
        </div>
      </div>
    </BookIn>
  );
};

export default BookmarkVideo;
