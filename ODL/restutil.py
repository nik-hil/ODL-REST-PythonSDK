import json

def write_json_file(data,file='jsonfile.json'):
    jsonfile = open(file,'w')
    jsonfile.write(json.dumps(data, indent=2, sort_keys=True, separators=(',', ': ')))
    jsonfile.close()