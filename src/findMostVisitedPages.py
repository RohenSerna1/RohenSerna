def findMostVisitedPages(logData):
    from collections import defaultdict

    url_visitors = defaultdict(set)

    for i in logData:
        url = i["url"]
        user_id = i["userId"]
        url_visitors[url].add(user_id)

    sorted_urls = sorted(url_visitors.items(), key=lambda x: len(x[1]), reverse = True)
    return [url for url, _ in sorted_urls]

logData = [
    {"url": "/home", "userId": "A"},
    {"url": "/about", "userId": "B"},
    {"url": "/products", "userId": "A"},
    {"url": "/home", "userId": "C"},
    {"url": "/contact", "userId": "B"},
    {"url": "/products", "userId": "D"},
    {"url": "/home", "userId": "A"},
    {"url": "/home", "userId": "B"},
    {"url": "/products", "userId": "A"}
]

print(f"The most visited page is: {findMostVisitedPages(logData)}")


