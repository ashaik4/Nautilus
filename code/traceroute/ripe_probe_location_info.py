import subprocess
import pickle
from pathlib import Path
import certifi
import os
import urllib3
import requests
from pprint import pprint

# 👇 Disable warnings about insecure SSL (since we are bypassing verification)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

RIPE_ATLAS_URL = "https://atlas.ripe.net/api/v2/probes/"
OUTPUT_FILE = Path("stats/all_ripe_probes_ip_and_coordinates")

def run_ripe_atlas_query_to_get_all_probe_locations():
	probe_to_coordinate_map = {}
	page_url = RIPE_ATLAS_URL + "?status=1&fields=id,address_v4,geometry&page_size=500"

	while page_url:
		print(f"Fetching: {page_url}")
		try:
			response = requests.get(page_url, verify=False)  # 🚨 SSL cert check bypassed here
			data = response.json()
		except requests.exceptions.RequestException as e:
			print(f"❌ Request failed: {e}")
			break

		for probe in data.get("results", []):
			probe_id = str(probe.get("id"))
			address_v4 = probe.get("address_v4", "")
			geometry = probe.get("geometry", {})

			try:
				lat, lon = geometry.get("coordinates", -1111.0)[0], geometry.get("coordinates", -1111.0)[1]
			except: 
				print("error")

			if -1111.0 not in (lat, lon):
				probe_to_coordinate_map[probe_id] = (address_v4, (lat, lon))

		page_url = data.get("next")

	return probe_to_coordinate_map


def save_probe_location_result (probe_to_coordinate_map):

	with open('stats/all_ripe_probes_ip_and_coordinates', 'wb') as fp:
		pickle.dump(probe_to_coordinate_map, fp)


def load_probe_location_result():


	if Path(Path.cwd() / 'stats/all_ripe_probes_ip_and_coordinates').exists():
		with open('stats/all_ripe_probes_ip_and_coordinates', 'rb') as fp:
			probe_to_coordinate_map = pickle.load(fp)
	else:
		print ('File was missing, running the queries again')
		probe_to_coordinate_map = run_ripe_atlas_query_to_get_all_probe_locations()
		save_probe_location_result(probe_to_coordinate_map)

	return probe_to_coordinate_map


if __name__ == '__main__':

	probe_to_coordinate_map = run_ripe_atlas_query_to_get_all_probe_locations()

	print (f'We have results for {len(probe_to_coordinate_map)} probes and we are saving results now')

	save_probe_location_result(probe_to_coordinate_map)

	print ('Loading the results to verify')

	probe_to_coordinate_map = load_probe_location_result()

	print (f'We have results for {len(probe_to_coordinate_map)} probes')
