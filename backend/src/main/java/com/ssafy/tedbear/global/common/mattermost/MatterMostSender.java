package com.ssafy.tedbear.global.common.mattermost;

import static com.ssafy.tedbear.global.common.mattermost.MatterMostMessageDto.*;

import com.ssafy.tedbear.global.common.FindMemberService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

import com.google.gson.Gson;

import lombok.RequiredArgsConstructor;

import javax.servlet.http.HttpServletRequest;

@Component
@RequiredArgsConstructor
public class MatterMostSender {

    @Value("${notification.mattermost.enabled}")
    private boolean mmEnabled;
    @Value("${notification.mattermost.webhook-url}")
    private String webhookUrl;

    private final RestTemplate restTemplate;
    private final MatterMostProperties mmProperties;
	private final FindMemberService findMemberService;

    public void sendMessage(Exception excpetion, HttpServletRequest req, String params) {
        if (!mmEnabled)
            return;

        try {
            Attachment attachment = Attachment.builder()
                    .color(mmProperties.getColor())
                    .pretext(mmProperties.getPretext())
                    .title(mmProperties.getTitle())
                    .text(mmProperties.getText())
                    .footer(mmProperties.getFooter())
                    .build();

            attachment.addExceptionInfo(excpetion, req);
            Attachments attachments = new Attachments(attachment);
            attachments.addProps(excpetion);
            String payload = new Gson().toJson(attachments);

            HttpHeaders headers = new HttpHeaders();
            headers.set("Content-type", MediaType.APPLICATION_JSON_VALUE);

            HttpEntity<String> entity = new HttpEntity<>(payload, headers);
            restTemplate.postForEntity(webhookUrl, entity, String.class);

        } catch (Exception e) {
        }

    }
}