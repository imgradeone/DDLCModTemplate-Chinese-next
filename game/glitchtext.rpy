# Glitchtext.rpy - 乱码文字

# 这里定义 DDLC 中显示的无意义乱码文字。

# 如果你乐意的话，你也可以修改这一部分，实现中文内容 / 奇怪的整活。

# 您也可以定义乱码文字的长度。
init python:
    import random

    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    # length 为乱码文字的长度，调用时使用如 glitchtext(60) 即可
    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output

