package com.ssafy.tedbear.domain.word.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.ssafy.tedbear.domain.member.entity.Member;
import com.ssafy.tedbear.domain.word.entity.Word;
import com.ssafy.tedbear.domain.word.entity.WordBookmark;

@Repository
public interface WordBookmarkRepository extends JpaRepository<WordBookmark, Long> {
	Optional<WordBookmark> findByMemberAndWord(Member member, Word word);
}