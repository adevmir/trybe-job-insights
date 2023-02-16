from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    list_jobs = []
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file)
        for job in jobs_reader:
            list_jobs.append(job)
        return list_jobs
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_types = []
    for job in jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return(job_types)
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
