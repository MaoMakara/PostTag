# -*- coding: utf-8 -*- 
Nouns={'របាយការណ៍', 'នេះ','ក៏','បាន','បង្ហាញ','ពី','ហានិភ័យ', 'ប្រឈម', 'ចំពោះ', 'សេដ្ឋកិច្ច'}
def POS_tag(Pos):
    lResult = []
    Pos_Tag = []
    for Word_tData in Pos:
        if Word_tData in Nouns:
            lResult.append(Word_tData)
            lResult.append('នាម')
            Pos_Tag.append(tuple(lResult))
            lResult = []
        
    return(Pos_Tag)


text=['ក្នុង', 'របាយការណ៍', 'នេះ','ក៏','បាន','បង្ហាញ','ពី','ហានិភ័យ', 'ប្រឈម', 'ចំពោះ', 'សេដ្ឋកិច្ច']
s=POS_tag(text)
print(s)
