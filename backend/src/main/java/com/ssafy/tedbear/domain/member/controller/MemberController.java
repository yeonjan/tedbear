package com.ssafy.tedbear.domain.member.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Controller
@RequestMapping("/member")
@NoArgsConstructor
@Slf4j
public class MemberController {
	@GetMapping("/test")
	public ResponseEntity<String> test() {
		return ResponseEntity.status(HttpStatus.OK).body("ikikkkii");
	}
}
