package com.ssafy.tedbear.global.common.oauth2;

import java.util.Map;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
public class OAuthAttributes {
	private Map<String, Object> attributes;
	private String nameArrtibuteKey;
	private String name;

	public static OAuthAttributes of(String registrationId, String userNameAttributeName,
		Map<String, Object> attributes) {

		// 네이버, 카카오 추가
		if ("naver".equals(registrationId))
			return ofNaver("id", attributes);
		if ("kakao".equals(registrationId))
			return ofKakao("id", attributes);

		return ofGoogle("id", attributes);
	}

	private static OAuthAttributes ofGoogle(String userNameAttributeName, Map<String, Object> attributes) {
		return OAuthAttributes.builder()
			.name((String)attributes.get("name"))
			.attributes(attributes)
			.nameArrtibuteKey(userNameAttributeName)
			.build();
	}

	private static OAuthAttributes ofNaver(String userNameAttributeName, Map<String, Object> attributes) {
		Map<String, Object> response = (Map<String, Object>)attributes.get("response");

		return OAuthAttributes.builder()
			.name((String)response.get("name"))
			.attributes(response)
			.nameArrtibuteKey(userNameAttributeName)
			.build();
	}

	private static OAuthAttributes ofKakao(String userNameAttributeName, Map<String, Object> attributes) {
		Map<String, Object> response = (Map<String, Object>)attributes.get("kakao_account");
		Map<String, Object> account = (Map<String, Object>)attributes.get("profile");

		return OAuthAttributes.builder()
			.name((String)account.get("nickname"))
			.attributes(response)
			.nameArrtibuteKey(userNameAttributeName)
			.build();
	}

}
