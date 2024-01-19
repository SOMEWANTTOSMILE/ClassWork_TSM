def hide():
    srting_ = "pivo@gmail.com"
    split_mail = str(srting_).split('@')
    a = split_mail[0][2]
    b = split_mail[1]
    print(a, 'split', b)


print(hide())