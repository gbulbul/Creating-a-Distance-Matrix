# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:43:34 2024

@author: gbulb
"""

class all_differences_for_each_pair:
    def find_all_differences_for_each_pair(dict_):
        pairs=()
        dict_for_differences_for_each_pair={}
        for key1 in dict_.keys():
            for key2 in dict_.keys():
                if (key2,key1) not in pairs:
                    pairs+=((key1,key2))
                    difference=[]
                    for i in range(len(dict_[key1])):
                        if dict_[key1][i]!=dict_[key2][i]:
                           difference.append(1)
                           dict_for_differences_for_each_pair[(key1,key2)]=sum(difference)
                        elif dict_[key1][i]==dict_[key2][i]:
                           difference==[0]
                           dict_for_differences_for_each_pair[(key1,key2)]=sum(difference)
        return dict_for_differences_for_each_pair
    def obtain_differences_for_each_key_as_a_list(pairs_and_differences,dict_):
        list_for_each_key0,list_for_each_key1,list_for_each_key2,list_for_each_key3=[],[],[],[]
        for key in pairs_and_differences.keys():
            if key[0]==list(dict_.keys())[0]:
                   list_for_each_key0.append(("%.5f" % float(pairs_and_differences[key]*0.1)))
                   
            elif key[0]==list(dict_.keys())[1]:
                   list_for_each_key1.append(("%.5f" % float(pairs_and_differences[key]*0.1)))
                   
            elif key[0]==list(dict_.keys())[2]:
                   list_for_each_key2.append("%.5f" % float(pairs_and_differences[key]*0.1))
                   
            elif key[0]==list(dict_.keys())[3]:
                   list_for_each_key3.append("%.5f" %float(pairs_and_differences[key]*0.1))
        return(list_for_each_key0,list_for_each_key1,list_for_each_key2,list_for_each_key3)
        print(list_for_each_key0)
        print(list_for_each_key1)
        print(list_for_each_key2)
        print(list_for_each_key3)
    def organize_the_output(list_for_each_key0,list_for_each_key1,list_for_each_key2,list_for_each_key3):
        data = {"0": list_for_each_key0,"1": list_for_each_key1,"2":list_for_each_key2,"3":list_for_each_key3} 
        df = pd.DataFrame(data,index=['', '','',''])
        df.columns = df.iloc[0,:].values
        df = df.tail(-1)
        return df
            
if __name__=="__main__":
    import pandas as pd
    dict_={}
    dict_['Rosalind_9499']='TTTCCATTTA'
    dict_['Rosalind_0942']='GATTCATTTC'
    dict_['Rosalind_6568']='TTTCCATTTT'
    dict_['Rosalind_1833']='GTTCCATTTA'
    pairs_and_differences=all_differences_for_each_pair.find_all_differences_for_each_pair(dict_)
    #print(all_differences_for_each_pair.find_all_differences_for_each_pair(dict_))
    list_for_each_key0,list_for_each_key1,list_for_each_key2,list_for_each_key3=all_differences_for_each_pair.obtain_differences_for_each_key_as_a_list(pairs_and_differences,dict_)
    print(all_differences_for_each_pair.organize_the_output(list_for_each_key0,list_for_each_key1,list_for_each_key2,list_for_each_key3))