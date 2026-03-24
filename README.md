# Cartoon Rendering
OpenCV를 이용하여 사진의 엣지를 표시해 만화풍(Cartoon Rendering)으로 변환하는 프로그램</br>
Canny Edge Detection과 Bilateral Filter를 조합하여 구현</br>
Cartoon Rendering 사용 전/후 비교 사진 출력

## 기능
1. 이미지 전처리 및 해상도 최적화
   - 입력받은 다양한 포맷의 이미지를 가로 600px 기준으로 비율을 유지하며 리사이즈
   - 처리 속도 향상 및 화면 출력이 잘리는 현상 방지
   - 히스토그램 평활화(Histogram Equalization)를 통해 이미지의 명암 대비 최적화
2. 정교한 엣지(윤곽선) 검출
   - OpenCV의 cv.Canny 알고리즘을 사용
   - 이중 임계값(Thresholding) 사용
     + 평활화된 이미지(Thresh: 800, 1700)에서 굵직한 선 추출
     + 원본 그레이 이미지(Thresh: 600, 1000)에서 세밀한 선 추출
   - 두 결과물을 bitwise_or 연산으로 합성하여 최종 윤곽선 확보
3. 카툰 효과 및 필터링
   - Bilateral Filter : 경계선은 유지하면서 피부나 배경의 질감을 부드럽게 뭉개 그림 같은 효과 부여
     + d=9, sigmaColor=75, sigmaSpace=75
   - Bitwise 연산 : 검출된 엣지를 반전(NOT)시켜 컬러 이미지 위에 검은색 테두리로 합성(AND)
4. 결과 시각화 및 자동 저장
   - 단계별 확인을 위한 3가지 윈도우 표시
     + Canny Edge1: hist: 평활화 이미지 기반 엣지 추출 과정</br>
       평활화 이미지(흑백) + 이미지 기반 엣지 + 최종 엣지
     + Canny Edge2: origin: 원본 이미지 기반 엣지 추출 과정</br>
       원본 이미지(흑백) + 이미지 기반 엣지 + 최종 엣지
     + Cartoon Rendering: 원본과 최종 결과물의 비교 화면</br>
       원본 이미지(컬러) + 최종 결과물(원본 + 최종 엣지)
   - 프로그램 종료 시 "파일명_result.jpg" 형식으로 결과물 자동 저장
5. 조작 방법
   - 이미지 선택 : 코드 내 img_select 변수 수정을 통해 sample_img 리스트 내 사진 변경 가능
   - 프로그램 종료 : 아무 키 입력
## 평가
- 만화 같은 느낌이 잘 표현되는 경우
  + 윤곽선이 뚜렷하고 물체가 투박한 경우
    - "Sample.png", "cityB.jpg", "cityD.webp"
  + 윤곽선이 많은 경우
    - "refl.jpg", "sea.jpg", "winter.png", "yellow.jpg"
- 만화 같은 느낌이 잘 표현되지 않는 경우
  + 빛으로 인해 그림자가 많은 경우
    - "aladdin.jpg"
  + 검은 색이 많은 경우
    - "hitman.jpg"
- 한계점
  1. 고정된 임계값(Threshold)
     - 다양한 이미지의 다양한 환경에 적용하기는 어렵다
  2. 조명에 취약
     - cv.equalizeHist를 사용해 이미지의 명암을 늘려 엣지 추출</br>
       그로인해 역광 혹은 노이즈에 취약하다
  3. '선'의 디테일과 굵기 조절 부재
     - 엣지의 선이 가늘어 검은 색이 많을 경우에 윤곽선의 구분이 어렵다
  4. 연산 속도
     - bilateralFilter를 사용해서 계산량이 많아 실시간 변환은 어렵다
