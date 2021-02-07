import csv

#ouverture du fichier .xslx
with open('stm_arrets_sig.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    line_count = 0
    stop_id = [] #id de l'arret
    lignes = [] #numeros de lignes passant par l'arret
    stop_name = [] #nom de l'arret
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        stop_id.append(row['stop_id'])
        stop_name.append(row['stop_name'])
        lignes.append(row['route_id'])
        line_count += 1
    print(stop_id)
    print(stop_name)
    print(lignes)
    print(f'Processed {line_count} lines.')
