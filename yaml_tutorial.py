import yaml
# YAML:
# similar to JavaScript Object Notation (JSON).
# extension  .yml, .yaml
# data serialization language - stores infomation nicely (key value pairs, objects, list)
# Readability
# indintation defines scope
def yaml_loader(filepath):
    with open(filepath, 'r') as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath,data):
    with open(filepath,"w") as file_descriptor:
        yaml.dump(data,file_descriptor)

if __name__ == "__main__":
    file_path = 'yaml_tutorial.ymal'
    data = yaml_loader(file_path)

    print data

    master_config = data.get('MasterConfig')
    for item_name, item_value in master_config.iteritems():
        print item_name, item_value

    file_path_2= 'yaml_tutorial_2.ymal'
    data2 = {"MasterConfig2":
    {
        "config1": 1
        ,"config2": 2
         }
    }

    yaml_dump(filepath=file_path_2,data=data2)
