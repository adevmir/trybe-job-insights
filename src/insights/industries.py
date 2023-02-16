from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    industries = []
    for job in jobs:
        if job["industry"] != '' and job["industry"] not in industries:
            industries.append(job["industry"])
    print(industries)
    return(industries)
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_industry_filter = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_industry_filter.append(job)
    return(jobs_industry_filter)
    raise NotImplementedError
