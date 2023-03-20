package com.ssafy.tedbear.domain.video.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.tedbear.global.util.data.service.DataService;

import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
@RequestMapping("video")
public class VideoController {
	final DataService dataService;

	// 추천 영상 12개
	@GetMapping("/recommand/list")
	public void initWord() {
		dataService.initWord();
	}

	// 문장에 있는 단어 넣기
	@GetMapping("/init-sentence-word")
	public void initSentenceWord() {
		dataService.initSentenceWord();
	}

	// 영상과 문장 넣기
	@GetMapping("/init-video-sentence")
	public void initVideoSentence() {
		dataService.initVideoSentence();
	}

	// 카테고리 넣기
	@GetMapping("/init-category")
	public void initCategory() {
		dataService.initCategory();
	}

	// 문장에 점수 넣기
	@GetMapping("/init-sentence-score")
	public void initSentenceScore() {
		dataService.initSentenceScore();
	}

}
