# filter a list of items to contain only one instance of each item
from geopy import distance


items = [1, 2, 3, 4, 5, 6, 6, 2, 3, 4, 5,]

def simple_filter_list_items(items, match):
    print([item for item in items if item == match])


tel_aviv = {'location': (32.068371,34.793917)}

cities = [{'name':'Beijing', 'location': (39.923674,116.335601)}, 
{'name':'New York', 'location': (40.690772, -73.944034)}, 
{'name': 'san_francisco', 'location': (37.756857, -122.434857)}]

def print_distance_between_cities(cities):
    for city in cities:
        print(city['name'])
        print(distance.distance(tel_aviv['location'], city['location']).km)


def print_cities_closer_than_10km_to_tel_aviv(cities):
    close_cities = [items for items in cities if distance.distance(tel_aviv['location'], items['location']).km < 10000]
    for item in close_cities:
        print(item['name'])


if __name__ == '__main__':
    print('*** printing all items from the list that == 2 ***')
    simple_filter_list_items(items, 2)
    print('*** printing distances between cities and Tel Aviv ***')
    print_distance_between_cities(cities)
    print('*** printing cities closer than 10,000km to Tel Aviv ***')
    print_cities_closer_than_10km_to_tel_aviv(cities)
