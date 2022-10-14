from view import *


def main():
    for page in range(1, get_page()+1):
        url = f'{BASE_URL}?page={str(page)}'
        html = get_html(BASE_URL)
        soup = get_soup(html)
        get_data(soup)
        print(f'Спарсили {page} страницу')


if __name__ == '__main__':
    main()
