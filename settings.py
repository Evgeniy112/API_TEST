valid_header_sol = {
    'sol': 1000,
    'camera': 'FHAZ',
    'api_key': 'DEMO_KEY',
    'page': 1
}
valid_header_earth_date = {
    'api_key': 'DEMO_KEY',
    'camera': 'FHAZ',
    'page': 1,
    'earth_date': '2022-03-25'
}
invalid_header_earth_date_63 = {
    'earth_date': '2022-03-25',
    'camera': 'FHAZ',
    'api_key': 132,
    'page': 1
}
invalid_header_sol_124 = {
    'sol': 0,
    'camera': '',
    'api_key': 'DEMO_KEY',
    'page': 'fghyjf'
}
