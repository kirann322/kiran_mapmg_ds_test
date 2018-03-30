pip install virtualenv
virtualenv my-project-env
cd my-project-env/
source bin/activate
pip install pandas
pip show pandas
cd ../
python mapmg_ds_test.py
deactivate
