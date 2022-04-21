def config_parse(config):
   match config:
        case {"route" : route}:
            print(f"route is {route}") 
        case {"persistent" : "no"}:
           print("No persistance")      
        case {"persistent" : "yes", **rest}:
           print(f"persistance {rest} ")
# start here
    
config_parse({"route":"127.0.0.1"})
config_parse({"route": "127.0.0.2","persistent" : "no"})
config_parse({"persistent" : "no","route": "127.0.0.3"})
config_parse({"persistent" : "no"})
config_parse({"persistent": "yes","test" : 2, "warn" : "off"})
config_parse({"persistent" : "yes"})