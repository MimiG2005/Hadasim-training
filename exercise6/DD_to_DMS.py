def DD_to_DMS(DDObj):
    lon = DDObj[0]
    lat = DDObj[1]

    lon_dir = 'E' if lon >= 0 else 'W'
    lat_dir = 'N' if lat >= 0 else 'S'

    abs_lon = abs(lon)
    abs_lat = abs(lat)

    DMS_degree_W = int(abs_lon)
    DMS_min_W = int((abs_lon - DMS_degree_W) * 60)
    DMS_sec_W = (abs_lon - DMS_degree_W - DMS_min_W / 60) * 3600

    DMS_degree_N = int(abs_lat)
    DMS_min_N = int((abs_lat - DMS_degree_N) * 60)
    DMS_sec_N = (abs_lat - DMS_degree_N - DMS_min_N / 60) * 3600

    result = [
        [DMS_degree_W, DMS_min_W, DMS_sec_W, lon_dir],
        [DMS_degree_N, DMS_min_N, DMS_sec_N, lat_dir],
        DDObj[2] if len(DDObj) > 2 else None
    ]
    return result


DD_coords = [-149.9002, 61.2181, 30]
DMS_coords = DD_to_DMS(DD_coords)
print(DMS_coords)
