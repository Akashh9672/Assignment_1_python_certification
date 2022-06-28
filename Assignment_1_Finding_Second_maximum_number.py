if __name__ == '__main__':
    n = int(input())
    list = map(int, input().split())
    print(sorted(set(list), reverse=True)[1])