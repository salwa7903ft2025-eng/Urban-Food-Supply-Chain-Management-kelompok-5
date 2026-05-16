#ntar gw lanjut :v
def insert(q, d):
    q.append(d)

def delete(q):
    try:
        m = 0
        for i in range(len(q)):
            if q[i] > q[m]:
                m = i
        item = q[m]
        del q[m]
        return item
    except IndexError:
        print("Queue empty.")
        exit()

def is_empty(q):
    return len(q) == 0

if __name__ == '__main__':
    q = []

    insert(q, 12)
    insert(q, 1)
    insert(q, 14)
    insert(q, 7)

    print(q)
    print("Removed elements:")
    while not is_empty(q):
        print(delete(q))
