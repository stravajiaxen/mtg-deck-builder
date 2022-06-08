# I want to make some simple readme files for each problem, but I hate
# writing readmes. Luckily, most problems on PE have a similar structure. I can probably
# get away with automatically making the readme if I do some clever stuff with
# beautiful soup.

import requests
from bs4 import BeautifulSoup
import shutil
import os

solution_out = \
'''
"""
Copyright Matt DeMartino (Stravajiaxen)
Licensed under MIT License -- do whatever you want with this, just don't sue me!

This code attempts to solve Project Euler (projecteuler.net) Problem #{problem_num} {problem_title}

{description}
"""
import time


def main():
    pass
    
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print("Elapsed Time: ", elapsed_time)
'''

problem_out = \
"""
# Euler {problem_num}: {problem_title}

## Description
{description}

## Solution
*Fill me in!*
"""

def problem_num(num, write=False):
    # Make a BeautifulSoup from the contents of project euler's page
    url_template = "https://projecteuler.net/problem={num}"
    url = url_template.format(num=num)
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")

    # Title is the first h2
    problem_title = soup.find_all("h2")[0].get_text()

    # Problem description is in the div marked as "problem
    problem_desc = soup.find(role="problem")
    descriptions = []
    for paragraph in problem_desc.find_all("p"):
        descriptions.append(paragraph.get_text())
    description = "\n\n".join(descriptions)

    text = problem_out.format(problem_num=num, problem_title=problem_title,
                              description=description)

    if not write:
        print(solution_out.format(problem_num=num, problem_title=problem_title,
                                        description=description))
        return text
    else:
        dir_loc = os.path.join(os.path.dirname(__file__), "..", "p" + str(num))
        print(dir_loc)
        os.mkdir(dir_loc)

        with open(os.path.join(dir_loc, "README.md"), 'w') as f:
            f.write(text.encode('ascii', 'ignore').decode())

        with open(os.path.join(dir_loc, "euler" + str(num) + ".py"), 'w') as f:
            f.write(solution_out.format(problem_num=num, problem_title=problem_title,
                                        description=description
                                        ).encode('ascii', 'ignore').decode())

        return text


if __name__ == '__main__':
    readme = problem_num(27, write=True)
    print(readme)