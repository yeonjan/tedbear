package com.ssafy.tedbear.domain.video.entity;

import java.sql.Timestamp;

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
@Table(name = "watching_video_tb")
@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class WatchingVideo {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long no;

	@NotNull
	@Column(name = "video_progress_time")
	private int videoProgressTime;

	@NotNull
	@Column(name = "video_status")
	private boolean videoStatus;

	@NotNull
	@Column(name = "updated_date")
	private Timestamp updatedDate;
}
