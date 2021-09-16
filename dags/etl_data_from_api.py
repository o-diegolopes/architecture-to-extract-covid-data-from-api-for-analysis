# airflow related

# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.providers.apache.hdfs.hooks.hdfs import HDFSHook

# others packeges
import json
import requests
import pandas as pd
from datetime import timedelta

default_args = {
    "owner": "Diego Lopes",
    "depends_on_past": False,
    # "start_date": datetime(2020, 1, 23),
    # "email_on_failure": False,
    # "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=3),
    "provide_context": True
}


class Api:
    """
        Returns API data.
    """

    def __init__(self):
        self.__credentials = json.load(open("../credentials.json"))
        self.__api_url = 'http://api.portaldatransparencia.gov.br'
        self.__apis = {
            'movements': 'api-de-dados/coronavirus/movimento-liquido-despesa',
            'transfers': 'api-de-dados/coronavirus/transferencias'
        }
        self.__apis_params_names = {
            'movements': {
                'date': 'mesAnoLancamento',
                'pages': 'pagina'
            },
            'transfers': {
                'date': 'mesAno',
                'pages': 'pagina'
            }
        }

    def request(self, api_name, year_month, pages):
        """
            Returns API response.

                    Parameters:
                        api_name (str): 'movements' or 'transfers'.

                        year_month (str): Year and month. Pattern -> AAAAMM.

                        pages (int): Total pages to request.

                    Returns:
                            API Response.
        """

        api_url = f"{self.__api_url}/{self.__apis.get(api_name)}"
        params = {
            self.__apis_params_names.get(api_name).get('date'): year_month,
            self.__apis_params_names.get(api_name).get('pages'): pages
        }
        headers = {'chave-api-dados': self.__credentials.get('api-key')}

        return requests.get(api_url, params=params, headers=headers)


class ParseApiResponse:

    def __init__(self):
        self.__init__()

    def request_all_api(self):
        self
        return 0
