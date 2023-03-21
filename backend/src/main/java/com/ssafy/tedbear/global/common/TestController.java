package com.ssafy.tedbear.global.common;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class TestController {
	@GetMapping("/test")
	public static ResponseEntity<ResponseDto<String>> test() {
		return new ResponseEntity<>(new ResponseDto("hi"), HttpStatus.OK);

	}

}
