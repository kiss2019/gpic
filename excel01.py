from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import  Pt #磅数
from docx.oxml.ns import qn #中文格式
import  time

price=input('请输入今日价格')
company_list=['佟丽娅'，'汪小敏'，''，'客户4'，'客户'，'客户1'，'客户1'，]