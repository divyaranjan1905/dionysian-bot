import os
import random
from PIL import Image
from utils.captcha.assets.emojis_map import emojis_index

def make_captcha(id: str):
    background = Image.open('utils/captcha/assets/background.png')
    paste_image_list = list()
    emoji_names = list()
    supported_emojis = ['🃏', '🎤', '🎥', '🎨', '🎩', '🎬', '🎭', '🎮', '🎯', '🎱', '🎲', '🎷', '🎸', '🎹', '🎾', '🏀', '🏆', '🏈', '🏉', '🏐', '🏓', '💠', '💡', '💣', '💨', '💸', '💻', '💾', '💿', '📈', '📉', '📊', '📌', '📍', '📎', '📏', '📐', '📞', '📟', '📠', '📡', '📢', '📣', '📦', '📹', '📺', '📻', '📼', '📽', '🖥', '🖨', '🖲', '🗂', '🗃', '🗄', '🗜', '🗝', '🗡', '🚧', '🚨', '🛒', '🛠', '🛢', '🧀', '🌭', '🌮', '🌯', '🌺', '🌻', '🌼', '🌽', '🌾', '🌿', '🍊', '🍋', '🍌', '🍍', '🍎', '🍏', '🍚', '🍛', '🍜', '🍝', '🍞', '🍟', '🍪', '🍫', '🍬', '🍭', '🍮', '🍯', '🍺', '🍻', '🍼', '🍽', '🍾', '🍿', '🎊', '🎋', '🎍', '🎏', '🎚', '🎛', '🎞', '🐌', '🐍', '🐎', '🐚', '🐛', '🐝', '🐞', '🐟', '🐬', '🐭', '🐮', '🐯', '🐻', '🐼', '🐿', '👛', '👜', '👝', '👞', '👟', '💊', '💋', '💍', '💎', '🔋', '🔌', '🔪', '🔫', '🔬', '🔭', '🔮', '🕯', '🖊', '🖋', '🖌', '🖍', '🥚', '🥛', '🥜', '🥝', '🥞', '🦊', '🦋', '🦌', '🦍', '🦎', '🦏', '🌀', '🌂', '🌑', '🌕', '🌡', '🌤', '⛅️', '🌦', '🌧', '🌨', '🌩', '🌰', '🌱', '🌲', '🌳', '🌴', '🌵', '🌶', '🌷', '🌸', '🌹', '🍀', '🍁', '🍂', '🍃', '🍄', '🍅', '🍆', '🍇', '🍈', '🍉', '🍐', '🍑', '🍒', '🍓', '🍔', '🍕', '🍖', '🍗', '🍘', '🍙', '🍠', '🍡', '🍢', '🍣', '🍤', '🍥', '🍦', '🍧', '🍨', '🍩', '🍰', '🍱', '🍲', '🍴', '🍵', '🍶', '🍷', '🍸', '🍹', '🎀', '🎁', '🎂', '🎃', '🎄', '🎈', '🎉', '🎒', '🎓', '🎙', '🐀', '🐁', '🐂', '🐃', '🐄', '🐅', '🐆', '🐇', '🐕', '🐉', '🐓', '🐖', '🐗', '🐘', '🐙', '🐠', '🐡', '🐢', '🐣', '🐤', '🐥', '🐦', '🐧', '🐨', '🐩', '🐰', '🐱', '🐴', '🐵', '🐶', '🐷', '🐸', '🐹', '👁\u200d🗨', '👑', '👒', '👠', '👡', '👢', '💄', '💈', '🔗', '🔥', '🔦', '🔧', '🔨', '🔩', '🔰', '🔱', '🕰', '🕶', '🕹', '🖇', '🚀', '🤖', '🥀', '🥁', '🥂', '🥃', '🥐', '🥑', '🥒', '🥓', '🥔', '🥕', '🥖', '🥗', '🥘', '🥙', '🦀', '🦁', '🦂', '🦃', '🦄', '🦅', '🦆', '🦇', '🦈', '🦉', '🦐', '🦑', '⭐️', '⏰', '⏲', '⚠️', '⚡️', '⚰️', '⚽️', '⚾️', '⛄️', '⛅️', '⛈', '⛏', '⛓', '⌚️', '☎️', '⚜️', '✏️', '⌨️', '☁️', '☃️', '☄️', '☕️', '☘️', '☠️', '♨️', '⚒', '⚔️', '⚙️', '✈️', '✉️', '✒️']
    r = random.random()
    random.shuffle(supported_emojis, lambda: r)
    r = random.random()
    random.shuffle(supported_emojis, lambda: r)
    for i in range(6):
        emoji_names.append(supported_emojis[i])
        paste_image_list.append(Image.open(f"utils/captcha/assets/emojis/{emojis_index.get(f'{supported_emojis[i]}')}.png"))
    position = [(20, 20), (180, 20), (310, 20), (20, 160), (180, 160), (310, 160)]
    for i in range(len(paste_image_list)):
        img = paste_image_list[i].rotate(random.randint(0, 360), resample=Image.BICUBIC, expand=True)
        img.thumbnail((200, 200), Image.ANTIALIAS)
        background.paste(img, (position[i]), img)
    background.save(f"utils/captcha/cache/{id}.png", "PNG", quality=100)
    captcha_answer = "Answer:"
    for i in range(len(emoji_names)):
        captcha_answer += f" {emoji_names[i]}"
    return captcha_answer, f"utils/captcha/cache/{id}.png"
