from src.pre_built.counter import count_ocurrences


SALARY_COUNTER = 598


def test_counter():
    assert count_ocurrences("data/jobs.csv", "salary") == SALARY_COUNTER
