import fitz
from tqdm import tqdm


def pdf2html(pdf_path, html_path):
    doc = fitz.open(pdf_path)
    for page in tqdm(doc):
        html_content = page.getText('html')
    print("开始输出html文件")
    with open(html_path, 'w', encoding='utf8', newline="") as fp:
        fp.write(html_content)


input_path = r'toa.pdf'  # 如果报错 就用绝对路径
html_path = r'toa.html'
pdf2html(input_path, html_path)
