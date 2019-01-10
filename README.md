1.Deduplication_data 파일 실행 (중복 행 제거)
$ python Deduplication_data "파일이름"

2.data_analysis 파일 실행(데이터 분포도 확인)

1)단일 유니 레이블 데이터
$python data_analysis.py --one "파일이름" --uni
2)다중 유니 레이블 데이터
$python data_analysis.py --total --uni
3)단일 멀티 레이블 데이터
$python data_analysis.py --one "파일이름" --multi
4)다중 멀티 레이블 데이터
$python data_analysis.py --total --multi
