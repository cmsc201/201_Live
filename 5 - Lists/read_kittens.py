if __name__ == '__main__':
    with open("kitten_names.txt", 'r') as f:
        all_kittens = f.readlines();
    print(all_kittens)
    for kitten in all_kittens:
        print(kitten.strip() + " is soooo awesome")