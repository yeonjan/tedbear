import styled from 'styled-components';
import { useState, useEffect } from 'react';
import { getVideoBookmark } from 'utils/api/bookmarkApi';

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
  const [videoBookmark, setVideoBookmark] = useState<IBookmarkVideo[]>([]);

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
      </div>
    </BookIn>
  );
};

export default BookmarkVideo;
