import styled from 'styled-components';
import { useState, useEffect } from 'react';
import { getSentenceBookmark } from 'utils/api/bookmarkApi';

interface IBookmarkSentence {
  no: number;
  content: string;
  translation: string;
  bookMarked: boolean;
  score: number;
  watchId: string;
  startTime: number;
  endTime: number;
}

const BookIn = styled.div`
  position: absolute;
  max-height: 800px;
  overflow: auto;
  margin: 20px;
`;

const BookmarkSentence = () => {
  const [sentenceBookmark, setSentenceBookmark] = useState<IBookmarkSentence[]>(
    [],
  );

  useEffect(() => {
    const fetchData = async () => {
      const data: IBookmarkSentence[] = await getSentenceBookmark();
      setSentenceBookmark(data);
      console.log(data);
    };
    fetchData();
  }, []);

  return (
    <BookIn>
      <div>
        <h2>Bookmarked Sentence</h2>
        {/* {sentenceBookmark} */}
      </div>
    </BookIn>
  );
};

export default BookmarkSentence;
