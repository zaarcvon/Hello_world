a=pd.concat([df1,df2])  #соединяю две таблицы просто подставляя одну вниз другой
a.fillna('Empty field', inplace=True)   #заполняю Nan чтобы потом не было проблем со сравнением значений 
for name,table in a.groupby('Name'): #группирую все строки таблицы по полю Namе и получаю кучу маленьких табличек состоящих из двух строк
                                      #для одного человека из исходных таблиц
    for column in table.columns:
        if len(table[column])==2:  ##если в получившейся микротабличке строк две (то есть человек был в двух таблицах)
            if table[column].iloc[0]!=table[column].iloc[1]:   # сравниваю для каждой колонки значение у этого человека, если они разные то вывожу их на экран
                print('Difference for ',name,' in ', column,', values are',  table[column].iloc[0],table[column].iloc[1])
