package com.ssafy.tedbear.domain.video.entity;

import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Getter
@Table(name = "video_tb")
@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Video {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long no;

	@NotNull
	private int score;

	@NotNull
	private String title;

	@NotNull
	@Column(name = "video_url")
	private String videoUrl;

	@NotNull
	@Column(name = "thumbnail_url")
	private String thumbnailUrl;

	@NotNull
	@Column(name = "published_date")
	private LocalDateTime publishedDate;
}
