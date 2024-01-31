def item_occurance_counter(list):
    count_dict = {}
    for i in list:
        count_dict[i] = list.count(i)
    return count_dict


def main():
    input_list = input(
        "Please enter a comma(,) seperated list(E.g item1,item2): ").split(",")
    print(item_occurance_counter(input_list))


if __name__ == "__main__":
    main()
