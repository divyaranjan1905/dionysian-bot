def make_captcha_markup(markup, __emoji, indicator):
    __markup = markup
    for i in markup:
        for k in i:
            if k["text"] == __emoji:
                k["text"] = f"{indicator}"
                k["callback_data"] = "Hehe"
                return __markup
