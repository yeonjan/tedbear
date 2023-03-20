package com.ssafy.tedbear.global.common.oauth2;

import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseCookie;
import org.springframework.security.core.Authentication;
import org.springframework.security.web.authentication.SimpleUrlAuthenticationSuccessHandler;

import javax.servlet.Servlet;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Optional;

@RequiredArgsConstructor
public class OAuth2LoginSuccessHandler extends SimpleUrlAuthenticationSuccessHandler {
    private final UserRepository userRepository;
    private final JwtTokenProvider jwtTokenProvider;

    @Override
    public void onAuthenticationSuccess(HttpServletRequest httpServletRequest, HttpServletResponse response, Authentication authentication) throws IOException, ServletException{
        String accessToken = jwtTokenProvider.createAccessToken(authentication);
        String refreshToken = jwtTokenProvider.createRefreshToken(authentication);

        CustomOAuth2User oAuth2User = (CustomOAuth2User) authentication.getPrincipal();
        saveOrUpdateUser(refreshToken, oAuth2User);

        ResponseCookie cookie = ResponseCookie.from("refresh", refreshToken)
                .httpOnly(true)
                .maxAge(JwtTokenProvider.REFRESH_TOKEN_VALIDATE_TIME)
                .path("/")
                .build();

        clearAuthenticationAttributes(request, response);

        response.addHeader("Set-Cookie", cookie.toString());
        response.getWriter().write(accessToken);
    }

    private void saveOrUpdateUser(String refreshToken, CustomOAuth2User oAuth2User){
        Optional<User> opt = userRepository.findByEmail(oAuth2User.getEmail());
        User user;

        if(opt == null){
            user = User.builder()
                    .email(oAuth2User.getEmail())
                    .nickname(oAuth2User.getNickname())
                    .refreshToken(refreshToken)
                    .build();
        } else{
            user = opt.get();
            user.updateRefreshToken(refreshToken);
        }

        userRepository.save(user);
    }

    protected void clearAuthenticationAttributes(HttpServletRequest request, HttpServletResponse httpServletResponse){
        super.clearAuthenticationAttributes(request);
    }
}
