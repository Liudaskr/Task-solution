from typing import List


def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]
) -> int:
    sorted_list = sorted(cities_with_train_station)
    extended_list = [-sorted_list[0]] + sorted_list + [2*(number_of_cities-1)-sorted_list[-1]]
    return max([(extended_list[i+1]-extended_list[i])//2 for i in range(len(extended_list)-1)])


if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (
        find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    )
    print("ALL TESTS PASSED")