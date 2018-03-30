# kiran_mapmg_ds_test


The following mapmg_ds_test.py script reads in data from a csv file called fake_data.csv and prints out the doctor id, titles, and names between members and their doctor.

To set up a python environment to run the mapmg_ds_test.py script, follow these steps. This was done on macOS, but could easily be modified for the Windows OS command line interface.

1) Install Python 2.7.14

https://www.python.org/downloads/release/python-2714/

2) Open up a Terminal and navigate into the mapmg_ds_test folder using the following command.

`cd kiran_mapmg_ds_test/`

3) Install package dependencies by running the following command in the terminal.

`bash install_dependencies.sh`

4) If you would like to run the script in a virtual environment, then run the following bash script, otherwise proceed to the next step. This script will create a new virtual environment called my-project-env, activate it, install pandas in it, and run the mapmg_ds_test.py script.

`bash create_virtual_environment.sh`

5) To run the script in the current local environment, skip the last step and run the following command in terminal.

`python mapmg_ds_test.py`

