package com.ssafy.tedbear.global.common;

import lombok.Getter;

@Getter
public class ResponseDto<T> {
	T data;

	public ResponseDto(T data) {
		this.data = data;
	}

}
