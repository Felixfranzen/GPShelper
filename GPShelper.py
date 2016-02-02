# -*- coding: utf-8 -*-
import sys
import copy

def read_file_data():
   
    cmdprompt_file = sys.argv[1]
    with open(cmdprompt_file) as f:
            f.readline()
            org_data = f.readlines()
            new_data = [x.strip().split() for x in org_data]
    return new_data

def location_dict(data):
   
    locations = {}
   
    counter = -1
    for lines in data:
   
        if not lines[0] in locations:
            counter += 1
            locations[lines[0]] = counter      
        if not lines[1] in locations:
            counter += 1
            locations[lines[1]] = counter                        
    return locations

def reverse_dict(dictionary):
    rev_dict = {}
    for loc,index in dictionary.iteritems():
        rev_dict[index] = loc
    return rev_dict
        

def standard_matrice(nodes):
   
    INF = 9999999
    size = len(nodes)
    matrice = [[INF for i in range(size)]for i in range(size)]
    return matrice 

def distance_matrice(matrice,location,data):
   
    for key in location:
        matrice[location[key]][location[key]] = 0
    
   
    for i in data:
        matrice[location[i[0]]][locations[i[1]]] = int(i[2])
        matrice[location[i[1]]][locations[i[0]]] = int(i[2])
    return matrice

def floyd_traverse(matrice,locations):
    path = copy.deepcopy(matrice)
    INF = 9999999
    n = range(len(locations))
    for i in n:
        for j in n:
            if (i==j or matrice[i][j] == INF):
                path[i][j] = -1
            else:
                path[i][j] = i
    
    for k in n:
        for i in n:
            for j in n:
                if (matrice[i][j] > (matrice[i][k] + matrice[k][j])):
                    path[i][j] = path[k][j]
                matrice[i][j] = min(matrice[i][j],(matrice[i][k] + matrice[k][j]))    
  
    return path

def path_finder(matrice1,locations,user_data):
    try:
        if user_data[0] != user_data[1]:
            
            try:
                node_1 = locations[user_data[1]]
                node_2 = locations[user_data[0]]
                path = "%s " % user_data[0]
                
            except KeyError:
                return False
            
            found = False
            while found == False:
                if not matrice1[node_1][node_2] == node_1:
                    path += "%s " % rev_loc[matrice1[node_1][node_2]]
                    node_2 = matrice1[node_1][node_2]
                
                elif matrice1[node_1][node_2] == node_1:
                    path += "%s" % user_data[1]
                    found = True
                    return path
                
                else:
                    found = True
                    return "No route"
        else:
            return False

    except:
        return False

def path_print(string_input,matrice,locations):
    string = string_input.split(" ")
    for i in string:
        if string.index(i)+1 != len(string):
            node_1 = locations[string[string.index(i)]]
            node_2 = locations[string[string.index(i)+1]]
            print "%s %s %i" % (string[string.index(i)], string[string.index(i)+1], matrice[node_1][node_2])
    
while True:
   
    user_input_org = raw_input("Enter origin and destination: ")
    user_data = user_input_org.split(" ")
    if user_data != ["quit"]:
    
        file_data = read_file_data() 
    
        locations = location_dict(file_data)
        
        rev_loc = reverse_dict(locations)
        stand_mat = standard_matrice(locations) 
         
    
        dest_mat = distance_matrice(stand_mat,locations,file_data)
        
    
        traverse = floyd_traverse(dest_mat,locations)
        path = path_finder(traverse,locations,user_data)
        if path == False:
            print "No route"
        else:
    
            path_print(path,dest_mat,locations)
    else:
        sys.exit()
 
