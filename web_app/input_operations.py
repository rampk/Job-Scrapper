def validate_website(websites):
    if not len(websites):
        return "indeed"
    else:
        return " ".join(websites)


def process_inputs(job_title, job_location, job_websites):
    job_title = job_title[0]
    job_title = job_title.replace(' ', '-')
    job_location = job_location[0]
    job_websites = validate_website(job_websites)
    return job_title, job_location, job_websites
