from combinatorial.visual.theme import Theme
from combinatorial.visual.widget import Widgeter
from combinatorial.visual.window import Window

white_theme = Theme()
black_theme = Theme(back='black', fore='white', aux1='SlateGrey', aux2='red', icon='\U0000263E')

themes: list[Theme] = [white_theme, black_theme]

Widgeter().themes = themes

Window().run()