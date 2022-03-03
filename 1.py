import pdfplumber

with pdfplumber.open("toa.pdf") as pdf:
    for idx, page in enumerate(pdf.pages):
        if idx == 0:
            continue
        print(f"-----page:{idx}")
        if page.annots:
            for annot in page.annots:
                if "title" in annot and annot['title']:
                    print(f"title:{annot['title']}")
                    if "data" in annot and annot['data']:
                        if 'FT' in annot['data']:
                            print(f"FT:{annot['data']['FT']}")
                        if 'CA' in annot['data']:
                            print(f"CA:{annot['data']['CA']}")
                        # if 'T' in annot['data']:
                        #     print(f"T:{annot['data']['T']}")
                        if 'V' in annot['data']:
                            print(f"V:{annot['data']['V']}")
