package com.ssafy.tedbear.domain.word.service;

import javax.transaction.Transactional;

import org.springframework.stereotype.Service;

import com.ssafy.tedbear.domain.word.repository.WordRepository;
import com.ssafy.tedbear.domain.word.repository.WordSentenceRepository;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Service
@Transactional
@RequiredArgsConstructor
@Slf4j
public class WordServiceImpl {
	private final WordRepository wordRepository;
	private final WordSentenceRepository wordSentenceRepository;

	
}
