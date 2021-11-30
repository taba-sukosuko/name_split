import pandas as pd

def serch(filepath, header=1, name_num=1): 
  #ヘッダーがある場合はheader=1，ない場合はheader=0.　name_numは名前が記載されている列一番左から1，２，・・・
  dictionary = pd.read_csv("./dataset/kanji.csv", names=["firstname"])

  filepath = "./input/" + filepath
  
  if header == 1:
    files = pd.read_csv(filepath)
  else:
    files = pd.read_csv(filepath, header=None)

  files_copy = files.copy()

  firstname_list=[]
  search_order = [2, 3, 1, 4, 5]

  result_first = []
  result_last = []

  name_num = name_num - 1
  
  #print(files)
  dataset = files_copy.iloc[:, name_num] # 読み込んだデータから名前の所だけのデータを作成
  #print(dataset)

  #print("------1")
  for i in range(len(dataset)): # name_listのループ
    firstname_list=[]
    name = dataset.iloc[i]
    #print("------2")

    for j in range(len(name)): # nameをスプリットするためのループ
      name_str = name[:j+1]
      firstname_list.append(name_str)

    for k in search_order:
      if len(name) < k: # 苗字がdatasetの中にない場合の処理
        result_last.append(name)
        result_first.append("エラー")
        break

      if len(name) >= 3:
        data_serch = dictionary.loc[dictionary["firstname"] == firstname_list[k - 1]]
      else:
        data_serch = dictionary.loc[dictionary["firstname"] == firstname_list[0]] # 名前が2文字の場合に苗字が1文字確定なため1文字だけ検索
        #lastnameの部分の処理
        result_last.append(firstname_list[0])
        #firstnameの部分の処理
        name_reverse = name[1:]
        result_first.append(name_reverse)
        break

      if len(data_serch) != 0:
        #lastnameの部分の処理
        result_last.append(data_serch.iloc[0, 0])

        #firstnameの部分の処理
        name_reverse = name[k:]
        result_first.append(name_reverse)
        break
  
  #配列をデータフレームに変換
  """
  result_first = pd.Series(result_first)
  result_last = pd.Series(result_last)
  name_split = pd.DataFrame({'lastname': result_last, 'firstname': result_first})
  """

  files_copy.insert(name_num, "名前", result_first)
  files_copy.insert(name_num, "苗字", result_last)
  files_copy = files_copy.drop(columns = files_copy.columns[[name_num + 2]])

  files_copy.to_csv("./output/output.csv", header=False, index=False, encoding='utf_8_sig')

  return files_copy