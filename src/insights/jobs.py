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
    jobs_filter = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filter.append(job)
    return(jobs_filter)
    raise NotImplementedError
