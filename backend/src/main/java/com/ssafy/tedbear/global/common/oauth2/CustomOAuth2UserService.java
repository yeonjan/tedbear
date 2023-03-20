package com.ssafy.tedbear.global.common.oauth2;

import lombok.RequiredArgsConstructor;
import org.springframework.security.oauth2.client.userinfo.DefaultOAuth2UserService;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserRequest;
import org.springframework.security.oauth2.core.OAuth2AuthenticationException;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class CustomOAuth2UserService extends DefaultOAuth2UserService {

    private final UserRepository userRepository;

    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException{
        // 로그인에 성공하면 OAuth2UserRequest에 유저 정보가 담긴다.
        OAuth2User oAuth2User = super.loadUser(userRequest);
        System.out.println(oAuth2User.getAttributes());

        return oAuth2User;
    }

    private User saveOrUpdate(CustomOAuth2User oAuth2User){
        User user = User.of(oAuth2User);
        userRepository.findByUid(user.getEmail()).ifPresent(entity -> user.setId(entity()));
        return userRepository.save(user);
    }
}
