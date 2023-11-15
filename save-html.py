# Define the number of levels
num_levels = 4

# For each level of detail
for i in range(num_levels):
    # Calculate the number of tiles per side for this level
    tiles_per_side = 2**i

    # Start the HTML file
    html = '<html><body>'

    # For each tile, reverse the y-axis
    for y in range(tiles_per_side-1, -1, -1):
        html += '<div>'
        for x in range(tiles_per_side):
            # Construct the URL for this tile image
            url = f'./images/level_{i}_tile_{x}_{y}.png'

            # Add the image to the HTML
            html += f'<img src="{url}" style="width:256px;height:256px;">'
        html += '</div>'

    # End the HTML file
    html += '</body></html>'

    # Write the HTML to a file
    with open(f'level_{i}_image.html', 'w') as f:
        f.write(html)