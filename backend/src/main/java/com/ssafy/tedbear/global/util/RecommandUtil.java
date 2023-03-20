package com.ssafy.tedbear.global.util;

import java.util.Random;

public class RecommandUtil {
	// 정규분포 이용해서, +- 10000 범위의 추천 스코어 리턴
	public static int getRecommandScore(int myScore) {
		Random random = new Random();
		int rand = (int)(random.nextGaussian() * 10000 / 2.58);
		rand = Math.max(rand, -10000);
		rand = Math.min(rand, 10000);
		return myScore + rand;
	}
}
