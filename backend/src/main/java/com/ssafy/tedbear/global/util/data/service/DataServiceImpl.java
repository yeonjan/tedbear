package com.ssafy.tedbear.global.util.data.service;

import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.apache.tomcat.util.json.JSONParser;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;

import com.ssafy.tedbear.domain.sentence.repository.SentenceRepository;
import com.ssafy.tedbear.domain.video.entity.VideoCategory;
import com.ssafy.tedbear.domain.video.repository.VideoCategoryRepository;
import com.ssafy.tedbear.domain.video.repository.VideoRepository;
import com.ssafy.tedbear.domain.word.entity.Word;
import com.ssafy.tedbear.domain.word.repository.WordRepository;
import com.ssafy.tedbear.global.util.JSONParseUtil;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class DataServiceImpl implements DataService {
	private final VideoRepository videoRepository;
	private final SentenceRepository sentenceRepository;
	private final WordRepository wordRepository;
	private final VideoCategoryRepository videoCategoryRepository;

	@Override
	public void initWord() {
		try {
			List<LinkedHashMap> jsonList = JSONParseUtil.getListFromJson("/data/cefr_vocab_en.json");

			Map<Object, Integer> scoreMap = new HashMap<>();
			scoreMap.put("A1", 358);
			scoreMap.put("A2", 716);
			scoreMap.put("B1", 1074);
			scoreMap.put("B2", 1432);
			scoreMap.put("C1", 1790);
			scoreMap.put("C2", 2148);
			// wordRepository.deleteAll();
			List<Word> wordList = new ArrayList<>();
			for (LinkedHashMap element : jsonList) {
				Word word = Word.builder()
					.content((String)element.get("word"))
					.score(scoreMap.get(element.get("level")))
					.build();
				wordList.add(word);
				// wordRepository.save(word);
			}
			// wordRepository.saveAll(wordList);

		} catch (Exception e) {
			e.printStackTrace();
		}
		// wordRepository.save(Word.builder().content("Sister").mean("누이").score(-1).build());
	}

	@Override
	public void initVideoSentence() {
		try {
			LinkedHashMap json = JSONParseUtil.getLinkedHashMapFromJson("/data/video_data.json");

			for (Object key : json.keySet()) {
				LinkedHashMap element = (LinkedHashMap)json.get(key);
				System.out.println(element.keySet());
			}
			Object key = "tB5J9qgM2zI";
			LinkedHashMap test = (LinkedHashMap)json.get(key);
			System.out.println(test);
			VideoCategory videoCategory = videoCategoryRepository.findById(
				Long.valueOf((String)test.get("category_no"))).get();
			String title = (String)test.get("title");
			String date = (String)test.get("published_at");
			String thumbnailUrl = (String)test.get("thumbnail_url");
			String videoUrl = (String)test.get("video_url");
			// List<List<String,String>>
			// System.out.println(test.get("scripts"));
			System.out.println(videoCategory);
			System.out.println(title);
			System.out.println(date);
			System.out.println(thumbnailUrl);
			System.out.println(videoUrl);

		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	@Override
	public void initCategory() {
		try {
			LinkedHashMap json = JSONParseUtil.getLinkedHashMapFromJson("/data/category_data.json");
			for (Object key : json.keySet()) {
				VideoCategory videoCategory = VideoCategory.builder()
					.name((String)json.get(key))
					.no(Long.valueOf((String)key))
					.build();
				videoCategoryRepository.save(videoCategory);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	;
}
