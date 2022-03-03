import pdfplumber

with pdfplumber.open("toa.pdf") as pdf:
    first_page = pdf.pages[0]
    for idx, page in enumerate(pdf.pages):
        print(f"-----page:{idx}")
        if page.annots:
            for annot in page.annots:
                if "title" in annot and annot['title']:
                    print(f"title:{annot['title']}")
                    if "data" in annot and annot['data']:
                        if 'FT' in annot['data']:
                            print(f"FT:{annot['data']['FT']}")
                        # if 'T' in annot['data']:
                        #     print(f"T:{annot['data']['T']}")
                        if 'V' in annot['data']:
                            print(f"V:{annot['data']['V']}")
