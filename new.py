# GETTING THE OUTPUT 98%############################################################################

# import matplotlib.pyplot as plt
# import random

# # Function to read the dimensions from the input file
# def read_box_dimensions(file_name):
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
        
#     # Read big box dimensions from the first line
#     big_box = tuple(map(int, lines[0].strip().split()))  
    
#     # Read small box dimensions along with their names
#     small_boxes = []
#     for line in lines[1:]:
#         parts = line.strip().split()
#         if len(parts) == 3:  # Ensure each line has a name, width, and height
#             name, width, height = parts
#             small_boxes.append((name, int(width), int(height)))
    
#     return big_box, small_boxes

# # Function to calculate the area of a box
# def calculate_area(width, height):
#     return width * height

# # Function to check if the box fits in the given space
# def fits_in_space(x, y, width, height, big_width, big_height, occupied_spaces):
#     return (x + width <= big_width and y + height <= big_height and
#             not any(x < ox + ow and x + width > ox and y < oy + oh and y + height > oy
#                     for ox, oy, ow, oh in occupied_spaces))

# # Function to visualize the box arrangement with different colors
# def plot_boxes(big_box, placed_boxes, remaining_boxes):
#     plt.figure(figsize=(8, 8))
#     plt.xlim(0, big_box[0])
#     plt.ylim(0, big_box[1])
    
#     # Draw the big box
#     plt.gca().add_patch(plt.Rectangle((0, 0), big_box[0], big_box[1], fill=None, edgecolor='blue', linewidth=2, label='Big Box'))

#     # Define a list of colors for the boxes
#     colors = plt.cm.get_cmap('hsv', len(placed_boxes))  # Use a colormap for distinct colors
    
#     # Draw placed boxes with colors and annotations
#     for index, (x, y, width, height) in enumerate(placed_boxes):
#         plt.gca().add_patch(plt.Rectangle((x, y), width, height, fill=True, edgecolor='black', color=colors(index)))
#         plt.text(x + width / 2, y + height / 2, f'{width}x{height}', 
#                  ha='center', va='center', fontsize=10, color='white', weight='bold')
    
#     plt.title('Box Arrangement')
#     plt.xlabel('Width')
#     plt.ylabel('Height')
#     plt.grid()
#     plt.legend()
#     plt.show()

# # Function to find the optimal arrangement with better space utilization
# def fit_boxes_optimized(big_box, small_boxes):
#     big_width, big_height = big_box
#     big_area = calculate_area(big_width, big_height)
    
#     placed_boxes = []
#     remaining_boxes = []
    
#     occupied_spaces = []  # Track occupied spaces

#     def place_box(x, y, width, height):
#         if fits_in_space(x, y, width, height, big_width, big_height, occupied_spaces):
#             placed_boxes.append((x, y, width, height))
#             occupied_spaces.append((x, y, width, height))
#             return True
#         return False

#     # Try to place each box
#     for name, box_width, box_height in small_boxes:
#         placed = False

#         # Try placing the box in its original orientation
#         for x in range(big_width):
#             for y in range(big_height):
#                 if place_box(x, y, box_width, box_height):
#                     placed = True
#                     break
#             if placed:
#                 break

#         # If not placed, try rotating the box by 90 degrees
#         if not placed:
#             box_width, box_height = box_height, box_width  # Rotate the box
#             for x in range(big_width):
#                 for y in range(big_height):
#                     if place_box(x, y, box_width, box_height):
#                         placed = True
#                         break
#                 if placed:
#                     break

#         if not placed:
#             remaining_boxes.append((name, box_width, box_height))
    
#     used_area = sum(calculate_area(width, height) for _, _, width, height in placed_boxes)
#     utilization_percentage = (used_area / big_area) * 100
    
#     return placed_boxes, remaining_boxes, utilization_percentage

# # Function to try different box arrangements
# def try_different_arrangements(big_box, small_boxes):
#     best_utilization = 0
#     best_arrangement = None
#     arrangement_results = []

#     # Try all arrangements starting from B1...B10, B2...B10,B1, etc.
#     for i in range(len(small_boxes)):
#         current_arrangement = small_boxes[i:] + small_boxes[:i]
#         arrangement_name = f"Arrangement starting with {current_arrangement[0][0]}"
        
#         print(f"\n{arrangement_name}")  # Print arrangement name
        
#         # Fit boxes and get utilization
#         placed_boxes, remaining_boxes, utilization = fit_boxes_optimized(big_box, current_arrangement)
        
#         # Print the result for each arrangement
#         print(f"Big Box Area: {calculate_area(*big_box)}")
#         print(f"Used Area: {sum(calculate_area(w, h) for _, _, w, h in placed_boxes)}")
#         print(f"Area Utilization: {utilization:.2f}%")
#         print(f"Placed {len(placed_boxes)} boxes:")
#         for box in placed_boxes:
#             print(f"  {box[0]} at (x={box[0]}, y={box[1]}) with width={box[2]} and height={box[3]}")
#         print(f"Remaining {len(remaining_boxes)} boxes:")
#         for box in remaining_boxes:
#             print(f"  {box[0]} with width={box[1]} and height={box[2]}")

#         # Store the result
#         arrangement_results.append((arrangement_name, placed_boxes, remaining_boxes, utilization))

#         # If this is the best utilization so far, store it
#         if utilization > best_utilization:
#             best_utilization = utilization
#             best_arrangement = (arrangement_name, placed_boxes, remaining_boxes)
    
#     # Print best result in the terminal
#     if best_arrangement:
#         print(f"\nOptimal arrangement: {best_arrangement[0]}")
#         print(f"Maximum Utilization: {best_utilization:.2f}%")
#         print(f"Placed boxes: {len(best_arrangement[1])}")
#         print(f"Remaining boxes: {len(best_arrangement[2])}")
        
#         # Plot the best arrangement
#         plot_boxes(big_box, best_arrangement[1], best_arrangement[2])

# # Main function to execute the program
# def main():
#     input_file = 'input.txt'  # Make sure you have this file in your directory
    
#     # Read dimensions
#     big_box, small_boxes = read_box_dimensions(input_file)
#     print(f"Big box dimensions: {big_box}")
#     print(f"Small boxes: {small_boxes}")
    
#     # Sort small boxes by area (largest to smallest)
#     small_boxes.sort(key=lambda box: calculate_area(box[1], box[2]), reverse=True)
    
#     # Try different arrangements
#     try_different_arrangements(big_box, small_boxes)

# if __name__ == "__main__":
#     main()

########################################################################################################

# WITH CORECT ORDER
# import matplotlib.pyplot as plt

# # Function to read box dimensions from a text file
# def read_boxes_from_file(file_path):
#     boxes = []
#     with open(file_path, 'r') as file:
#         # Read big box dimensions
#         big_box_dimensions = file.readline().strip().split()
#         big_width = int(big_box_dimensions[0])
#         big_height = int(big_box_dimensions[1])
        
#         # Read small box dimensions
#         for line in file:
#             dimensions = line.strip().split()
#             width = int(dimensions[0])
#             height = int(dimensions[1])
#             boxes.append((width, height))
    
#     return big_width, big_height, boxes

# # Function to check if a box fits in the available space
# def fits_in_space(x, y, width, height, big_width, big_height, occupied_spaces):
#     if x + width > big_width or y + height > big_height:
#         return False
#     for (occupied_x, occupied_y, occupied_width, occupied_height) in occupied_spaces:
#         if (x < occupied_x + occupied_width and x + width > occupied_x and
#             y < occupied_y + occupied_height and y + height > occupied_y):
#             return False
#     return True

# # Function to try placing boxes in different orders
# def place_boxes_in_order(big_width, big_height, small_boxes):
#     sequence_order = [
#         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  # -B1,B2,B3,B4,B5,B6,B7,B8,B9,B10
#         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],  # -B2,B3,B4,B5,B6,B7,B8,B9,B10,B1
#         [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],  # -B3,B4,B5,B6,B7,B8,B9,B10,B1,B2
#         [3, 4, 5, 6, 7, 8, 9, 0, 1, 2],  # -B4,B5,B6,B7,B8,B9,B10,B1,B2,B3
#         [4, 5, 6, 7, 8, 9, 0, 1, 2, 3],  # -B5,B6,B7,B8,B9,B10,B1,B2,B3,B4
#         [5, 6, 7, 8, 9, 0, 1, 2, 3, 4],  # -B6,B7,B8,B9,B10,B1,B2,B3,B4,B5
#         [6, 7, 8, 9, 0, 1, 2, 3, 4, 5],  # -B7,B8,B9,B10,B1,B2,B3,B4,B5,B6
#         [7, 8, 9, 0, 1, 2, 3, 4, 5, 6],  # -B8,B9,B10,B1,B2,B3,B4,B5,B6,B7
#         [8, 9, 0, 1, 2, 3, 4, 5, 6, 7],  # -B9,B10,B1,B2,B3,B4,B5,B6,B7,B8
#         [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]   # -B10,B1,B2,B3,B4,B5,B6,B7,B8,B9
#     ]
    
#     best_placement = None
#     best_utilization = 0
    
#     for order in sequence_order:
#         print(f"Arrangement starting with B{order[0] + 1}")
#         occupied_spaces = []  # Track placed box locations
#         placed_boxes = []     # Track placed boxes' info
#         placed_successfully = []  # Track which boxes were placed
        
#         for index in order:
#             box = small_boxes[index]
#             box_width = box[0]
#             box_height = box[1]
#             placed = False
            
#             # Try to place the box in the available spaces
#             for x in range(big_width):
#                 for y in range(big_height):
#                     if fits_in_space(x, y, box_width, box_height, big_width, big_height, occupied_spaces):
#                         placed_boxes.append((x, y, box_width, box_height))
#                         occupied_spaces.append((x, y, box_width, box_height))
#                         placed = True
#                         placed_successfully.append(f"B{index + 1} placed at (x={x}, y={y}) with width={box_width} and height={box_height}")
#                         break
#                 if placed:
#                     break
            
#             if not placed:
#                 placed_successfully.append(f"B{index + 1} could not be placed (width={box_width}, height={box_height})")
        
#         # Calculate and display area utilization after each arrangement
#         used_area = sum([w * h for _, _, w, h in placed_boxes])
#         area_utilization = (used_area / (big_width * big_height)) * 100
#         print(f"Big Box Area: {big_width * big_height}")
#         print(f"Used Area: {used_area}")
#         print(f"Area Utilization: {area_utilization:.2f}%\n")
        
#         # Print the placement status of all boxes
#         print("Placement Status:")
#         for status in placed_successfully:
#             print(status)
        
#         # Track the best placement (highest area utilization)
#         if area_utilization > best_utilization:
#             best_utilization = area_utilization
#             best_placement = placed_boxes
    
#     return best_placement, best_utilization, big_width, big_height

# # Function to plot the best arrangement
# def plot_best_arrangement(best_placement, big_width, big_height):
#     fig, ax = plt.subplots()
#     ax.set_xlim(0, big_width)
#     ax.set_ylim(0, big_height)
#     ax.set_aspect('equal')
    
#     for (x, y, width, height) in best_placement:
#         ax.add_patch(plt.Rectangle((x, y), width, height, edgecolor='blue', facecolor='cyan', lw=2))
    
#     plt.gca().invert_yaxis()  # Invert Y-axis so that (0,0) is at the top-left corner
#     plt.title('Best Box Arrangement')
#     plt.show()

# # Main function
# def main():
#     # Path to the file containing box dimensions
#     file_path = "box_dimensions.txt"
    
#     # Read box dimensions from the file
#     big_width, big_height, small_boxes = read_boxes_from_file(file_path)
    
#     # Call the function to place boxes and calculate utilization
#     best_placement, best_utilization, big_width, big_height = place_boxes_in_order(big_width, big_height, small_boxes)
    
#     # Output the final best arrangement and area utilization
#     print(f"Optimal Arrangement Area Utilization: {best_utilization:.2f}%")
#     print("Placing boxes in the best arrangement:")
#     for idx, (x, y, width, height) in enumerate(best_placement):
#         print(f"  {idx} at (x={x}, y={y}) with width={width} and height={height}")
    
#     # Plot the best arrangement
#     plot_best_arrangement(best_placement, big_width, big_height)

# # Run the main function
# if __name__ == "__main__":
#     main()


# #######################################################################################################################################

# import matplotlib.pyplot as plt

# # Function to read box dimensions from a text file
# def read_boxes_from_file(file_path):
#     boxes = []
#     with open(file_path, 'r') as file:
#         # Read big box dimensions
#         big_box_dimensions = file.readline().strip().split()
#         big_width = int(big_box_dimensions[0])
#         big_height = int(big_box_dimensions[1])
        
#         # Read small box dimensions
#         for line in file:
#             dimensions = line.strip().split()
#             width = int(dimensions[0])
#             height = int(dimensions[1])
#             boxes.append((width, height))
    
#     return big_width, big_height, boxes

# # Function to check if a box fits in the available space
# def fits_in_space(x, y, width, height, big_width, big_height, occupied_spaces):
#     if x + width > big_width or y + height > big_height:
#         return False
#     for (occupied_x, occupied_y, occupied_width, occupied_height) in occupied_spaces:
#         if (x < occupied_x + occupied_width and x + width > occupied_x and
#             y < occupied_y + occupied_height and y + height > occupied_y):
#             return False
#     return True

# # Function to try placing boxes in different orders
# def place_boxes_in_order(big_width, big_height, small_boxes):
#     sequence_order = [
#         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  # -B1,B2,B3,B4,B5,B6,B7,B8,B9,B10
#         [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],  # -B2,B3,B4,B5,B6,B7,B8,B9,B10,B1
#         [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],  # -B3,B4,B5,B6,B7,B8,B9,B10,B1,B2
#         [3, 4, 5, 6, 7, 8, 9, 0, 1, 2],  # -B4,B5,B6,B7,B8,B9,B10,B1,B2,B3
#         [4, 5, 6, 7, 8, 9, 0, 1, 2, 3],  # -B5,B6,B7,B8,B9,B10,B1,B2,B3,B4
#         [5, 6, 7, 8, 9, 0, 1, 2, 3, 4],  # -B6,B7,B8,B9,B10,B1,B2,B3,B4,B5
#         [6, 7, 8, 9, 0, 1, 2, 3, 4, 5],  # -B7,B8,B9,B10,B1,B2,B3,B4,B5,B6
#         [7, 8, 9, 0, 1, 2, 3, 4, 5, 6],  # -B8,B9,B10,B1,B2,B3,B4,B5,B6,B7
#         [8, 9, 0, 1, 2, 3, 4, 5, 6, 7],  # -B9,B10,B1,B2,B3,B4,B5,B6,B7,B8
#         [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]   # -B10,B1,B2,B3,B4,B5,B6,B7,B8,B9
#     ]
    
#     best_placement = None
#     best_utilization = 0
    
#     for order in sequence_order:
#         print(f"Arrangement starting with B{order[0] + 1}")
#         occupied_spaces = []  # Track placed box locations
#         placed_boxes = []     # Track placed boxes' info
#         placed_successfully = []  # Track which boxes were placed
        
#         for index in order:
#             box = small_boxes[index]
#             box_width = box[0]
#             box_height = box[1]
#             placed = False
            
#             # Try to place the box in the available spaces
#             for x in range(big_width):
#                 for y in range(big_height):
#                     if fits_in_space(x, y, box_width, box_height, big_width, big_height, occupied_spaces):
#                         placed_boxes.append((x, y, box_width, box_height, f"B{index + 1}"))  # Add label with box info
#                         occupied_spaces.append((x, y, box_width, box_height))
#                         placed = True
#                         placed_successfully.append(f"B{index + 1} placed at (x={x}, y={y}) with width={box_width} and height={box_height}")
#                         break
#                 if placed:
#                     break
            
#             if not placed:
#                 placed_successfully.append(f"B{index + 1} could not be placed (width={box_width}, height={box_height})")
        
#         # Calculate and display area utilization after each arrangement
#         used_area = sum([w * h for _, _, w, h, _ in placed_boxes])
#         area_utilization = (used_area / (big_width * big_height)) * 100
#         print(f"Big Box Area: {big_width * big_height}")
#         print(f"Used Area: {used_area}")
#         print(f"Area Utilization: {area_utilization:.2f}%\n")
        
#         # Print the placement status of all boxes
#         print("Placement Status:")
#         for status in placed_successfully:
#             print(status)
        
#         # Track the best placement (highest area utilization)
#         if area_utilization > best_utilization:
#             best_utilization = area_utilization
#             best_placement = placed_boxes
    
#     return best_placement, best_utilization, big_width, big_height

# # Function to plot the best arrangement
# def plot_best_arrangement(best_placement, big_width, big_height):
#     fig, ax = plt.subplots()
#     ax.set_xlim(0, big_width)
#     ax.set_ylim(0, big_height)
#     ax.set_aspect('equal')
    
#     for (x, y, width, height, label) in best_placement:
#         ax.add_patch(plt.Rectangle((x, y), width, height, edgecolor='blue', facecolor='cyan', lw=2))
#         ax.text(x + width/2, y + height/2, label, ha='center', va='center', color='white', fontsize=12)  # Add the label on each box
    
#     plt.gca().invert_yaxis()  # Invert Y-axis so that (0,0) is at the top-left corner
#     plt.title('Best Box Arrangement')
#     plt.show()

# # Main function
# def main():
#     # Path to the file containing box dimensions
#     file_path = "box_dimensions.txt"  # Make sure the file path is correct
    
#     # Read box dimensions from the file
#     big_width, big_height, small_boxes = read_boxes_from_file(file_path)
    
#     # Call the function to place boxes and calculate utilization
#     best_placement, best_utilization, big_width, big_height = place_boxes_in_order(big_width, big_height, small_boxes)
    
#     # Output the final best arrangement and area utilization
#     print(f"Optimal Arrangement Area Utilization: {best_utilization:.2f}%")
#     print("Placing boxes in the best arrangement:")
#     for idx, (x, y, width, height, label) in enumerate(best_placement):
#         print(f"  {label} at (x={x}, y={y}) with width={width} and height={height}")
    
#     # Plot the best arrangement
#     plot_best_arrangement(best_placement, big_width, big_height)

# # Run the main function
# if __name__ == "__main__":
#     main()


# ##################################### FOR THE POWER CONSUMPTION CODE!!!!!!!!!!!!!!!!!!1

import matplotlib.pyplot as plt

# Function to read box dimensions from a text file
def read_boxes_from_file(file_path):
    boxes = []
    with open(file_path, 'r') as file:
        # Read big box dimensions
        big_box_dimensions = file.readline().strip().split()
        big_width = int(big_box_dimensions[0])
        big_height = int(big_box_dimensions[1])
        
        # Read small box dimensions and power
        for line in file:
            dimensions = line.strip().split()
            width = int(dimensions[0])
            height = int(dimensions[1])
            power = int(dimensions[2])  # Power consumption
            boxes.append((width, height, power))
    
    return big_width, big_height, boxes

# Function to check if a box fits in the available space
def fits_in_space(x, y, width, height, big_width, big_height, occupied_spaces):
    if x + width > big_width or y + height > big_height:
        return False
    for (occupied_x, occupied_y, occupied_width, occupied_height) in occupied_spaces:
        if (x < occupied_x + occupied_width and x + width > occupied_x and
            y < occupied_y + occupied_height and y + height > occupied_y):
            return False
    return True

# Function to check power constraint between adjacent boxes
def check_power_constraint(box1, box2, power_threshold):
    total_power = box1[2] + box2[2]  # sum of the powers of two boxes
    return total_power <= power_threshold

# Function to try placing boxes in different orders
def place_boxes_in_order(big_width, big_height, small_boxes, power_threshold):
    sequence_order = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],
        [3, 4, 5, 6, 7, 8, 9, 0, 1, 2],
        [4, 5, 6, 7, 8, 9, 0, 1, 2, 3],
        [5, 6, 7, 8, 9, 0, 1, 2, 3, 4],
        [6, 7, 8, 9, 0, 1, 2, 3, 4, 5],
        [7, 8, 9, 0, 1, 2, 3, 4, 5, 6],
        [8, 9, 0, 1, 2, 3, 4, 5, 6, 7],
        [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    
    best_placement = None
    best_utilization = 0
    
    for order in sequence_order:
        print(f"Arrangement starting with B{order[0] + 1}")
        occupied_spaces = []  # Track placed box locations
        placed_boxes = []     # Track placed boxes' info
        placed_successfully = []  # Track which boxes were placed
        
        for index in order:
            box = small_boxes[index]
            box_width = box[0]
            box_height = box[1]
            placed = False
            
            # Try to place the box in the available spaces
            for x in range(big_width):
                for y in range(big_height):
                    if fits_in_space(x, y, box_width, box_height, big_width, big_height, occupied_spaces):
                        # Check power constraint if this box is adjacent to another
                        if len(occupied_spaces) > 0:
                            last_box = occupied_spaces[-1]  # Last placed box
                            last_x, last_y, last_width, last_height = last_box[:4]
                            # Check if the box is adjacent horizontally or vertically
                            if (abs(x - last_x) <= last_width or abs(y - last_y) <= last_height):
                                if not check_power_constraint(box, small_boxes[order[occupied_spaces.index(last_box)]], power_threshold):
                                    continue  # Skip placing this box due to power constraint

                        placed_boxes.append((x, y, box_width, box_height, f"B{index + 1}"))
                        occupied_spaces.append((x, y, box_width, box_height))
                        placed = True
                        placed_successfully.append(f"B{index + 1} placed at (x={x}, y={y}) with width={box_width} and height={box_height}")
                        break
                if placed:
                    break
            
            if not placed:
                placed_successfully.append(f"B{index + 1} could not be placed (width={box_width}, height={box_height})")
        
        # Calculate and display area utilization after each arrangement
        used_area = sum([w * h for _, _, w, h, _ in placed_boxes])
        area_utilization = (used_area / (big_width * big_height)) * 100
        print(f"Big Box Area: {big_width * big_height}")
        print(f"Used Area: {used_area}")
        print(f"Area Utilization: {area_utilization:.2f}%\n")
        
        # Print the placement status of all boxes
        print("Placement Status:")
        for status in placed_successfully:
            print(status)
        
        # Track the best placement (highest area utilization)
        if area_utilization > best_utilization:
            best_utilization = area_utilization
            best_placement = placed_boxes
    
    return best_placement, best_utilization, big_width, big_height

# Function to plot the best arrangement
def plot_best_arrangement(best_placement, big_width, big_height):
    fig, ax = plt.subplots()
    ax.set_xlim(0, big_width)
    ax.set_ylim(0, big_height)
    ax.set_aspect('equal')
    
    for (x, y, width, height, label) in best_placement:
        ax.add_patch(plt.Rectangle((x, y), width, height, edgecolor='blue', facecolor='cyan', lw=2))
        ax.text(x + width/2, y + height/2, label, ha='center', va='center', color='white', fontsize=12)  # Add the label on each box
    
    plt.gca().invert_yaxis()  # Invert Y-axis so that (0,0) is at the top-left corner
    plt.title('Best Box Arrangement')
    plt.show()

# Main function
def main():
    # Path to the file containing box dimensions
    file_path = "box_dimensions.txt"  # Make sure the file path is correct
    
    # Read box dimensions from the file
    big_width, big_height, small_boxes = read_boxes_from_file(file_path)
    
    # Set power threshold for placing boxes side by side (e.g., 6W)
    power_threshold = 10
    
    # Call the function to place boxes and calculate utilization
    best_placement, best_utilization, big_width, big_height = place_boxes_in_order(big_width, big_height, small_boxes, power_threshold)
    
    # Output the final best arrangement and area utilization
    print(f"Optimal Arrangement Area Utilization: {best_utilization:.2f}%")
    print("Placing boxes in the best arrangement:")
    for idx, (x, y, width, height, label) in enumerate(best_placement):
        print(f"  {label} at (x={x}, y={y}) with width={width} and height={height}")
    
    # Plot the best arrangement
    plot_best_arrangement(best_placement, big_width, big_height)

# Run the main function
if __name__ == "__main__":
    main()
