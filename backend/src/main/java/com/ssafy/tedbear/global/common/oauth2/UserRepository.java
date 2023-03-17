package com.ssafy.tedbear.global.common.oauth2;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ssafy.tedbear.domain.member.entity.Member;

public interface UserRepository extends JpaRepository<Member, Long> {
	Optional<Member> findByUid(String uid);
}
