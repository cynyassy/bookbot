def get_num_words(text: str) -> int:
    # split on whitespace and count the tokens
    return len(text.split())

def counting_characters(text: str) -> dict:
    text = text.lower()
    character_count ={}
    for char in text:
        if char in character_count:
            character_count[char]+=1
        else:
            character_count[char]=1
    return character_count

def sorted_characters(character_count: dict) -> list[dict]:
    # convert dictionary into a list of dicts
    characters_list = []
    for char, count in character_count.items():
        if char.isalpha():   # only include letters
            characters_list.append({"char": char, "num": count})

    # define helper function for sorting by 'num'
    def sort_on(item):
        return item["num"]

    # sort list of dicts by 'num' descending
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list
