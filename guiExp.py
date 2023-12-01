# this is the early stages of my gui work, hoping to get more done soon. 



import tkinter as tk






















from PIL import Image, ImageTk

class MapGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GPS Map Viewer")
        self.root.geometry("800x800")

        # Placeholder for GPS data (latitude, longitude)
        self.gps_data = (0.0, 0.0)

        # Load a sample map image
        self.map_image = Image.open("sample_map_image.jpg")  # Replace with your map image

        # Create canvas to display the map
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()

        # Display the map image
        self.display_map()

    def update_gps_data(self, latitude, longitude):
        # Update GPS data
        self.gps_data = (latitude, longitude)

        # Update the map display
        self.display_map()

    def display_map(self):
        # Clear previous drawings on the canvas
        self.canvas.delete("all")

        # Convert latitude and longitude to pixel coordinates (for demonstration purposes)
        pixel_x = int((self.gps_data[1] + 180) * (800 / 360))
        pixel_y = int((90 - self.gps_data[0]) * (800 / 180))

        # Display the map image
        map_photo = ImageTk.PhotoImage(self.map_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=map_photo)

        # Display a marker at the GPS location
        self.canvas.create_oval(pixel_x - 5, pixel_y - 5, pixel_x + 5, pixel_y + 5, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = MapGUI(root)
    # Replace the following line with actual GPS data updates
    app.update_gps_data(37.7749, -122.4194)  # San Francisco coordinates
    root.mainloop()

