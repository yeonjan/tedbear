package com.ssafy.tedbear;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;

import com.ssafy.tedbear.global.common.oauth2.AppProperties;

@EnableConfigurationProperties(AppProperties.class)
@SpringBootApplication
public class TedbearApplication {

	public static void main(String[] args) {
		SpringApplication.run(TedbearApplication.class, args);
	}

}

