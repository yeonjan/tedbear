package com.ssafy.tedbear.domain.word.dto;

import lombok.Getter;
import lombok.Setter;

public class WordDto {

	@Getter
	@Setter
	public static class Request{
		String query;
	}
}
