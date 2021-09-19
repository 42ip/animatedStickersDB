def mdMaker(connections : dict):
    from mdutils.mdutils import MdUtils
    from mdutils import Html
    mdFile = MdUtils(file_name='Stickers',title='All Stickers')
    texts = []
    mdFile.new_line()
    for k,v in connections.items():
        # print(1)
        texts.append(k)
        texts.append(Html.image(path=v))
    mdFile.new_table(text=texts, text_align='center', columns = 2,rows = len(texts) // 2)
    mdFile.create_md_file()
    
