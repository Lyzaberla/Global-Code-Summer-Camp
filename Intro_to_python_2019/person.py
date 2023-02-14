print('welcome, let us get interactive')
def get_name():
    name =input('what is your name?')
    return name
def get_age():
    age =int(input('how old are you?'))
    return age
def main():
    print('Hello',get_name(), 'I know you are', get_age(), 'years old.')
    print('nice to meet you')

main()


