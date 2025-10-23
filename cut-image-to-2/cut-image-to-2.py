from PIL import Image
import os

def split_image(image_path):
    """
    Splits an image into two equal vertical halves.
    """
    try:
        img = Image.open(image_path)
        width, height = img.size

        midpoint = width // 2

        left_box = (0, 0, midpoint, height)
        left_half = img.crop(left_box)

        right_box = (midpoint, 0, width, height)
        right_half = img.crop(right_box)

        base_name, extension = os.path.splitext(image_path)
        
        filename_a = f"{base_name}A{extension}"
        filename_b = f"{base_name}B{extension}"

        left_half.save(filename_a)
        right_half.save(filename_b)
        
        print(f"  -> Successfully split into '{filename_a}' and '{filename_b}'")

    except Exception as e:
        print(f"  -> An error occurred while processing {image_path}: {e}")

def process_all_images_in_folder():
    """
    Finds and processes all images in the current folder.
    """
    # Add or remove extensions as needed
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    processed_count = 0

    # os.listdir('.') lists all files in the current directory
    for filename in os.listdir('.'):
        # Check if the file has a valid image extension
        if filename.lower().endswith(valid_extensions):
            base_name, ext = os.path.splitext(filename)
            
            # Skip files that already end with 'A' or 'B'
            if base_name.upper().endswith('A') or base_name.upper().endswith('B'):
                print(f"Skipping '{filename}' (already a split part).")
                continue
            
            print(f"Processing '{filename}'...")
            split_image(filename)
            processed_count += 1
    
    if processed_count == 0:
        print("No new images found to process.")
    else:
        print(f"\nFinished processing {processed_count} image(s).")


# --- Main execution block ---
if __name__ == "__main__":
    process_all_images_in_folder()
    print("\nScript finished. Press Enter to exit.")
    input() # Pauses the script to see the output