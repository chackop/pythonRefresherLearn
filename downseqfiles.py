import os
import re
import urllib.request
import urllib.parse


def download_sequence_files(first_url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    url_head, url_tail = os.path.split(first_url)
    first_index = int(re.findall(r"[0-9]+", url_tail)[-1])
    index_count, error_count = 0, 0
    while error_count < 5:
        next_index = str(int(first_index) + index_count)
        if first_index[0] == "0":
            next_index = "0" * (len(first_index) - len(next_index)) + next_index
        next_url = urllib.parse.urljoin(
            url_head, re.sub(first_index, next_index, url_tail)
        )
        try:
            output_file = os.path.join(output_dir, os.path.basename(next_url))
            urllib.request.urlretrieve(next_url, output_file)
            print(f"Downloaded: {next_url} -> {output_file}")
        except IOError as e:
            print(f"Error downloading {next_url}: {e}")
            error_count += 1
