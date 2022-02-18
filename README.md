# CUR Extractor Application

This repository aims to help sanitize the Cost and Usage Reports (CUR) generated by AWS.
This CUR Extractor uses Django as its web framework, served by NGINX and uWSGI.

## Setting up the environment:

* Clone the repository

```
git clone git@github.com:grumatic/cur_extractor_admin.git
```

* Go to the cloned repository's directory

* Create your `.env` file
    (use the existing `.env-SAMPLE` file as template)
    * DJANGO_SUPERUSER_\* - is used for setting up the default django admin
    * SECRET_KEY - is used by Django for it crypto signing, should be random and unique
    * MONGO_NAME - the mongo container name used to connect django to the DB
    * CELERY_BROKER_URL - the redis url (using container name)

    * STS_ACCESS_KEY_ID - access key id from user with STS:AssumeRole permissions
    * STS_SECRET_ACCESS_KEY - secret access key from user with STS:AssumeRole permissions
    * EXTERNAL_ID - external_id from role creation (trusted entity)

* Change any desired Configs in `src/cur_extractor/Config/Config.py`
    * BEAT_\* - Used by celery to schedule task runs (default is at minue 00 every hour)
    * DOWNLOAD_PATH - will be the temporary path for the CUR data (deleted after every task if `NEED_REMOVE_TEMP` is `True`)
    * DEFAULT_PREFIX - default prefix added to the S3 object key
    * NEED_REMOVE_TEMP - whether the `DOWNLOAD_PATH` is supposed to be deleted afte the task is ran
    * CHUNK_SIZE - the size of chunks analyzed. (bigger chunk sizes need more memory)

* Build through docker-compose

``` development using "runserver"
docker-compose up --build
```

``` production using uWSGI and NGINX
docker-compose -f docker-compose-prod.yaml up --build
```


## Using the CUR Extractor


* After it's built, navigate to [http://localhost:8000](http://localhost:8000)

* Login with the admin username and password used in the `.env` file.

* You must create (in order):
    * Storage Info
        - The Storage Info ARN's role must have read permission of the bucket selected
        - The original CUR reports will be read from here
    * Payer Acccount
        - The Storage Info you select must be the one which has the account's CUR reports
    * Linked Account (optional)
        - Must be linked with one Payer Account.
        - This account can be use to filter the reports in the Report Info
    * Report Info
        - The Report Info ARN's role must have write permission to the bucket entered
        - The report will be generated according to the Payer account selected.
        - The fields which have its cross box selected, will be included in the report.
        if you wish to remove them, you should unselect their respective cross box.
        - The accounts can be selected for more granular filtering. If no account is selected, all accounts included in the payer account's report will included in the report.
