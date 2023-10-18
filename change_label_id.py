import os


def replace_class_ids_in_annotations(input_files, id_mapping, path):
    for input_file in input_files:
        if input_file.lower().endswith(".txt") and "README" not in input_file:
            file_path = os.path.join(main_dir, path, input_file)
            with open(file_path, 'r') as infile:
                lines = infile.readlines()

            with open(file_path, 'w') as outfile:
                for line in lines:
                    items = line.strip().split(' ')
                    old_class_id = int(items[0])
                    if old_class_id in id_mapping:
                        new_class_id = id_mapping[old_class_id]
                        items[0] = str(new_class_id)
                    outfile.write(' '.join(items) + '\n')


# Example usage:

main_dir = "C:\\Users\\emiel\\OneDrive\\Documenten\\CoinDetection\\datasets"


dir_5_euro = "Euro 5.v1i.yolov8\\labels"
dir_5_euro_dict = {
    0: 3
}
replace_class_ids_in_annotations(os.listdir(os.path.join(main_dir, dir_5_euro)), dir_5_euro_dict, dir_5_euro)

dir_10_euro = "Euro10.v10i.yolov8\\labels"
dir_10_euro_dict = {
    0: 4
}
replace_class_ids_in_annotations(os.listdir(os.path.join(main_dir, dir_10_euro)), dir_10_euro_dict, dir_10_euro)

dir_20_euro = "Euro 20.v1i.yolov8\\labels"
dir_20_euro_dict = {
    0: 5
}
replace_class_ids_in_annotations(os.listdir(os.path.join(main_dir, dir_20_euro)), dir_20_euro_dict, dir_20_euro)

dir_50_euro = "Euro 50 new.v1i.yolov8\\labels"
dir_50_euro_dict = {
    0: 6
}
replace_class_ids_in_annotations(os.listdir(os.path.join(main_dir, dir_50_euro)), dir_50_euro_dict, dir_50_euro)

dir_100_euro = "euro100.v1i.yolov8\\labels"
dir_100_euro_dict = {
    0: 7
}
replace_class_ids_in_annotations(os.listdir(os.path.join(main_dir, dir_100_euro)), dir_100_euro_dict, dir_100_euro)


dir_nomi_pascal_dataset = "Dataset format conversion.v5-nomi_pascal_dataset.yolov8\\labels"
#['100euro', '10euro', '20euro', '50euro', '5euro']
dir_nomi_pascal_dataset_dict = {
    0: 7,
    1: 4,
    2: 5,
    3: 6,
    4: 3
}
replace_class_ids_in_annotations(os.listdir(os.path.join(main_dir, dir_nomi_pascal_dataset)),
                                 dir_nomi_pascal_dataset_dict, dir_nomi_pascal_dataset)


dir_coins = "Euros.v1-coins.yolov8\\labels"
#['1-EUR', '2-EUR', '50-EUR']
dir_coins_dict = {
    0: 0,
    1: 1,
    2: 6,
}
replace_class_ids_in_annotations(os.listdir(os.path.join(main_dir, dir_coins)),
                                 dir_coins_dict, dir_coins)

dir_projec = "Projec2.v3i.yolov8\\labels"
#['1', '10', '100', '2', '20', '200', '5', '50']
dir_projec_dict = {
    0: 0,
    1: 4,
    2: 7,
    3: 1,
    4: 5,
    5: 8,
    6: 3,
    7: 6
}
replace_class_ids_in_annotations(os.listdir(os.path.join(main_dir, dir_projec)),
                                 dir_projec_dict, dir_projec)



