package com.ssafy.tedbear.domain.sentence.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;

import com.ssafy.tedbear.domain.video.entity.Video;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Entity
@Getter
@Table(name = "sentence_tb")
@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Builder
@ToString
public class Sentence {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long no;

	@NotNull
	private int score;

	@NotNull
	@Column(columnDefinition = "TEXT")
	private String content;

	@Column(columnDefinition = "TEXT")
	private String translation;

	@NotNull
	@Column(name = "start_time")
	private int startTime;

	@NotNull
	@Column(name = "end_time")
	private int endTime;

	@ManyToOne
	@JoinColumn(name = "video_no")
	private Video video;

}
