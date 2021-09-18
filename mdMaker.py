def mdMaker(connections : dict):
    from mdutils.mdutils import MdUtils
    from mdutils import Html
    mdFile = MdUtils(file_name='Stickers',title='All Stickers')
    for k,v in connections.items():
        # print(1)
        mdFile.new_header(level=1,title=k)
        mdFile.new_paragraph(Html.image(path=v))
    mdFile.create_md_file()
    
