def sjf(jobs: list, index:int):
    job_item = jobs[index]
    sjf_list = []
    for job in jobs[index+1:]:
        if job < job_item:
            sjf_list.append(job)

    return sum(sjf_list) + sum(jobs[:index+1])



print(sjf([10,10,10,10],3))