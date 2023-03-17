package com.ssafy.tedbear.global.common.oauth2;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class OAuth2LoginSecurityConfig {

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		// http
		// .authorizeHttpRequests(authorize -> authorize
		// 	.anyRequest().authenticated()
		// )
		// .oauth2Login(withDefaults());
		// .oauth2Login(oauth2 -> oauth2
		// 	.authorizationEndpoint(authorization -> authorization
		// 	)
		// 	.redirectionEndpoint(redirection -> redirection
		// 	)
		// )
		return http.build();
	}
}
