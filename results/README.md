# Structure of an entry of each Nautilus results

## The IP link to cable mapping (link_to_cable_and_score_mapping_sol_validated_v4 and link_to_cable_and_score_mapping_sol_validated_v6)

These files are saved as python dictionaries where the key is the IP link and the value is the data associated with the cable mappings. The cable mapping data is structured as

{
    the number of potential submarine cables that could be mapped to the IP link,
    the list of filtered submarine cables corresponding to the IP link,
    the prediction score associated with each cable mapped,
    the corresponding list of landing points for the cable mapped,
    the category mapped to the IP link by Nautilus
}

An example is shown below:

('129.250.6.128', '129.250.2.242') : (6, ['APCN-2', 'Asia Submarine-cable Express (ASE)/Cahaya Malaysia'], [0.9821555163233112, 0.9631944956491411], [[(5885, 5939), (5703, 5939)], [(5887, 5902)]], 'bg_oc')

where 6 corresponds to the # of submarine cables mapped by Nautilus initially, ['APCN-2', 'Asia Submarine-cable Express (ASE)/Cahaya Malaysia'] corrsponds to the cables Nautilus identifies after its final pruning steps, [0.9821555163233112, 0.9631944956491411] corresponds to the prediction scores associated with APCN-2 and ASE cables respectively and 'bg_oc' which indicates 'Both good geolocation and Definite Submarine Link' catgeory being attached to ('129.250.6.128', '129.250.2.242') link.

## The Validated IP to Geolocation mapping meta-information (all_validated_ip_location_v4 and all_validated_ip_location_v6)

These files are python dictionaries and the structure for an entry is as follows 

{
    'location_index': <The list of indices, always 0 to 9)>,
    'coordinates': <The list of coordinates corresponding to the indices>,
    'penalty_count': <The list of count of the number of traceroutes for which the SoL validation failed for a given coordinate',
    'total_count': <The list of the total number of traceroutes, typically 0 (for sources which had no geolocation output) and x (the number of traceroutes)
}

An entry in each of these lists corresponding to location_index, coordinates, penalty_count and total_count correspond to a specific geolocation service.
