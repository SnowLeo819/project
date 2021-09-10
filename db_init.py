from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.perf_it

db.qna.drop();
db.ans.drop();
db.like.drop();

# 작성중 내용, 완성본 아님

doc = [
    {'idx': 1, 'quiz': "코로나 시국 종료!<br>제일 먼저 가고 싶은 여행지는?", 'ans_01': "도시의 빌딩 숲에서 멋진 야경을<br>감상할 수 있는 미국 뉴욕", 'ans_02': "새하얀 설산에서 다양한 액티비티를<br>즐길 수 있는 스위스 ", 'ans_03': "와인과 함께 우아한 만찬을<br>즐길 수 있는 프랑스", 'ans_04': "눈 앞에 펼쳐진 푸른 바다를 보며<br>휴식할 수 있는 괌"},
    {'idx': 2, 'quiz': "즐거운 여행을 끝마치고<br>집으로 돌아온 나는?", 'ans_01': "역시 여행은 주기적으로 다녀줘야 제 맛,<br> 바로 다음엔 어디를 가볼까~", 'ans_02': "그 동안 못 봤던 친구들에게 여행 썰<br>풀어줘야지, 바로 약속을 잡는다",
     'ans_03': "여행지에서 사온 기념품 정리하고<br>밀린 집안일부터 해야지", 'ans_04': "돌아다니느라 너무 피곤했음,<br>집에서 휴식"},
    {'idx': 3, 'quiz': "갑작스럽게 휴무를 얻게 되었다!<br>오늘의 일정은?", 'ans_01': "다들 모여! 나들이 가자~", 'ans_02': "근손실 못참지!",
     'ans_03': "출출한데 뭐라도 사올까?", 'ans_04': "혼자 뒹굴뒹굴.."},
    {'idx': 4, 'quiz': "서점에 들어간 당신,<br>가장 먼저 집어든 책의 제목은?", 'ans_01': "너와 함께라면 인생도 여행이다", 'ans_02': "백년운동",
     'ans_03': "백종원의 집밥 요리 레시피", 'ans_04': "달러구트 꿈 백화점"},
    {'idx': 5, 'quiz': "책을 구매하고 카페로 들어간<br>당신이 고른 메뉴는?", 'ans_01': "얼어죽어도 아이스 아메리카노!", 'ans_02': "내 취향이 어때서! 민트초코라떼", 'ans_03': "알콜은 나의 힘! 와인에이드",
     'ans_04': "더워죽어도 핫초코"},
    {'idx': 6, 'quiz': "음료를 다 마시고 카페를 나온 당신<br>오늘의 날씨는?", 'ans_01': "나들이 가기 좋게 맑은 날", 'ans_02': "밖으로 나가면 안되는 폭염", 'ans_03': "파전에 막걸리가 땡기는 소나기",
     'ans_04': "간판 날아갈 거 같은 태풍"},
]

ansDoc = [
    # 추천 활동명, 추천멘트 1&2, 추천데이터 1~3위 (이미지주소, 이름, 장르or부제 , 출연진 등 세부 정보 1&2

    {'idx': 1, 'type': 'A', 'brand': 'LE LABO', 'eng': 'ANOTHER 13 EDP', 'kor': '르라보 어나더 13 EDP',
     'desc': ' 암브록스, 자스민, 이끼, 암브레트 시드 등의 열 세가지 원료들이 섞여 중독성 있는 우디 머스크 계열의 향', 'keyword': ['포근한', '편안한', '성숙한']},
    {'idx': 2, 'type': 'B', 'brand': 'diptyque', 'eng': 'TAMDAO', 'kor': '딥디크 탐다오',
     'desc': '열대 다우림 속의 나무와 오래된 사원 주위에서 샌덜우드 나무를 끌고 다니는 코끼리 모습을 그린 관능적인 향수', 'keyword': ['관능적인', '매혹적인', '고귀한', '우디']},
    {'idx': 3, 'type': 'C', 'brand': 'Jo Malon', 'eng': 'Lime Basil & Mandarin Cologne', 'kor': '조말론 라임바질앤 만다린',
     'desc': '카리브해의 산들바람에서 실려온 듯한 라임향에 톡 쏘는 바질과 향기로운 백리향이 더해져 독특한 조합을 만들어 냅니다.',
     'keyword': ['상큼한', '신선한', '밝은', '시트러스']},
    {'idx': 4, 'type': 'D', 'brand': 'BYREDO', 'eng': 'LA TULIPE', 'kor': '바이레도 라튤립',
     'desc': '한 계절에 처음 맺는 꽃봉오리처럼 활기 넘치고 매력적이고 낙천적인 느낌의 향수',
     'keyword': ['발랄한', '매력적인', '낙천적인', '플로럴']},
]

likeDoc = [
    {'idx': 1, 'like': 0},
]



db.qna.insert_many(doc);
db.ans.insert_many(ansDoc);