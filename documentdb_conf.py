# -*- coding: utf-8 -*-
import boto3
import base64
import json
from pymongo import MongoClient


##### AWS Secret Manager Start #########
########### DccumentDB ####################
def read_secrets_manager(secret_name, region_name):
    #secret_name = "dev/docdb/talentmatcher"
    #region_name = "us-east-1"
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager', region_name=region_name)
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
    else:
        secret = base64.b64decode(get_secret_value_response['SecretBinary'])
    secret_var = json.loads(secret)
    return secret_var


##### AWS Secret Manager Start #########

if __name__ == "__main__":
    REGION_NAME = "us-east-1"
    DOCDB_SECRET_NAME = 'dev/docdb/job_title_normalizer'

    USE_DOCUMENTDB = False
    AUTH_MECH = 'SCRAM-SHA-256'
    MERGED_TITLES_COLLECTION = "merged_titles"
    CA_CERT_FILE = '/home/dev_job_title_norm/global-bundle.pem'

    if USE_DOCUMENTDB:
        # docdb_secret_var = read_secrets_manager(DOCDB_SECRET_NAME, REGION_NAME)

        MONGODB_HOST = "tz-dev-docdb.cluster-cwgf4xjyujk9.us-east-1.docdb.amazonaws.com"
        MONGODB_PORT = "27017"
        MONGODB_AUTHDB = "data_consolidation"
        MONGODB_USER = "dev_admin_usr"
        MONGODB_PWD = "##KsdjKKLkds*343"
        DATA_CONSOLIDATION_DB_NAME = "data_consolidation"
        SSL = True
        SSL_CA_CERTS = CA_CERT_FILE
    else:
        # DB Details
        MONGODB_HOST = "localhost"
        MONGODB_PORT = 27017
        DATA_CONSOLIDATION_DB_NAME = "data_consolidation"
        pass

    if USE_DOCUMENTDB:
        client = MongoClient(
            MONGODB_HOST,
            MONGODB_PORT,
            username=MONGODB_USER,
            password=MONGODB_PWD,
            authSource=MONGODB_AUTHDB,
            authMechanism=AUTH_MECH,
            ssl=True,
            ssl_ca_certs=CA_CERT_FILE)
    else:
        client = MongoClient(MONGODB_HOST, MONGODB_PORT)

    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        print('successfully connected to DB master')
    except Exception as ex:
        print('Error during connection: ' + str(ex))
