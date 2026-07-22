#!/usr/bin/env python3
import json
import os.path
import sys
from hashlib import sha1
from http.client import HTTPResponse
from pathlib import Path
from typing import OrderedDict
from urllib.parse import quote
from urllib.request import urlopen


class Puller:
    base_url = "https://chromium-i18n.appspot.com/ssl-address"
    entries = OrderedDict[str, OrderedDict]()

    def pull[T](self, kind: str, *paths: str) -> T:
        pathname = os.path.join(kind, *paths)
        print("Downloading", repr(pathname), file=sys.stderr)
        with urlopen(os.path.join(self.base_url, quote(pathname))) as response:
            response: HTTPResponse
            if response.status != 200:
                raise RuntimeError(f"Unexpected response code {response.status}")
            payload: OrderedDict = json.load(response, object_pairs_hook=OrderedDict)
        if "key" in payload:
            payload.move_to_end("key", last=False)
        payload.move_to_end("id", last=False)
        self.entries[payload["id"]] = payload
        return payload

    def pull_countries(self):
        def pull(*paths: str):
            return self.pull("data", *paths)

        def expand(prefix: str, sub_keys: list[str], suffix: str = ""):
            for key in sub_keys:
                region_data = pull(prefix, key + suffix)
                if "sub_keys" not in region_data:
                    continue
                expand(os.path.join(prefix, key), region_data["sub_keys"].split("~"), suffix)

        manifest = pull()
        for country in manifest["countries"].split("~"):
            country_data = pull(country)
            if "sub_keys" not in country_data:
                continue
            expand(country, country_data["sub_keys"].split("~"))
            if "languages" not in country_data:
                continue
            languages = country_data["languages"].split("~")
            for language in languages[1:]:
                country_data = pull(country + "--" + language)
                expand(country, country_data["sub_keys"].split("~"), "--" + language)

    def pull_examples(self):
        def pull(*paths: str):
            return self.pull("examples", *paths)

        manifest = pull()
        for country in manifest["countries"].split("~"):
            example_data = pull(country)
            for example_type in example_data["types"].split("~"):
                example_type_data = pull(country, example_type)
                for language in example_type_data["languages"].split("~"):
                    pull(country, example_type, language)

    def __iter__(self):
        yield from self.entries.items()


def main(saved_path: Path):
    puller = Puller()
    puller.pull_countries()
    puller.pull_examples()
    content = json.dumps(
        OrderedDict(puller),
        separators=(",", ":"),
        ensure_ascii=False,
    )
    if saved_path.exists() and sha1(saved_path.read_bytes()).hexdigest() == sha1(content.encode("utf-8")).hexdigest():
        print("No changes detected, skipping write to", saved_path)
    else:
        print("Writing to", saved_path)
        saved_path.write_text(content)


if __name__ == "__main__":
    main(Path.cwd() / "i18n-address.json")
