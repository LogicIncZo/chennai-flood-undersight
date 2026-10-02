import json, csv, re
from xml.etree import ElementTree as ET

NS = {"wfs":"http://www.opengis.net/wfs/2.0","ows":"http://www.opengis.net/ows/1.1"}
t = ET.parse("getcapabilities.xml")
root = t.getroot()

counts = {}
with open("/home/workspace/UngalSoththu/chennai-flood-undersight/docs/wfs_census_2026-09-29.csv") as f:
    for row in csv.DictReader(f):
        try: counts[row["layer"]] = int(row["count"])
        except ValueError: counts[row["layer"]] = None

def wc(name):  # word-count splitter for CamelCase / snake_case
    s = name.replace("_"," ")
    return len(re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])", s))

UPPER = {"rfs","ecmwf","ncep","gfs","ukmo","imd","ncmrwf","srg","aws","arg","awlr","gcc","wrd","cmwssb","twad","nrsc","irs","lulc","dgps","iitm","cma","pwd","hq","nem","idw","gds","irl","ndvi","gnv","aoi","dem","cfms","amc","usd","dsmwsm","tnuiFSL".lower()}
LOWER = {"or","of","the","by","with","and","for","in","a"}
LABELS = {"chennai","basin","cma","gcc","tiruvallur","kancheepuram","chengalpattu","vellore"}

def friendly(short):
    s = short
    s = re.sub(r"_withlabel$", "", s); lab = s != short
    for p in ["gis_flood_inundation_","gis_flood_hotspots_","gis_scenario_waterlevel_","gis_waterlevel_display_","gis_administrative_units_","gis_lulc_","station_","transaction_","gis_","wms_","wfs_","get_"]:
        if s.startswith(p): s = s[len(p):]
    s = re.sub(r"^bulletin_", "", s)
    s = s.replace("districtmap_observedrainfallbulletin","district_map").replace("_observedrainfallbulletin","")
    toks = s.split("_")
    out = []
    for t in toks:
        tl = t.lower()
        if tl in UPPER: out.append(t.upper())
        elif tl == "observedrainfall": out.append("observed rainfall")
        elif tl == "waterdepth": out.append("water depth")
        elif tl == "minmax": out.append("min/max")
        elif tl == "streetnames": out.append("street names")
        elif tl == "withlabel": out.append("labels")
        elif tl == "manmade": out.append("man-made")
        elif tl == "keyloactions": out.append("key locations")
        elif tl == "rrls": out.append("RRLS")
        elif tl in ("web","max","control","controlweb","controlmax","rainforecast","rainforecastweb","rainforecastcontrol"): out.append(t)
        else: out.append(t.capitalize() if len(t) > 3 and t.islower() else t)
    t = " ".join(out)
    if lab: t += " (labels)"
    return t

def cat(name):
    n = name.lower()
    if "utilities" in n or "office" in n or "street" in n or "road" in n or "structure" in n or "parcel" in n or "location" in n or "keyloaction" in n or "railway" in n or "building" in n: return "infra"
    if re.search(r"\b(gis_)?(flood|inundation)", n) or "warning" in n or "crowdsourc" in n or "waterdepth" in n or "hotspot" in n: return "flood"
    if "stations" in n or re.search(r"(^|_)transaction", n) or re.search(r"\b(srg|aws|arg|awlr|agro)\b", n) or "rainfall" in n or "rain" in n or "gauge" in n or "waterlevel" in n or "anemometer" in n or "thermometer" in n or "humidity" in n or "evaporim" in n or "sunenergy" in n or "plank" in n or "radarpressure" in n or "shaftencoder" in n or "sql" in n or "idw" in n or re.search(r"\bgds\b", n) or re.search(r"\baws_new\b", n): return "stations"
    if "ward" in n or "zone" in n or "administr" in n or "boundary" in n or "basin" in n or "district" in n or "subbasin" in n or "watershed" in n or "cmwssb" in n or "catchment" in n: return "admin"
    if "waterbody" in n or "waterbodie" in n or "lake" in n or "tank" in n or "reservoir" in n or "spillway" in n or "bathym" in n: return "waterbodies"
    if "waterway" in n or "drain" in n or "river" in n or "canal" in n or "stream" in n or "channel" in n: return "waterways"
    if "bathym" in n or "contour" in n or "soil" in n or "lulc" in n or "geomorph" in n or "geolog" in n or "landuse" in n or "levelling" in n or "dgps" in n or "slope" in n: return "terrain"
    if "forecast" in n or "ensemble" in n or "ecmwf" in n or "ecmf" in n or "ncep" in n or "ncmrwf" in n or "gfs" in n or "ukmo" in n or "imd" in n or "controlweb" in n or "controlmax" in n or "iitmcontrol" in n or "element" in n or "onedimmodel" in n or re.search(r"\brfs\b", n): return "forecast"
    if "bulletin" in n: return "bulletin"
    if re.search(r"\btmp_table\b|\btestview\b|\bsurface_test\b|transaction_master", n): return "internal"
    return "other"

TITLE_FIX = {
 "ChennaiDSS:flood_1976": "Flood extent 1976",
 "ChennaiDSS:waterbodies_1972": "Water bodies 1972 baseline",
}

layers = []
for ft in root.iter("{http://www.opengis.net/wfs/2.0}FeatureType"):
    name = ft.findtext("wfs:Name", default="", namespaces=NS)
    title = ft.findtext("wfs:Title", default="", namespaces=NS) or name.split(":",1)[-1]
    lc = ft.find("ows:WGS84BoundingBox", NS)
    bbox = None
    if lc is not None:
        try:
            ll = [float(x) for x in lc.findtext("ows:LowerCorner", namespaces=NS).split()]
            ur = [float(x) for x in lc.findtext("ows:UpperCorner", namespaces=NS).split()]
            if abs(ll[0]) <= 180.5 and abs(ll[1]) <= 90.5: bbox = [ll[0], ll[1], ur[0], ur[1]]
        except Exception: pass
    layers.append({
        "name": name,
        "short": name.split(":",1)[-1],
        "title": TITLE_FIX.get(name, friendly(name.split(":",1)[-1])),
        "count": counts.get(name),
        "bbox": bbox,
        "cat": cat(name),
        "words": wc(name),
    })

layers.sort(key=lambda l: (l["cat"], -(l["count"] or 0)))
out = {"generated": "2026-10-02", "endpoint": "https://chennaifloodmonitor.tn.gov.in/geohorr/ChennaiDSS/ows", "count": len(layers), "layers": layers}
json.dump(out, open("catalog.json","w"), ensure_ascii=False)
from collections import Counter
print("layers:", len(layers), "| categories:", dict(Counter(l["cat"] for l in layers)))
print("sample:", json.dumps(layers[0], ensure_ascii=False))
