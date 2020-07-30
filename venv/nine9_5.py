from _collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

# favorite_languages = {
#     'jen':"python",
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python',}

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " +
          language.title() + ".")