import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import argparse

#dir path
YOUR_DIR_PATH ='./data'

#명령인수 설정
parser = argparse.ArgumentParser()
parser.add_argument( "--one", help="choose one file",required=True)
parser.add_argument( "--total", help="choose all file",action = 'store_true')
parser.add_argument( "--uni", help="choose uni label",action = 'store_true')
parser.add_argument( "--multi", help="choose multi label",action = 'store_true')

args = parser.parse_args()

#명령인수로 넣은 파일을 읽을 수 있도록 도와줍니다.
def Read_file_name():
    file_name =args.one
    # for num in range(1,len(sys.argv)-1):
    #     file_name += sys.argv[num] +' '
    # file_name+=sys.argv[len(sys.argv)-1]

    return file_name

#csv 파일 읽고 dataframe 양식으로 return
def Read(file_name):
    filepath = os.path.join(YOUR_DIR_PATH, file_name)
    df = pd.read_csv(filepath)
    df['MAIN EMOTION'] = df['MAIN EMOTION'].astype(int)
    return df

#멀티레이블 데이터를 읽습니다.
def Read_multi_data(file_name):
    multi_label = []
    df = Read(file_name)
    for label in df["EMOTIONS"]:

        #set 10번 delimiter ,가 아니라 ; 으로 되어있습니다. 참고 바랍니다.
        label = label.replace(';',',')

        #set 4번 delimiter ,가 아니라 . 으로 되어있어서 추가합니다.
        label = label.replace('.',',')
        idx_len = label.split(',')
        #비어있는 값 제거(결측치 제거)
        for idx in idx_len:
            if(idx == ''):
                continue
            multi_label.append(int(idx))
    multi_df = pd.DataFrame({'EMOTIONS': multi_label})
    multi_df['EMOTIONS'] = multi_df['EMOTIONS'].astype(int)
    return multi_df

#data 디렉토리에 있는 preprocessing을 진행한 파일만 골라내기
def Is_newdata():
    file =[]
    file_list = os.listdir(YOUR_DIR_PATH)
    for item in file_list:
        if item.find('new') is not -1 :
            file.append(item)
    return file

#데이터 분포를 확인합니다.
def Show_plt(df,category,file_name='ALL'):
    sns.countplot(x=category, data=df)
    plt.title(file_name)
    plt.show()

#단일 csv, 유니 레이블 분포도 확인
def Show_Uni(file_name):
    # read
    df = Read(file_name)
    Show_plt(df,'MAIN EMOTION',file_name)


#다중 csv, 유니 레이블 분포도 확인
def Show_Uni_All():
    df = pd.DataFrame({'MAIN EMOTION':[]})
    #read
    lst =[]
    file_list = Is_newdata()
    for file in file_list:
        lst.append(Read(file))

    #모든 행을 결합합니다.
    df = pd.concat(lst)
    #df_total["MAIN EMOTION"] = df_total["MAIN EMOTION"].astype(int)
    Show_plt(df,'MAIN EMOTION')


#단일 csv,멀티 레이블 분포도 확인
def Show_Multi(file_name):
    multi_df = Read_multi_data(file_name)
    multi_df['EMOTIONS']=multi_df['EMOTIONS'].astype(int)
    Show_plt(multi_df,'EMOTIONS',file_name)

def Show_Multi_All():
    #read
    lst = []
    file_list = Is_newdata()
    for file in file_list:
        Show_Multi(file)
        lst.append(Read_multi_data(file))
    df_total = pd.concat(lst)
    Show_plt(df_total,'EMOTIONS')





if __name__ == "__main__":
    #단일 유니레이블 데이터
    if args.one and args.uni:
        file_name = Read_file_name()
        Show_Uni(file_name)

    #다중 유니레이블 데이터
    if args.total and args.uni:
        Show_Uni_All()

    #단일 멀티레이블 데이터
    if args.one and args.multi:
        #file_name = Read_file_name()
        Show_Multi(file_name)

    #다중 멀티레이블 데이터
    if args.total and args.multi:
        Show_Multi_All()