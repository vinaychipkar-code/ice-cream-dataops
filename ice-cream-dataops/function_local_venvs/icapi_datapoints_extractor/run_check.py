import os
import sys

from pathlib import Path
from pprint import pprint

from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials

# This is necessary to import adjacent modules in the function code.
sys.path.insert(0, str(Path(__file__).parent / "local_code"))

from local_code.handler import handle # noqa: E402

try:
    from dotenv import load_dotenv

    for parent in Path(__file__).resolve().parents:
        if (parent / ".env").exists():
            load_dotenv(parent / '.env')
except ImportError:
    ...


def main() -> None:
    credentials = OAuthClientCredentials(
        token_url="https://login.microsoftonline.com/923486cb-1d5b-48ea-832b-05bd4c6123ae/oauth2/v2.0/token",
        client_id="95857a30-1a9f-4675-a0b4-83ca958634eb",
        client_secret=os.environ["ICAPI_EXTRACTORS_CLIENT_SECRET"],
        scopes=['https://bluefield.cognitedata.com/.default'],
    )

    client = CogniteClient(
        config=ClientConfig(
            client_name="CDF-Toolkit:0.6.53",
            project="vinay-project",
            base_url="https://bluefield.cognitedata.com",
            credentials=credentials,
        )
    )

    print("icapi_datapoints_extractor LOGS:")
    response = handle(
        client=client,
        data={'hours': 1},
    )

    print("icapi_datapoints_extractor RESPONSE:")
    pprint(response)


if __name__ == "__main__":
    main()
