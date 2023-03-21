package com.ssafy.tedbear.domain.sentence.dto;

import java.util.List;
import java.util.stream.Collectors;

import com.ssafy.tedbear.domain.sentence.entity.Sentence;

import lombok.Getter;

@Getter
public class SentenceDetailDto {
	Long no;
	int startTime;
	int endTime;
	String content;
	boolean bookmarked;

	//원본 비디오 영상 링크

	public SentenceDetailDto(Sentence sentence) {
		this.no = sentence.getNo();
		this.startTime = sentence.getStartTime();
		this.endTime = sentence.getEndTime();
		this.content = sentence.getContent();
	}

	public static class ListResponse {
		List<SentenceDetailDto> data;

		public ListResponse(List<Sentence> list) {
			//List<VideoDto.Info> data = videoList.stream().map(VideoDto.Info::new).collect(Collectors.toList());

			this.data = list.stream().map(((sentence) -> new SentenceDetailDto(sentence))).collect(Collectors.toList());
		}
	}

}
