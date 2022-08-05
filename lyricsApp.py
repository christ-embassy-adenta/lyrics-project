import flet
from flet import Page, Image, TextField, icons, colors, Row, Column, Container, border, Icon, Stack, alignment, Text
from lyrics import lyrics

logo = Image(
    src=f"/images/logo.png",
    width=100,
    height=100,
    fit="contain",
)

title_search = TextField(hint_text='Enter title', expand=True,
                         border='none')
name_search = TextField(hint_text='Enter title', expand=True,
                        border='none')
title = Container(height=60, width=300, border_radius=5, border=border.all(1, colors.YELLOW_700), padding=5,
                  content=title_search)
name = Container(height=60, width=300, border_radius=5, border=border.all(1, colors.YELLOW_700), padding=5,
                 content=name_search)

search_container = Row(spacing=10, controls=[title, name])


def main(page: Page):
    page.theme_mode = 'dark'
    page.window_max_width = True
    page.scroll = True
    page.padding = 0
    page.horizontal_alignment = 'center'
    page.title = 'Blw Lyrics App'

    def get_lyrics(e):
        text.value = f"Searching for '{title_search.value}' by '{name_search.value}..."
        page.update()
        text.value = lyrics(title_search.value, name_search.value)
        title_search.value = ''
        name_search.value = ''
        page.update()

    search_button = Container(height=40, width=100, border_radius=5,
                              content=Row(
                                  controls=[Icon(name=icons.SEARCH, color=colors.YELLOW_700), Text(value='Search')]),
                              padding=5,
                              border=border.all(1, colors.YELLOW_700),
                              on_click=get_lyrics)

    header = Container(content=Column(width=700, controls=[logo, Column(controls=[search_container, search_button],
                                                                        horizontal_alignment='center')],
                                      horizontal_alignment='center', ), alignment=alignment.center)
    view_stack = Stack([
        Container(width=page.window_width,
                  content=Image(
                      src=f"/images/banner-2.jpg",
                      width=1000,
                      height=300,
                      fit="fitWidth",

                  )),
        header

    ], height=400)

    text = Text(
        value='lyric', selectable=True)

    column_text = Column(width=800, controls=[
                         text], horizontal_alignment='center')

    page.add(view_stack, column_text)


if __name__ == '__main__':
    flet.app(target=main, assets_dir="assets")
