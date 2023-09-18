# Project Starter

This repository contains the starter code for the **Ensuring Quality Releases** project of the cd1807 Ensuring Quality Releases (Quality Assurance) course taught by Nathan Anderson.

## How to use?

- Fork this repository to your Github account and clone it locally for further development.
- Follow the classroom instructions, and check the rubric before a submission.

## Suggestions and Corrections

Feel free to submit PRs to this repo should you have any proposed changes.

## VM selenium set up

- Install chrome

    ```python
        sudo apt-get update
        sudo apt-get upgrade 

        get https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        udo apt install ./google-chrome-stable_current_amd64.deb -y
    ```

- Install the selenium chrome driver

    ```python
        wget -qP /tmp/ "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.88/linux64/chromedriver-linux64.zip"
        sudo unzip -oj /tmp/chromedriver-linux64.zip -d /usr/bin
        sudo chmod 755 /usr/bin/chromedriver
    ```

## Custom logs forwarding

See Azure documentation: <https://learn.microsoft.com/EN-us/azure/azure-monitor/agents/data-collection-text-log?tabs=portal>
See : <https://www.youtube.com/watch?v=8Vl1BIGXHV0>
