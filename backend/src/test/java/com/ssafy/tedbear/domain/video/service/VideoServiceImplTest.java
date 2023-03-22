package com.ssafy.tedbear.domain.video.service;

import static org.junit.jupiter.api.Assertions.*;

import java.time.LocalDateTime;
import java.util.NoSuchElementException;
import java.util.concurrent.TimeUnit;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.TestPropertySource;

import com.ssafy.tedbear.domain.member.entity.Member;
import com.ssafy.tedbear.domain.member.repository.MemberRepository;
import com.ssafy.tedbear.domain.video.entity.Video;
import com.ssafy.tedbear.domain.video.entity.WatchingVideo;
import com.ssafy.tedbear.domain.video.repository.WatchingVideoRepository;

@SpringBootTest
class VideoServiceImplTest {
	@Autowired
	WatchingVideoRepository watchingVideoRepository;
	@Autowired
	MemberRepository memberRepository;

	@Test
	@DisplayName("마지막으로 업데이트된 영상 잘 찾아오는지 테스트")
	public void saveWatchingTest() throws InterruptedException {
		Member member = memberRepository.findById(1L)
			.orElseThrow(() -> new NoSuchElementException("해당 회원을 찾을 수 없습니다"));
		long lastVideoNo = 1100;
		for (long videoNo = 1000; videoNo <= lastVideoNo; videoNo++) {
			WatchingVideo watchingVideo = WatchingVideo.builder()
				.video(Video.builder().no(videoNo).build())
				.member(member)
				.updatedDate(LocalDateTime.now())
				.videoProgressTime(11)
				.videoStatus(false)
				.build();
			watchingVideoRepository.save(watchingVideo);
			TimeUnit.SECONDS.sleep(1);
			System.out.println(videoNo);
		}
		assertEquals(watchingVideoRepository.findTop1ByMemberAndVideoStatusOrderByUpdatedDateDesc(member, false)
			.get()
			.getVideo()
			.getNo(), lastVideoNo);

	}
}