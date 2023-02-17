from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salary = 0
    for job in jobs:
        if job["max_salary"] != "" and \
                job["max_salary"] != "invalid" and \
                max_salary < int(job["max_salary"]):
            max_salary = int(job["max_salary"])
    return(int(max_salary))
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    jobs = read(path)
    min_salary = 9999999999999999999
    for job in jobs:
        if job["min_salary"] != "" and \
                job["min_salary"] != 'invalid' and \
                min_salary > int(job["min_salary"]):
            min_salary = int(job["min_salary"])
    print(min_salary)
    return(int(min_salary))
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    print(job, salary)
    if not "max_salary" in job \
            or not "min_salary" in job:
        raise ValueError
    max_salary = job["max_salary"]
    min_salary = job["min_salary"]
    if type(max_salary) == str:
        max_salary = int(max_salary)
    if type(min_salary) == str:
        min_salary = int(min_salary)
    if type(salary) == str:
        salary = int(salary)
    if type(max_salary) != int \
            or type(min_salary) != int \
            or type(salary) != int:
        raise ValueError
    if min_salary > max_salary:
        raise ValueError
    return max_salary >= salary >= min_salary
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
