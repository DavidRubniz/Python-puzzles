from functools import reduce
inventory = [
    {'id': 101, 'name': 'Classic T-Shirt', 'price': 25, 'category': 'Apparel'},
    {'id': 102, 'name': 'Leather Wallet', 'price': 50, 'category': 'Accessories'},
    {'id': 103, 'name': 'Bluetooth Headphones', 'price': 150, 'category': 'Electronics'},
    {'id': 104, 'name': 'Coffee Mug', 'price': 15, 'category': 'Homeware'},
    {'id': 105, 'name': 'Running Shoes', 'price': 80, 'category': 'Apparel'},
    {'id': 106, 'name': 'Smartphone', 'price': 700, 'category': 'Electronics'}
]
lambda1 = lambda x: x['category'] == 'Apparel'
lst = list(filter(lambda1, inventory))

lambda2 = lambda x: x['name']
print(list(map(lambda2, inventory)))
print(list(map(lambda x: x, filter(lambda x: x['price'] > 100, inventory))))
print(sorted(inventory, key=lambda x: x['price']))
print(any(list(map(lambda x:x['category'] == 'Homeware', inventory))))
print(all(list(map(lambda x: x['price'] > 10, inventory))))
print(sorted(list(map(lambda x: x['name'], list(filter(lambda x:x['category']=='Apparel', inventory))))))
print(reduce(lambda x,y:x+y, list(map(lambda x:x['price'], list(filter(lambda x:x['category']=='Electronics', inventory))))))

student_data = [
    {'name': 'Alice', 'grades': [
        {'subject': 'Math', 'score': 90},
        {'subject': 'History', 'score': 85},
        {'subject': 'Physics', 'score': 92}
    ]},
    {'name': 'Bob', 'grades': [
        {'subject': 'Math', 'score': 78},
        {'subject': 'History', 'score': 95},
        {'subject': 'Physics', 'score': 88}
    ]},
    {'name': 'Charlie', 'grades': [
        {'subject': 'Math', 'score': 82},
        {'subject': 'History', 'score': 79},
        {'subject': 'Physics', 'score': 85}
    ]},
    {'name': 'David', 'grades': [
        {'subject': 'Math', 'score': 95},
        {'subject': 'History', 'score': 91},
        {'subject': 'Physics', 'score': 89}
    ]}
]


print(list(map(lambda s: s['name'], filter(lambda s: any(map(lambda g: g['score'] > 90, s['grades'])) and
                                (sum(map(lambda g: g['score'], s['grades'])) / len(s['grades'])) < 88, student_data))))