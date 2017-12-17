import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes. decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)
#怎么说呢，可能每句话都能看懂在做什么，但是给我写，我一个字也写不出来。。主要应该还是没学过script里面的这些函数
#有一点跟已经学的东西有差距，open("language.txt", encoding = "utf-8")，看这句话，以前都是open(file_name,'w')这样的，但是这篇script里面有多处带error和encoding的，不是很懂
