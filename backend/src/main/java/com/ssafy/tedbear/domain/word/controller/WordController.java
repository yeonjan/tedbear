package com.ssafy.tedbear.domain.word.controller;

import org.apache.coyote.Response;
import org.springframework.data.domain.Pageable;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.ssafy.tedbear.domain.word.dto.WordDto;
import com.ssafy.tedbear.domain.word.repository.WordRepository;
import com.ssafy.tedbear.domain.word.repository.WordSentenceRepository;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Controller
@RequiredArgsConstructor
@Transactional
@RequestMapping("/word")
public class WordController {

	private final WordRepository wordRepository;
	private final WordSentenceRepository wordSentenceRepository;

	@GetMapping("/search")
	public ResponseEntity<?> searchWord(WordDto.Request query, Pageable pageable){
		String word = query.getQuery();
		return null;
	}
}
