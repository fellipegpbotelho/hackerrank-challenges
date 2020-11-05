from typing import Dict, List


def get_student_marks() -> List[float]:
    n = int(input())

    student_marks: Dict[str, List[float]] = {}
    for _ in range(n):
        name, *line = input().split()
        student_marks[name] = list(map(float, line))

    query_name: str = input().strip()
    return student_marks[query_name]


def calculate_student_average(marks: List[float]) -> str:
    average: float = sum(marks) / len(marks)
    return '{:.2f}'.format(average)


def main() -> None:
    marks = get_student_marks()
    average = calculate_student_average(marks)
    print(average)


if __name__ == '__main__':
    main()