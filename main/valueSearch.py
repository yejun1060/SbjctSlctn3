# 교과 영역
dic_1 = {'A': '기초',
         'B': '탐구',
         'C': '체육과 예술',
         'D': '생활과 교양', }
# 교과군
dic_2 = {'A': '국어',
         'B': '영어',
         'C': '수학',
         'D': "사회",
         "E": "과학",
         'F': '예술',
         'G': '체육',
         'H': '기술과 가정',
         'I': '제2외국어',
         'J': '한문',
         'K': '교양'}
# 구분
dic_3 = {'A': '일반',
         'B': '진로',
         'C': '공통'}
# 단위수
dic_4 = {'A': 2,
         'B': 3,
         'C': 4,
         'D': 5,
         'E': 6, }
# 과목구분코드
dic = {'연극': 'CFAC',
       '음악 연주/미술 창작': 'CFBC',

       '정보': 'DHAB-1',
       '한문1': 'DJAB-1',
        
       '언어와 매체': 'AAAB-1',
       '확률과 통계': 'ACAB-1',
       '영어회화': 'ABAB-1',
       '영미 문학 읽기': 'ABBB-1',

       '일본어1': 'DIAC-1',
       '중국어': 'DIAC-2',

       '한국지리': 'BDAE-1',
       '사회문화': 'BDAE-2',
       '세계사': 'BDAE-3',
       '생활과 윤리': 'BDAE-4',
       '경제': 'BDAE-5',

       '물리학1': 'BEAE-1',
       '화학1': 'BEAE-2',
       '생명과학1': 'BEAE-3',
       '지구과학1': 'BEAE-4',

       '프로그래밍': 'DHBE-6',

       '화법과 작문': 'AAAE-2',
       '심화 국어': 'AABB-1',
       '고전 읽기': 'AABB-2',
       '실용 국어': 'AABB-3',

       '미적분': 'ACAE-2',
       '기하': 'ACBE-1',
       '수학과제 탐구': 'ACBB-2',
       '경제수학': 'ACBB-3',
       '실용 수학': 'ACBB-4',

       '영어 독해와 작문': 'ABAE-2',
       '영어권문화': 'ABBB-2',
       '실용영어': 'ABBB-3',

       '미술 감상과 비평': 'CFBB-1',
       '드로잉': 'CFBB-2',
       '시창청음': 'CFBB-3',
       '음악 감상과 비평': 'CFBB-4',

       '세계지리': 'BDAE-6',
       '윤리와 사상': 'BDAE-7',
       '동아시아사': 'BDAE-8',
       '정치와 법': 'BDAE-9',
       '여행지리': 'BDBB-1',
       '사회문제 탐구': 'BDBB-2',
       '고전과 윤리': 'BDAB-3',

       '물리학2': 'BEBE-1',
       '화학2': 'BEBE-2',
       '생명과학2': 'BEBE-3',
       '지구과학2': 'BEBE-4',
       '물리학실험': 'BEBB-5',
       '화학실험': 'BEBB-6',
       '생명과학실험': 'BEBB-7',
       '지구과학실험': 'BEBB-8',
       '과학사': 'BEBB-9',
       '생활과 과학': 'BEBB-10',

       '진로와 직업': 'DKAB-10',
       '가정 과학': 'DHBB-5',
       '공학 일반': 'DHBB-6',
       '사물인터넷 서비스': 'DHBB-7',
       '빅데이터 분석': 'DHBB-8',

       '체육전공실기기초': 'DCBA-1',
       '스포츠 경기 체력': 'DCBA-2',

       '중국어 회화1': 'DIBA-1',
       '일본어 회화1': 'DIBA-2',
       '중국문화': 'DIBA-3',
       '일본문화': 'DIBA-4',

       '철학': 'DKAA-1',
       '논리학': 'DKAA-2',
       '심리학': 'DKAA-3',
       '교육학': 'DKAA-4',
       '논술': 'DKAA-5',
       '환경': 'DKAA-6',
       '강원도의 역사와 문화': 'DKAA-7',
       '실용 경제': 'DKAA-8',
       '공중 보건': 'DKAA-9',
       '바리스타': 'DKAA-10',

       '창의 경영': 'DHBA-1',
       '인간발달': 'DHBA-2',
       '건축 일반': 'DHBA-3',
       '기초 제도': 'DHBA-4',

       '응용 프로그래밍 개발': 'DHBA-5', }
# 6단위 과목 목록
subject_list = ["화법과 작문", "미적분", "기하", "영어 독해와 작문", "세계 지리", "윤리와 사상", "동아시아사", "정치와 법", "물리학1", "화학1", "생명과학1", "지구과학1", "물리학2", "화학2", "생명과학2", "지구과학2"]


def search_value(temp):
    print("temp" + temp)
    test = temp.split(';')
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    l = []

    for i in test:

        # -가 포함됨. 그러므로 split 해야됨
        if dic[i].find("-") != -1:
            t = dic[i].split("-")[0]

        # -가 포함되지 않음. 그러므로 split 없이 dic에서 찾아서 append하면 됨.
        else:
            t = dic[i]

        for j in t:
            l.append(j)

        # 진로과목수 카운트
        if l[2] == "B":
            a += 1

        # 기초교과 카운트
        if l[0] == "A":
            b += dic_4[l[3]]
        
        # 사회과목 카운트
        if l[1] == "D":
            c += dic_4[l[3]]
        
        # 과학과목 카운트
        if l[1] == "E":
            d += dic_4[l[3]]

        # 생활 교양 카운트
        if l[0] == "D":
            e += dic_4[l[3]]

        # 예술과목 카운트
        if l[0] == "C":
            f += dic_4[l[3]]

        l.clear()

    return str(a)+";"+str(b)+";"+str(c)+";"+str(d)+";"+str(e)+";"+str(f)
