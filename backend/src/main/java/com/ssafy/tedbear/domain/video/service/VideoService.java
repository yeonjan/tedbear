package com.ssafy.tedbear.domain.video.service;

import com.ssafy.tedbear.domain.member.entity.Member;
import com.ssafy.tedbear.domain.video.dto.VideoDetail;
import com.ssafy.tedbear.domain.video.dto.VideoInfo;
import com.ssafy.tedbear.domain.video.dto.VideoInfoList;
import com.ssafy.tedbear.domain.video.dto.WatchingVideoInfo;

public interface VideoService {

	VideoInfoList getRecommendList(long memberNo);

	VideoDetail getDetail(long memberNo, String watchId);

	VideoInfo getWatchingRecent(long memberNo);

	VideoInfoList getWatchingList(long memberNo, int page);

	VideoInfoList getCompleteList(long memberNo, int page);

	void saveWatchingRecord(long memberNo, WatchingVideoInfo request);

	void saveCompleteRecord(long memberNo, WatchingVideoInfo request);

}
