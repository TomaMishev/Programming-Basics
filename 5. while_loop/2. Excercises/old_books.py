favorite_book = input()
searched_book = input()
book_counter = 0
is_found = False
while searched_book != "No More Books":

    if searched_book == favorite_book:
        is_found = True
        break
    book_counter += 1

    searched_book = input()

if is_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_counter} books.")
