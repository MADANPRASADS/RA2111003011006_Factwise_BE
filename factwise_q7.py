def Score(Points,k):
    n = len(Points)
    current_sum = sum(Points[:k])
    max_sum =current_sum
    for i in range(k-1,-1,-1):
        current_sum += Points[n-(k-i)]-Points[i]
        max_sum = max(max_sum, current_sum)
    return max_sum
def get_input():
    Points = input("Enter values:").strip().split()
    Points = list(map(int, Points))
    k =int(input("Value of k:"))
    return Points, k
def main():
    Points, k = get_input()
    max_score = Score(Points,k)
    print(max_score)
if __name__ == "__main__":
    main()