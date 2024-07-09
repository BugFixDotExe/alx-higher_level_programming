#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""A Python Script fetches the recent contributor to a repo"""
if __name__ == "__main__":
    import requests
    import sys

    try:
        url = "https://api.github.com/repos/{}/{}/commits".format(
                sys.argv[2], sys.argv[1])
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "per_page": "10"
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            to_json = response.json()
            for commit in to_json:
                sha = commit.get("sha")
                author_name = commit.get(
                        "commit", {}).get("author", {}).get("name")
                print(f"{sha}: {author_name}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except ValueError as e:
        print(e)
