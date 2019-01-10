import sys
import pandas as pd
import os

#디렉토리 생성
YOUR_FILE_PATH = "./data"

if not os.path.isdir(YOUR_FILE_PATH):
	os.mkdir(YOUR_FILE_PATH)

def read_csv(file_name):
    # read
    filepath = os.path.join(YOUR_FILE_PATH, file_name)
    df = pd.read_csv(filepath)#, na_values='NaN')

    #첫번째 중복행을 제외한 나머지는 삭제
    df = df.drop_duplicates(['SENTENCE'],keep='first')

    #결측치 제거
    df = df.dropna(axis=0)
    #df['MAIN EMOTION']=df['MAIN EMOTION'].astype(int)
    print(df)

    #write
    file_name = 'new_' + file_name
    file_path = os.path.join(YOUR_FILE_PATH, file_name)
    df.to_csv(file_path, sep=',', na_rep='NaN', index=False)
    return df

#명령인수로 실행
# $python Deduplication_data.py "file_name"
# file_name =''
# for num in range(1,len(sys.argv)-1):
#     file_name += sys.argv[num] +' '
# file_name+=sys.argv[len(sys.argv)-1]

file_name = sys.argv[1]
df = read_csv(file_name)

#코드 내에서 실행
#df = read_csv(file_name)



