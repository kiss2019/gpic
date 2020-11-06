from docxtpl import DocxTemplate ,RichText
tpl=DocxTemplate('model.docx')

rt = RichText('an exemple of ')
rt.add('a rich text', style='myrichtextstyle')
rt.add('some violet', color='#ff00ff',size=40)
rt.add('\n我是谁')

content={
    'rt':rt,
    'user':'刘德华',
    'user2':'倪妮',
    'address':'西湖',
    'time':'2008年8月8日'
}

tpl.render(content)
tpl.save('002.docx')