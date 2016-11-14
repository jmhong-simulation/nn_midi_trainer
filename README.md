# nn_midi_trainer

목표

- 1차: 현재 C++ 버전을 Python Tensorflow  버전으로 변환. (현재는 1CPU에서 밤새 훈련이 필요했기 때문에 GPU 사용시 속도 향상을 기대)
- 2차: 훈련 품질 높이기 (완전 암기- 현재는 이전 음에서 다음 음 출력, 출력할 음 결정 방법 - 현재는 주사위)
- 3차: 더 많은 곡들 테스트

Meeting

#0

- 미디 데이터를 훈련 데이터로 바꿔주는 모듈을 파이썬 버전으로 만들기 (파이썬 모듈이 별도로 들었음)  
- 피아노 연주 모듈 파이썬으로 개발 (이것도 파이썬 모듈이 있을 경우 더 쉬움)
- NN을 Python TF로 구현 (어렵지 않음)
- 데이터 구조 개선 및 추가 테스트 (여기서부터는 미지의 영역)
- 코드 정리 및 깃헙 공개 (readme파일에 참여자 이름과 이메일 주소 넣는 것 잊지 마세요)
- 기고문 문서 작성 

#1
Piano player (https://github.com/Calysto/chuck)
Midi reading (MIDO or IOMIDI)

#2
Data structure for training
Tensorflow NN (FCNN)

#3
Test

#4
Test

#5
Review

Outline

Introduction (Previous Work)

summarize each reference in 2-3 sentences.

Learning 
Deep Jazz https://github.com/jisungk/deepjazz/blob/master/generator.py 유선우
Magenta 조동헌

Rule based
Representative 1-3 
조동헌

Piano player

Midi reading
정종현

Data structure for training

Tensorflow NN (FCNN)

Results and discussion
- moon light, epoch vs accuracy
- additional...

Conclusion
- Future work
- Github link

정종현, 조동헌, 유선우, 김준기, 홍정모
