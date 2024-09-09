import csv

# Open the input CSV file for reading
i = 1
while i < 26:
    csv_file = f'messages_{i}.csv'
    with open(csv_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        # Specify the columns you want to keep
        selected_columns = [
            'post_id',
            'post_text',
            'original_text',
            'shared_text',
            'time',
            'image_lowquality',
            'images_lowquality_description',
            'video',
            'video_thumbnail',
            'likes',
            'comments',
            'post_url',
            'link',
            'username',
            'is_live',
            'reaction_count',
            'was_live'
        ]

        # Open the output CSV file for writing
        with open(f'mini_{csv_file}', mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=selected_columns)

            # Write the header (column names)
            writer.writeheader()

            # Write only the selected columns from each row
            for row in reader:
                filtered_row = {col: row[col] for col in selected_columns}
                writer.writerow(filtered_row)
    i += 1
    print(f"{csv_file} with selected columns has been saved.")
