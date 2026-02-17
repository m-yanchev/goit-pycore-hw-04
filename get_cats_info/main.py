def get_cats_info(path: str) -> list | None:

    cats_info = []

    cat_list = read_cat_list(path)
    if cat_list is None:
        return None

    for cat_str in cat_list:
        cat_dict = get_cat_dict(cat_str)
        if cat_dict is not None:
            cats_info.append(cat_dict)

    return cats_info


def read_cat_list(path: str) -> list | None:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cat_str = file.readlines()
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None
    else:
        # remove leading and trailing whitespace characters
        return [line.strip() for line in cat_str]


def get_cat_dict(cat_str: str) -> dict | None:

    cat_info = cat_str.split(',')
    if len(cat_info) != 3:
        print(f"У рядку {cat_str} є зайві дані: "
              f"{cat_info[3:]}. Вони будуть проігноровані.")
    id = cat_info[0].strip()
    name = cat_info[1].strip().capitalize()
    age = cat_info[2].strip()

    if not is_id(id):
        print(f"Некоректний формат id: {id}. "
              f"Він повинен бути шістнадцятковим числом.")
        return None
    elif not is_name(name):
        print(f"Некоректний формат імені: {name}. "
              f"Ім'я не може бути порожнім.")
        return None
    elif not is_age(age):
        print(f"Некоректний формат віку: {age}. "
              f"Вік повинен бути невід'ємним цілим числом.")
        return None
    else:
        return {'id': id.strip(), 'name': name.strip(), 'age': age.strip()}


def is_id(id: str) -> bool:
    try:
        int(id, 16)
        return True
    except ValueError:
        return False


def is_name(name: str) -> bool:
    return bool(name)


def is_age(age: str) -> bool:
    return age.isdigit() and int(age) >= 0


cats_info = get_cats_info("get_cats_info/cats_file.txt")
print(cats_info)
