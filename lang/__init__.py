# fileName : lang/__init__.py
# copyright Β©οΈ 2021 nabilanavab

from configs.config import settings

langList = {
        "eng" : ["π΄π½πΆπ»πΈππ·", "English"]
    }

# Display Lang in a Beutiful Way
async def disLang(lang):
    if lang in langList:
        return langList[lang][0]
    else:
        return langList[settings.DEFAULT_LANG][0]

# ===================================================================================================================================[NABIL A NAVAB -> TG: nabilanavab]
